from pathlib import Path

from environs import Env

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / '.env'

env = Env()
env.read_env(path=ENV_FILE, override=True)
