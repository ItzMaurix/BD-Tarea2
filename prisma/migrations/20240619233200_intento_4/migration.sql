/*
  Warnings:

  - You are about to drop the `Administrador` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "Administrador" DROP CONSTRAINT "Administrador_id_usuario_fkey";

-- DropTable
DROP TABLE "Administrador";
