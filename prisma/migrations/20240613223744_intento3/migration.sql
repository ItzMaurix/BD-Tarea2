-- AlterTable
ALTER TABLE "Usuario" ALTER COLUMN "fecha_creacion" SET DEFAULT CURRENT_TIMESTAMP;

-- CreateTable
CREATE TABLE "Correo" (
    "id_correo" SERIAL NOT NULL,
    "id_remitente" INTEGER NOT NULL,
    "asunto" TEXT,
    "cuerpo" TEXT,
    "fecha_envio" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Correo_pkey" PRIMARY KEY ("id_correo")
);

-- CreateTable
CREATE TABLE "Administrador" (
    "id_admin" SERIAL NOT NULL,
    "id_usuario" INTEGER NOT NULL,

    CONSTRAINT "Administrador_pkey" PRIMARY KEY ("id_admin")
);

-- CreateTable
CREATE TABLE "Correo_destinatario" (
    "id_destinatario" INTEGER NOT NULL,
    "id_correo_dest" INTEGER NOT NULL,

    CONSTRAINT "Correo_destinatario_pkey" PRIMARY KEY ("id_correo_dest","id_destinatario")
);

-- CreateTable
CREATE TABLE "Correo_favorito" (
    "id_usuario" INTEGER NOT NULL,
    "id_correo_favorito" INTEGER NOT NULL,
    "fecha_agregado" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Correo_favorito_pkey" PRIMARY KEY ("id_usuario","id_correo_favorito")
);

-- CreateTable
CREATE TABLE "Usuario_bloqueado" (
    "id_usuario" INTEGER NOT NULL,
    "id_bloqueo" INTEGER NOT NULL,

    CONSTRAINT "Usuario_bloqueado_pkey" PRIMARY KEY ("id_bloqueo","id_usuario")
);

-- CreateTable
CREATE TABLE "Bloqueo" (
    "id_bloqueo" SERIAL NOT NULL,
    "id_usuario_bloqueador" INTEGER NOT NULL,
    "fecha_bloqueo" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Bloqueo_pkey" PRIMARY KEY ("id_bloqueo")
);

-- CreateIndex
CREATE UNIQUE INDEX "Correo_id_remitente_key" ON "Correo"("id_remitente");

-- CreateIndex
CREATE UNIQUE INDEX "Administrador_id_usuario_key" ON "Administrador"("id_usuario");

-- AddForeignKey
ALTER TABLE "Correo" ADD CONSTRAINT "Correo_id_remitente_fkey" FOREIGN KEY ("id_remitente") REFERENCES "Usuario"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Administrador" ADD CONSTRAINT "Administrador_id_usuario_fkey" FOREIGN KEY ("id_usuario") REFERENCES "Usuario"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Correo_destinatario" ADD CONSTRAINT "Correo_destinatario_id_destinatario_fkey" FOREIGN KEY ("id_destinatario") REFERENCES "Usuario"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Correo_destinatario" ADD CONSTRAINT "Correo_destinatario_id_correo_dest_fkey" FOREIGN KEY ("id_correo_dest") REFERENCES "Correo"("id_correo") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Correo_favorito" ADD CONSTRAINT "Correo_favorito_id_usuario_fkey" FOREIGN KEY ("id_usuario") REFERENCES "Usuario"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Correo_favorito" ADD CONSTRAINT "Correo_favorito_id_correo_favorito_fkey" FOREIGN KEY ("id_correo_favorito") REFERENCES "Correo"("id_correo") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Usuario_bloqueado" ADD CONSTRAINT "Usuario_bloqueado_id_usuario_fkey" FOREIGN KEY ("id_usuario") REFERENCES "Usuario"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Usuario_bloqueado" ADD CONSTRAINT "Usuario_bloqueado_id_bloqueo_fkey" FOREIGN KEY ("id_bloqueo") REFERENCES "Bloqueo"("id_bloqueo") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Bloqueo" ADD CONSTRAINT "Bloqueo_id_usuario_bloqueador_fkey" FOREIGN KEY ("id_usuario_bloqueador") REFERENCES "Usuario"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
