Abner Vidal ROL: 202273032-3
Natalia Antileo ROL: 202173070-2
Mauricio Ramos ROL: 202273041-2

Enlace al repositorio GitHub: https://github.com/ItzMaurix/BD-Tarea2

Intrucciones para la correcta ejecución de la api:
1. Importante tener instalado bun y python3.
2. Una vez descargada la tarea y se encuentre dentro de la carpeta BD-Tarea2, debe realizar
 los siguientes comandos(Windows):
- cd..
- bun create elysia BD-Tarea2
- cd BD-Tarea2
- bun add -d prisma
- bunx prisma init
- bunx prisma generate
- bunx prisma migrate dev
- bun run --watch src/index.ts
3. Una vez realizados estos comandos, ejecute el comando pip install -r requirements.txt
4. Finalmente para acceder a la interfaz, simplemente realice el comando python3 cli.py