# check_env.py

import os
from dotenv import load_dotenv
from pathlib import Path


# 🔥 cargar .env
load_dotenv()


def check_env_variables():
    print("\n🔐 Verificando variables de entorno...\n")

    required_vars = {
        "AWS_ACCESS_KEY_ID": os.getenv("AWS_ACCESS_KEY_ID"),
        "AWS_SECRET_ACCESS_KEY": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "AWS_DEFAULT_REGION": os.getenv("AWS_DEFAULT_REGION"),
        "MINIO_SERVER_URL": os.getenv("MINIO_SERVER_URL"),
        "MINIO_BROWSER_URL": os.getenv("MINIO_BROWSER_REDIRECT_URL"),
    }

    all_ok = True

    for key, value in required_vars.items():
        if value is None or value == "":
            print(f"❌ FALTA: {key}")
            all_ok = False
        else:
            print(f"✅ {key}: OK")

    return all_ok


def check_project_structure():
    print("\n📁 Verificando estructura del proyecto...\n")

    base_dir = Path(__file__).resolve().parent

    required_paths = [
        "data/raw",
        "data/processed",
        "models",
        "src",
    ]

    all_ok = True

    for path in required_paths:
        full_path = base_dir / path

        if full_path.exists():
            print(f"✅ {path}")
        else:
            print(f"❌ FALTA: {path}")
            all_ok = False

    return all_ok


def check_dvc():
    print("\n📦 Verificando DVC...\n")

    dvc_folder = Path(".dvc")

    if dvc_folder.exists():
        print("✅ DVC inicializado")
        return True
    else:
        print("❌ DVC NO inicializado")
        return False


def main():
    print("\n🚀 CHECK DE ENTORNO MLOps - HOTEL PROJECT\n")

    env_ok = check_env_variables()
    structure_ok = check_project_structure()
    dvc_ok = check_dvc()

    print("\n📊 RESUMEN FINAL")
    print("-------------------")

    if env_ok and structure_ok and dvc_ok:
        print("🎉 TODO OK - listo para entrenar o hacer deploy")
    else:
        print("⚠️ Hay problemas que debes corregir antes de continuar")


if __name__ == "__main__":
    main()