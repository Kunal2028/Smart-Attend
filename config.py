import os

from dotenv import load_dotenv

load_dotenv()

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

EMBEDDINGS_DIR = os.path.join(DATA_DIR, "embeddings")
UPLOADS_DIR = os.path.join(DATA_DIR, "uploads")
FACES_DIR = os.path.join(DATA_DIR, "faces")
DB_PATH = os.path.join(DATA_DIR, "smartattend.db")

# Ensure required data directories exist
DATA_DIRECTORIES = [
    DATA_DIR,
    EMBEDDINGS_DIR,
    UPLOADS_DIR,
    FACES_DIR,
]

for directory in DATA_DIRECTORIES:
    os.makedirs(directory, exist_ok=True)


# School configuration
SCHOOL_NAME = os.getenv("SCHOOL_NAME", "Your School")
DEFAULT_CLASS = os.getenv("DEFAULT_CLASS", "CS-301")


# Face recognition configuration
FACE_MODEL = "buffalo_l"  # buffalo_l = best accuracy; buffalo_s = faster
MATCH_THRESHOLD = float(
    os.getenv("FACE_MATCH_THRESHOLD", "0.40")
)  # cosine distance
MIN_SCORE = float(
    os.getenv("FACE_MIN_SCORE", "0.70")
)  # detection confidence


# Email configuration
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
EMAIL_FROM = os.getenv("EMAIL_FROM", "")
EMAIL_FROM_NAME = os.getenv("EMAIL_FROM_NAME", "SmartAttend System")
