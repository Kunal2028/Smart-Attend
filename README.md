# 🎓 SmartAttend

**An AI-powered classroom attendance system using face recognition.**
Take one photo of the class, and SmartAttend detects every face, identifies enrolled students, marks attendance, stores the records, and emails each student their status.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![InsightFace](https://img.shields.io/badge/Face%20Recognition-InsightFace%20(ArcFace)-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)

---

## 📌 Table of Contents

- [Features](#-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Tips for Better Accuracy](#-tips-for-better-accuracy)
- [Privacy & Ethics](#-privacy--ethics)
- [Group Members](#-group-members)

---

## ✨ Features

| Module | Description |
|---|---|
| 📷 **Take Attendance** | Upload or capture a classroom photo. All faces are detected and matched against enrolled students, with an annotated image showing names and confidence. |
| 👤 **Enroll Students** | Register students with one or more face photos. Embeddings are averaged (with flip augmentation) for a robust profile. |
| 📋 **Attendance Records** | Browse saved attendance sessions and individual student records. |
| 📊 **Reports** | View attendance statistics and summaries. |
| 📧 **Email Notifications** | Styled HTML present/absent emails with date, subject, class, recognition confidence and overall attendance percentage. |

**Highlights**

- Works on **crowded classroom photos**: multi-scale tiled detection catches small and distant faces.
- **Low-light and blur handling**: CLAHE contrast equalisation plus mild sharpening before detection.
- **Fast matching**: all faces are matched against all students with a single vectorised matrix multiplication.
- **Smart alerts**: warns students whose attendance drops below 75% and congratulates those above 85%.
- **Runs fully on CPU**: no GPU required.
- Everything is configurable through a `.env` file.

---

## 🧠 How It Works

```
Classroom photo
      │
      ▼
1. Preprocess ──► CLAHE lighting fix + unsharp mask
      │
      ▼
2. Detect ──────► RetinaFace (InsightFace buffalo_l)
      │            • adaptive det_size (up to 1280 px)
      │            • horizontal / vertical tiling for wide or tall images
      │            • Non-Max Suppression (IoU 0.45) to merge duplicates
      ▼
3. Align ───────► 5-point landmarks → 112×112 ArcFace canonical face
      │
      ▼
4. Embed ───────► 512-dim L2-normalised ArcFace embedding
      │
      ▼
5. Match ───────► Cosine distance vs. enrolled students (threshold 0.40)
      │
      ▼
6. Output ──────► Annotated image + present list + unknown count
                   → saved to database → emails sent
```

**Enrollment strategy:** each student's embedding is the normalised average of the embeddings of all their photos plus horizontally flipped copies. Embeddings are stored as `.npy` files in `data/embeddings/`.

**Detection thresholds**

| Mode | Minimum detection score |
|---|---|
| Classroom (many small / partial faces) | `max(0.30, FACE_MIN_SCORE − 0.20)` → **0.50** by default |
| Enrollment (single clear face) | `max(0.60, FACE_MIN_SCORE)` → **0.70** by default |

---

## 🛠️ Tech Stack

| Purpose | Technology |
|---|---|
| Web UI | [Streamlit](https://streamlit.io/) |
| Face detection & recognition | [InsightFace](https://github.com/deepinsight/insightface) (RetinaFace + ArcFace, `buffalo_l` model pack) |
| Inference runtime | ONNX Runtime (CPU) |
| Image processing | OpenCV (headless), Pillow, NumPy, SciPy |
| Database | SQLite via SQLAlchemy |
| Data analysis | Pandas |
| Email | SMTP (`smtplib`) with HTML templates |
| Configuration | python-dotenv |

---

## 📁 Project Structure

```
Smart-Attend/
├── app.py              # Streamlit entry point: sidebar navigation & page routing
├── config.py           # Paths, thresholds, school and SMTP settings (reads .env)
├── database.py         # Database models and initialisation
├── face_engine.py      # Face detection, alignment, embedding, matching pipeline
├── email_service.py    # SMTP sender and HTML email templates
├── requirements.txt    # Python dependencies
├── pages/
│   ├── capture.py      # 📷 Take Attendance
│   ├── enroll.py       # 👤 Enroll Students
│   ├── records.py      # 📋 Attendance Records
│   └── reports.py      # 📊 Reports
└── data/               # Auto-created on first run
    ├── embeddings/     # Student face embeddings (.npy)
    ├── faces/          # Cropped faces saved per session
    ├── uploads/        # Uploaded images
    └── smartattend.db  # SQLite database
```

---

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- `pip`
- Internet connection on first run (the `buffalo_l` model pack, about 300 MB, is downloaded once and cached locally)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Kunal2028/Smart-Attend.git
cd Smart-Attend

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create your .env file (see Configuration below)

# 5. Run the app
streamlit run app.py
```

Open **http://localhost:8501** in your browser.

> ⚠️ **Windows users:** `insightface` may need the *Microsoft C++ Build Tools* installed to compile successfully.

---

## ⚙️ Configuration

Create a `.env` file in the project root. All values are optional and fall back to defaults.

```env
# School / class
SCHOOL_NAME=Your School or College Name
DEFAULT_CLASS=CS-301

# Face recognition tuning
FACE_MATCH_THRESHOLD=0.40   # cosine distance; lower = stricter
FACE_MIN_SCORE=0.70         # detection confidence

# Email (SMTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
EMAIL_FROM=your_email@gmail.com
EMAIL_FROM_NAME=SmartAttend System
```

| Variable | Default | Description |
|---|---|---|
| `SCHOOL_NAME` | `Your School` | Shown in email headers and footers |
| `DEFAULT_CLASS` | `CS-301` | Default class name |
| `FACE_MATCH_THRESHOLD` | `0.40` | Maximum cosine distance to accept a match. Lower = fewer false matches, higher = fewer missed students |
| `FACE_MIN_SCORE` | `0.70` | Base detection confidence (classroom and enrollment thresholds are derived from it) |
| `SMTP_HOST` / `SMTP_PORT` | `smtp.gmail.com` / `587` | Mail server (uses STARTTLS) |
| `SMTP_USER` / `SMTP_PASSWORD` | empty | Mail credentials. If empty, emails are skipped without errors |
| `EMAIL_FROM` / `EMAIL_FROM_NAME` | empty / `SmartAttend System` | Sender address and display name |

> 💡 For Gmail, create an [App Password](https://support.google.com/accounts/answer/185833) (2-Step Verification required) and use it as `SMTP_PASSWORD`.
> 🔐 Never commit your `.env` file. Add it to `.gitignore`.

To switch to a faster, lighter model, change `FACE_MODEL` in `config.py` from `buffalo_l` (best accuracy) to `buffalo_s`.

---

## 📖 Usage

1. **Enroll students**: go to **👤 Enroll Students**, add the student's details and upload 1 or more clear face photos. More photos from different angles give better recognition.
2. **Take attendance**: go to **📷 Take Attendance**, choose the class, and upload or capture a classroom photo. Review the annotated result (green box = recognised, blue box = unknown).
3. **Save and notify**: confirm the attendance, then send present/absent emails to students.
4. **Review**: use **📋 Attendance Records** and **📊 Reports** to view history and statistics.

---

## 🎯 Tips for Better Accuracy

- Enroll each student with **3 to 5 clear, front-facing photos** with different lighting.
- Take the classroom photo from the **front of the room**, at eye level, with good lighting.
- Use a **high-resolution** image so distant faces have enough pixels.
- If real students are shown as *Unknown*, slightly **raise** `FACE_MATCH_THRESHOLD` (e.g. 0.45). If wrong students are being matched, **lower** it (e.g. 0.35).
- If faces are being missed, lower `FACE_MIN_SCORE`.

---

## 🔒 Privacy & Ethics

SmartAttend processes and stores biometric data (face embeddings and cropped face images). Before using it with real students:

- Obtain **consent** from students (or guardians for minors).
- Follow your institution's and local **data protection regulations**.
- Keep the `data/` folder secure and **never commit it** to a public repository.

---

## 👥 Group Members

| # | Name | Registration No. | Responsibility |
|---|------|------------------|----------------|
| 1 | Krishna Agarwal | 20243144 | Face-recognition engine, configuration, accuracy evaluation |
| 2 | Kunal Upadhyay | 20243148 | Data layer, attendance workflow, e-mail service |
| 3 | Krishna Goyal | 20243525 | Streamlit UI, project documents |


---

⭐ If you find this project useful, consider giving it a star!
