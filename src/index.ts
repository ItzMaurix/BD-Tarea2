import { Elysia } from "elysia";
import { PrismaClient } from "@prisma/client";
const prisma = new PrismaClient();
async function obtener_usuario(msg){
  const usuario = await prisma.usuario.findMany({
    where: {
      direccion_correo: msg,
    },
  });
  if (usuario.length == 0){
    return 0
  }
  return 1
}
const app = new Elysia().get("/existe-usuario/:msg", ({ params : { msg } }) => obtener_usuario(msg)).listen(3000);
/*
const newUser = await prisma.usuario.create({
  data: {
    nombre: 'Juanito',
    direccion_correo: 'juanito668@juan.com',
    clave: '1234',
    descripcion: 'me gusta el amongus potion'
  },
});*/
//console.log('Usuario creado:', newUser);
console.log(
  `🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`
);
