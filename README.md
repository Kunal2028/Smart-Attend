# 🎓 SmartAttend

**A face-recognition based attendance system built with Streamlit.**

SmartAttend lets teachers take attendance from a camera photo, automatically identifies enrolled students, stores records in a database, generates reports, and emails students their present/absent status.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red)
![InsightFace](https://img.shields.io/badge/Face%20Recognition-InsightFace-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## ✨ Features

- 📷 **Take Attendance**: capture a class photo and automatically recognise enrolled students
- 👤 **Enroll Students**: register students with their face data and details
- 📋 **Attendance Records**: browse and review past attendance sessions
- 📊 **Reports**: view attendance statistics and summaries
- 📧 **Email Notifications**: send styled HTML present/absent emails to students, including recognition confidence and overall attendance percentage
- ⚠️ **Low-attendance alerts**: students are warned when their attendance drops below 75%
- 🗄️ **Persistent storage**: records are stored using SQLAlchemy

---

## 🛠️ Tech Stack

| Purpose | Technology |
|---|---|
| UI / Web app | [Streamlit](https://streamlit.io/) |
| Face recognition | [InsightFace](https://github.com/deepinsight/insightface) + ONNX Runtime |
| Image processing | OpenCV (headless), Pillow, NumPy, SciPy |
| Database | SQLAlchemy |
| Data handling | Pandas |
| Email | SMTP (`smtplib`) with Jinja2 / HTML templates |
| Config | python-dotenv |

---

## 📁 Project Structure

```
Smart-Attend/
├── app.py              # Main Streamlit app (sidebar navigation + page routing)
├── database.py         # Database models and initialisation
├── email_service.py    # SMTP email sending and HTML templates
├── requirements.txt    # Python dependencies
└── pages/
    ├── capture.py      # Take Attendance page
    ├── enroll.py       # Enroll Students page
    ├── records.py      # Attendance Records page
    └── reports.py      # Reports page
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Kunal2028/Smart-Attend.git
cd Smart-Attend
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root for email notifications:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
EMAIL_FROM=your_email@gmail.com
EMAIL_FROM_NAME=SmartAttend
SCHOOL_NAME=Your School / College Name
```

> 💡 For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your normal password.
> If SMTP credentials are not set, the app skips sending emails and continues to work normally.

### 5. Run the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## 📖 How to Use

1. **Enroll Students**: open *Enroll Students* and add each student's details along with their face photo.
2. **Take Attendance**: open *Take Attendance*, capture or upload a class photo, and let the system recognise students.
3. **Review**: check *Attendance Records* to verify and view saved sessions.
4. **Analyse**: use *Reports* to see attendance trends.
5. **Notify**: send present/absent emails to students after a session.

---

## 📧 Email Notifications

Each email includes:

- Date, subject and class
- Present / absent status (green header for present, red for absent)
- Face-recognition confidence (for present students)
- Overall attendance percentage
- A warning if attendance is below 75%, or an encouragement message at 85% and above

---

## 🔒 Privacy Note

SmartAttend stores facial data for enrolled students. Make sure you have consent from students (or guardians) and follow your institution's data protection policies. Never commit your `.env` file or database to GitHub.

---

## 🗺️ Roadmap

- [ ] Admin login / authentication
- [ ] Export reports to CSV / PDF
- [ ] Live webcam / video stream recognition
- [ ] Multi-class and multi-teacher support
- [ ] Docker support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m "Add amazing feature"`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. Add a `LICENSE` file to the repository to make it official.

---

## 👥 Group Members

| # | Name | Registration No. | Responsibility |
|---|------|------------------|----------------|
| 1 | Krishna Agarwal | 20243144 | Face-recognition engine, configuration, accuracy evaluation |
| 2 | Kunal Upadhyay | 20243148 | Data layer, attendance workflow, e-mail service |
| 3 | Krishna Goyal | 20243525 | Streamlit UI, project documents |

Repository maintained by [@Kunal2028](https://github.com/Kunal2028).

⭐ If you find this project useful, consider giving it a star!
