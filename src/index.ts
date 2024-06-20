import { Elysia,t } from "elysia";
import { PrismaClient } from "@prisma/client";
import { PrismaClientKnownRequestError } from "@prisma/client/runtime/library";

const prisma = new PrismaClient();

/*
Descripcion: Esta funcion se encarga de manejar los errores de

Parámetros:
string error: error realizado por la función

Return:
devuelve el mensaje utilizado.
*/ 
function handleError(error: unknown) {
  console.log(`[${new Date().toLocaleTimeString()}] Error: ${error instanceof Error ? error.message : 'Unknown error'}`);
  if (error instanceof PrismaClientKnownRequestError) {
    throw new Error('Error en la base de datos');
  }
  throw error;
}

/*
Descripcion: Funcion que regresa la informacion del usuario como lo es el
nombre, direccion de correo y su descrpcion

Parámetros:
string _correo: direccion de correo electronico del usuario a pedir informacion

Return:
Devuelve usuario con los atributos nombre, direccion de correo y descripcion
*/ 
async function get_descripcion(_correo: string) {
  try {
    const usuario = await prisma.usuario.findFirst({
      where: { direccion_correo: _correo },
      select: { nombre: true, direccion_correo: true, descripcion: true }
    });
    if (!usuario) throw new Error('Usuario no encontrado');
    return usuario;
  } catch (error) {
    handleError(error);
  }
}

/*
Descripcion: Esta función se encarga de corroborar si en la tabla usuario existe un usuario
que coincida con el correo indicado.

Parámetros:
string _correo: direccion de correo electronico del usuario a pedir informacion

Return:
Devuelve usuario con los atributos correo y clave.
*/ 
async function get_usuario(_correo: string) {
  try {
    const usuario = await prisma.usuario.findFirst({
      where: { direccion_correo: _correo },
      select: { direccion_correo: true, clave: true }
    });
    if (!usuario) throw new Error('Usuario no encontrado');
    return usuario;
  } catch (error) {
    handleError(error);
  }
}

/*
Descripcion: Esta función se encarga de registrar un usuario en la base de datos.

Parámetros:
string _nombre: nombre del usuario a crear.
string _correo: direccion de correo electronico del usuario a crear.
string _clave: clave del usuario a crear.
string _descripción: descripción del usuario a crear.

Return:
Devuelve la información del usuario creado.
*/ 
async function register_user(opciones: {_nombre: string, _correo: string, _clave: string, _descripcion: string}) {
  try {
    const newUser = await prisma.usuario.create({
      data: {
        nombre: opciones._nombre,
        direccion_correo: opciones._correo,
        clave: opciones._clave,
        descripcion: opciones._descripcion
      },
    });
    return newUser;
  } catch (error) {
    handleError(error);
  }
}

/*
Descripcion: Funcion que se encarga bloquear un usuario en la base de datos

Parámetros:
string _correo: direccion de correo electronico del usuario
string _clave: clave del usuario
string _correo_bloquear: direccion de correo electronico al que se desea bloquear

Return:
Devuelve el bloqueo generado por el usuario y se genera una ID a la tabla.
*/
async function block_user(opciones: { _correo: string, _clave: string, _correo_bloquear: string }) {
  try {
    const usuario = await prisma.usuario.findFirst({
      where: { direccion_correo: opciones._correo, clave: opciones._clave },
      select: { id: true }
    });
    if (!usuario) throw new Error('Usuario no encontrado o credenciales incorrectas');

    const usuario_bloqueado = await prisma.usuario.findFirst({
      where: { direccion_correo: opciones._correo_bloquear },
      select: { id: true }
    });
    if (!usuario_bloqueado) throw new Error('Usuario a bloquear no encontrado');

    const bloqueo = await prisma.usuario_bloqueado.create({
      data: {
        usuario: { connect: { id: usuario_bloqueado.id } },
        bloqueo: { create: { id_usuario_bloqueador: usuario.id } }
      }
    });
    return bloqueo;
  } catch (error) {
    handleError(error);
  }
}

/*
Descripcion: Esta función se encarga de marcar un correo como favorito dependiendo del id.

Parámetros:
string _correo: direccion de correo electronico del usuario a crear.
string _clave: clave del usuario a crear.
string _id: id del correo a marcar.

Return:
Devuelve la información de la relación creada entre el correo y usuario.
*/
 
async function set_favorite(opciones: { _correo: string, _clave: string, _id: number }) {
  try {
    const usuario = await prisma.usuario.findFirst({
      where: { direccion_correo: opciones._correo, clave: opciones._clave },
      select: { id: true }
    });
    if (!usuario) throw new Error('Usuario no encontrado o credenciales incorrectas');

    const correo_fav = await prisma.correo_favorito.create({
      data: {
        usuario: { connect: { id: usuario.id } },
        correo: { connect: { id_correo: opciones._id } }
      },
    });
    return correo_fav;
  } catch (error) {
    handleError(error);
  }
}

/*
Descripcion: Esta función se encarga de desmarcar un correo como favorito dependiendo del id.

Parámetros:
string _correo: direccion de correo electronico del usuario a crear.
string _clave: clave del usuario a crear.
string _id: id del correo a marcar.

Return:
Devuelve la información de la relación eliminada entre el correo y usuario.
*/
 
async function delete_favorite(opciones: {_correo: string, _clave: string, _id: number}) {
  try {
    const usuario = await prisma.usuario.findFirst({
      where: { direccion_correo: opciones._correo, clave: opciones._clave },
      select: { id: true }
    });
    if (!usuario) throw new Error('Usuario no encontrado o credenciales incorrectas');

    const eliminar_correo = await prisma.correo_favorito.delete({
      where: {
        id_usuario_id_correo_favorito: {
          id_usuario: usuario.id,
          id_correo_favorito: opciones._id
        }
      }
    });
    return eliminar_correo;
  } catch (error) {
    handleError(error);
  }
}

/*
Descripcion: Esta función se encarga de obtener los correos favoritos dependiendo del usuario.

Parámetros:
string _correo: direccion de correo electronico del usuario a crear.
string _clave: clave del usuario a crear.

Return:
Devuelve la información de correos favoritos del usuario.
*/
 
async function get_favorite(opciones: {_correo: string, _clave: string}) {
  try {
    const usuario = await prisma.usuario.findFirst({
      where: { direccion_correo: opciones._correo, clave: opciones._clave },
      select: { id: true }
    });
    if (!usuario) throw new Error('Usuario no encontrado o credenciales incorrectas');
    const correos = await prisma.correo_favorito.findMany({
      where: { id_usuario: usuario.id },
      select: { id_correo_favorito: true }
    });
    return correos;
  } catch (error) {
    handleError(error);
  }
}

/*
Descripcion: Esta función crea un nuevo correo enviado por una persona en cuestión

Parámetros:
string _correo: direccion de correo electronico del usuario que envía el correo.
string _clave: clave del usuario que envía el correo.
string _asunto: asunto del correo enviado.
string _cuerpo: cuerpo del correo enviado.
string _correo_recibe: dirección de correo electrónido del usuario que recibe el correo.

Return:
Devuelve la informacion de envio correo, donde se genera una relacion con el remitente del correo con el destinatario.
*/

async function enviar_correo(opciones: {_correo: string, _clave: string, _asunto: string, _cuerpo: string, _correo_recibe: string}) {
  try {
    const usuario = await prisma.usuario.findFirst({
      where: { direccion_correo: opciones._correo, clave: opciones._clave },
      select: { id: true }
    });
    if (!usuario) throw new Error('Usuario no encontrado o credenciales incorrectas');

    const usuario_destinatario = await prisma.usuario.findFirst({
      where: { direccion_correo: opciones._correo_recibe },
      select: { id: true }
    });
    if (!usuario_destinatario) throw new Error('Usuario destinatario no encontrado');

    const correo = await prisma.correo.create({
      data: {
        remitente: { connect: { id: usuario.id } },
        asunto: opciones._asunto,
        cuerpo: opciones._cuerpo,
      }
    });

    const correo_destinatario = await prisma.correo_destinatario.create({
      data: {
        usuario: { connect: { id: usuario_destinatario.id } },
        correo: { connect: { id_correo: correo.id_correo } }
      }
    });

    console.log(`[${new Date().toLocaleTimeString()}] Correo enviado correctamente de ${opciones._correo} a ${opciones._correo_recibe}`);
    return correo_destinatario;
  } catch (error) {
    handleError(error);
  }
}

const app = new Elysia().get("/api/informacion/:correo", async ({ params: { correo }, set }) => {
                          try {
                            console.log(`[${new Date().toLocaleTimeString()}] Solicitud de información para: ${correo}`);
                            const resultado = await get_descripcion(correo);
                            return resultado;
                          } catch (error) {
                            set.status = error instanceof PrismaClientKnownRequestError ? 500 : 400;
                            return { error: error instanceof Error ? error.message : 'Error desconocido' };
                          }
                        })
                        .get("/api/get_usuario/:correo", async ({ params: { correo }, set }) => {
                          try {
                            console.log(`[${new Date().toLocaleTimeString()}] Solicitud de usuario para: ${correo}`);
                            const resultado = await get_usuario(correo);
                            return resultado;
                          } catch (error) {
                            set.status = error instanceof PrismaClientKnownRequestError ? 500 : 400;
                            return { error: error instanceof Error ? error.message : 'Error desconocido' };
                          }
                        })
                        .post("/api/registrar/", async ({ body, set }) => {
                          try {
                            console.log(`[${new Date().toLocaleTimeString()}] Solicitud de registro para: ${body._correo}`);
                            const resultado = await register_user(body);
                            return resultado;
                          } catch (error) {
                            set.status = error instanceof PrismaClientKnownRequestError ? 500 : 400;
                            return { error: error instanceof Error ? error.message : 'Error desconocido' };
                          }
                        }, {
                          body: t.Object({
                            _nombre: t.String(),
                            _correo: t.String(),
                            _clave: t.String(),
                            _descripcion: t.String()
                          })
                        })
                        .post("/api/bloquear/", async ({ body, set }) => {
                          try {
                            console.log(`[${new Date().toLocaleTimeString()}] Solicitud de bloqueo de ${body._correo} a ${body._correo_bloquear}`);
                            const resultado = await block_user(body);
                            return resultado;
                          } catch (error) {
                            set.status = error instanceof PrismaClientKnownRequestError ? 500 : 400;
                            return { error: error instanceof Error ? error.message : 'Error desconocido' };
                          }
                        }, {
                          body: t.Object({
                            _correo: t.String(),
                            _clave: t.String(),
                            _correo_bloquear: t.String()
                          })
                        })
                        .post("/api/marcarcorreo/", async ({ body, set }) => {
                          try {
                            console.log(`[${new Date().toLocaleTimeString()}] Solicitud para marcar correo como favorito de ${body._correo}`);
                            const resultado = await set_favorite(body);
                            return resultado;
                          } catch (error) {
                            set.status = error instanceof PrismaClientKnownRequestError ? 500 : 400;
                            return { error: error instanceof Error ? error.message : 'Error desconocido' };
                          }
                        }, {
                          body: t.Object({
                            _correo: t.String(),
                            _clave: t.String(),
                            _id: t.Number()
                          })
                        })
                        .post("/api/vercorreo/", async ({ body, set }) => {
                          try {
                            console.log(`[${new Date().toLocaleTimeString()}] Solicitud para ver correos favoritos de ${body._correo}`);
                            const resultado = await get_favorite(body);
                            return resultado;
                          } catch (error) {
                            set.status = error instanceof PrismaClientKnownRequestError ? 500 : 400;
                            return { error: error instanceof Error ? error.message : 'Error desconocido' };
                          }
                        }, {
                          body: t.Object({
                            _correo: t.String(),
                            _clave: t.String()
                          })
                        })
                        .post("/api/enviarcorreo/", async ({ body, set }) => {
                          try {
                            console.log(`[${new Date().toLocaleTimeString()}] Solicitud para enviar correo de ${body._correo} a ${body._correo_recibe}`);
                            const resultado = await enviar_correo(body);
                            return resultado;
                          } catch (error) {
                            set.status = error instanceof PrismaClientKnownRequestError ? 500 : 400;
                            return { error: error instanceof Error ? error.message : 'Error desconocido' };
                          }
                        }, {
                          body: t.Object({
                            _correo: t.String(),
                            _clave: t.String(),
                            _asunto: t.String(),
                            _cuerpo: t.String(),
                            _correo_recibe: t.String()
                          })
                        })
                        .delete("/api/desmarcarcorreo/", async ({ body, set }) => {
                          try {
                            console.log(`[${new Date().toLocaleTimeString()}] Solicitud para desmarcar correo favorito de ${body._correo}`);
                            const resultado = await delete_favorite(body);
                            return resultado;
                          } catch (error) {
                            set.status = error instanceof PrismaClientKnownRequestError ? 500 : 400;
                            return { error: error instanceof Error ? error.message : 'Error desconocido' };
                          }
                        }, {
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