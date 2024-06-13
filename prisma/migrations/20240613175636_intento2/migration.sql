/*
  Warnings:

  - You are about to drop the column `email` on the `Usuario` table. All the data in the column will be lost.
  - You are about to drop the column `name` on the `Usuario` table. All the data in the column will be lost.
  - A unique constraint covering the columns `[direccion_correo]` on the table `Usuario` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `direccion_correo` to the `Usuario` table without a default value. This is not possible if the table is not empty.
  - Added the required column `fecha_creacion` to the `Usuario` table without a default value. This is not possible if the table is not empty.

*/
-- DropIndex
DROP INDEX "Usuario_email_key";

-- AlterTable
ALTER TABLE "Usuario" DROP COLUMN "email",
DROP COLUMN "name",
ADD COLUMN     "clave" TEXT,
ADD COLUMN     "descripcion" TEXT,
ADD COLUMN     "direccion_correo" TEXT NOT NULL,
ADD COLUMN     "fecha_creacion" TIMESTAMP(3) NOT NULL,
ADD COLUMN     "nombre" TEXT;

-- CreateIndex
CREATE UNIQUE INDEX "Usuario_direccion_correo_key" ON "Usuario"("direccion_correo");
