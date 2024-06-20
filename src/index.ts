import { Elysia,t } from "elysia";
import { PrismaClient } from "@prisma/client";
const prisma = new PrismaClient();

async function get_descripcion(_correo: string){
  try{
  const usuario = await prisma.usuario.findMany({
    where: {
      direccion_correo: _correo,
    },
    select: {
      nombre: true,
      direccion_correo: true,
      descripcion: true
    }
  });
  return usuario;
  } catch (err) {
    return "Hubo un error"+err;
  }
}

async function get_usuario(_correo: string){
  try{
  const usuario = await prisma.usuario.findMany({
    where: {
      direccion_correo: _correo,
    },
    select: {
      direccion_correo: true,
      clave: true
    }
  });
  return usuario;
  } catch (err) {
    return "Hubo un error"+err;
  }
}

async function register_user(opciones: {_nombre: string, _correo: string, _clave: string, _descripcion: string}){
  try{
  const newUser = await prisma.usuario.create({
    data: {
      nombre: opciones._nombre,
      direccion_correo: opciones._correo,
      clave: opciones._clave,
      descripcion: opciones._descripcion
    },
  });
  return newUser;
  } catch(err){
    console.log("Hubo un error :");
  }
}

async function block_user(opciones: { _correo: string, _clave: string, _correo_bloquear: string }) {
  try {
    const usuario = await prisma.usuario.findMany({
      where: {
        direccion_correo: opciones._correo,
        clave: opciones._clave
      },
      select: {
        id: true
      }
    });

    const usuario_bloqueado = await prisma.usuario.findMany({
      where: {
        direccion_correo: opciones._correo_bloquear
      },
      select: {
        id: true
      }
    });
    const bloqueo = await prisma.usuario_bloqueado.create({
      data: {
        usuario: {
          connect: {
            id:usuario_bloqueado[0]?.id 
          }
        },
        bloqueo: {
          create: {
            id_usuario_bloqueador: usuario[0]?.id 
          }
        }
      }
    });

    return bloqueo;
  } catch (err) {
    console.log("Hubo un error :", err);
  }
}
async function set_favorite(opciones: { _correo: string, _clave: string, _id: number }) {
  try {
    const usuario = await prisma.usuario.findMany({
      where: {
        direccion_correo: opciones._correo,
        clave: opciones._clave
      }
    });

    const correo_fav = await prisma.correo_favorito.create({
      data: {
        usuario: {
          connect: {
            id: usuario[0]?.id
          }
        },
        correo: {
          connect: {
            id_correo: opciones._id
          }
        }
      },
    });

    return correo_fav;
  } catch (err) {
    console.log("Hubo un error :", err);
  }
}

async function delete_favorite(opciones: {_correo: string, _clave: string, _id: number}){
  try{
    const userID = await prisma.usuario.findMany({
      where: {
        direccion_correo: opciones._correo,
        clave: opciones._clave
      },
      select: {
        id: true
      }
    });
    console.log("estamos bien???")
    const eliminar_correo = await prisma.correo_favorito.delete({
      where: {
        id_usuario_id_correo_favorito: {
          id_usuario: userID[0]?.id,
          id_correo_favorito: opciones._id
        }
      }
    });
    return userID;
    } catch (err) {
      return "Hubo un error"+err;
    }
}


async function get_favorite(opciones: {_correo: string, _clave: string}){
  try{
    const userID = await prisma.usuario.findMany({
      where: {
        direccion_correo: opciones._correo,
        clave: opciones._clave
      },
      select: {
        id: true
      }
    });
    const correos = await prisma.correo_favorito.findMany({
      where: {
        id_usuario: userID[0]?.id
      }, 
      select: {
        id_correo_favorito: true
      }
    });
    return correos;
    } catch (err) {
      return "Hubo un error"+err;
    }
}

async function enviar_correo(opciones: {_correo: string, _clave: string, _asunto: string, _cuerpo: string, _correo_recibe: string}){
  try {
    const usuario = await prisma.usuario.findMany({
      where: {
        direccion_correo: opciones._correo,
        clave: opciones._clave
      },
      select: {
        id: true
      }
    });
    const usuario_receptor = await prisma.usuario.findMany({
      where: {
        direccion_correo: opciones._correo_recibe
      }, 
      select: {
        id: true
      }
    });
    const envio_correo = await prisma.correo_destinatario.create({
      data: {
        usuario: {
          connect: {
            id:usuario_receptor[0]?.id 
          }
        },
        correo: {
          create: {
            id_remitente: usuario[0]?.id, 
            asunto: opciones._asunto,
            cuerpo: opciones._cuerpo
          }
        }
      }
    });

    return envio_correo;
  } catch (err) {
    console.log("Hubo un error :", err);
  }
}

const app = new Elysia().get("/api/informacion/:correo", ({ params : { correo } }) => get_descripcion(correo))
                        .get("/api/get_usuario/:correo", ({ params : {correo}}) => get_usuario(correo))
                        .post("/api/registrar/", ({ body }) => register_user(body), {
                          body: t.Object({
                            _nombre: t.String(),
                            _correo: t.String(),
                            _clave: t.String(),
                            _descripcion: t.String()
                          }) 
                        })
                        .post("/api/bloquear/", ({ body }) => block_user(body), {
                          body: t.Object({
                            _correo: t.String(),
                            _clave: t.String(), 
                            _correo_bloquear: t.String()
                          })
                        })
                        .post("/api/marcarcorreo/", ({ body }) => set_favorite(body), {
                          body: t.Object({
                            _correo: t.String(),
                            _clave: t.String(),
                            _id: t.Number()
                          })
                        })
                        .post("/api/vercorreo/", ({ body }) => get_favorite(body),{
                          body: t.Object({
                            _correo: t.String(),
                            _clave: t.String()
                          })
                        })
                        .post("/api/enviarcorreo/", ({ body }) => enviar_correo(body), {
                          body: t.Object({
                            _correo: t.String(),
                            _clave: t.String(),
                            _asunto: t.String(),
                            _cuerpo: t.String(),
                            _correo_recibe: t.String()
                          })
                        })
                        .delete("/api/desmarcarcorreo/", ({ body }) => delete_favorite(body), {
                          body: t.Object({
                            _correo: t.String(),
                            _clave: t.String(),
                            _id: t.Number()
                          })
                        })
                        .listen(3000);
console.log(
  `🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`
);