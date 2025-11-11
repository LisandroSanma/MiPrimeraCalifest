import os
import shutil
import subprocess

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
# Carpeta donde están tus archivos originales
origen = r"C:\Users\pc\Downloads\CaliFest\PrimeraCaliFest"

# Carpeta que se va a crear para subir a GitHub
destino = r"C:\Users\pc\Downloads\CaliFest"

# URL de tu repositorio GitHub (crealo vacío antes)
repo_url = "https://github.com/LisandroSanma/MiPrimeraCalifest"

# Nombre de la branch para GitHub Pages
branch = "main"
# -----------------------------

# Crear la carpeta de destino si no existe
if not os.path.exists(destino):
    os.makedirs(destino)

# Copiar todos los archivos desde la carpeta original
for item in os.listdir(origen):
    s = os.path.join(origen, item)
    d = os.path.join(destino, item)
    if os.path.isdir(s):
        shutil.copytree(s, d, dirs_exist_ok=True)
    else:
        shutil.copy2(s, d)

print("📂 Archivos copiados correctamente a:", destino)

# Entrar a la carpeta de destino
os.chdir(destino)

# Inicializar repositorio Git
subprocess.run(["git", "init"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Subida inicial de la invitación Califest"])
subprocess.run(["git", "branch", "-M", branch])

# Conectar al repositorio remoto
subprocess.run(["git", "remote", "add", "origin", repo_url])

# Subir todo al repositorio
subprocess.run(["git", "push", "-u", "origin", branch])

print("✅ Invitación subida a GitHub correctamente.")
print(f"🔗 GitHub Pages: https://{repo_url.split('/')[-2]}.github.io/{repo_url.split('/')[-1].replace('.git','')}/")
