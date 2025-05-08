# Ensemble File Analysis Tools

A web-based tool to analyze various file types (videos, documents, images, etc.) for security and integrity. It includes a FastAPI backend, a React (Vite) frontend, and supports file analysis using Kali Linux-based command-line logic.

---

## 🧰 Technologies Used

- **Frontend**: React (Vite + TailwindCSS)
- **Backend**: FastAPI (Python 3.13+)
- **Logic Layer**: Kali Linux CLI tools and Python libraries

---

## 🚀 How to Run

### 1. Backend (FastAPI)

```bash
cd fastapi-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

The FastAPI server will be available at:  
➡️ `http://127.0.0.1:8000`

---

### 2. Frontend (React + Vite)

```bash
cd react-frontend
npm install
npm run dev
```

The Vite development server will be running at:  
➡️ `http://localhost:5173`

---

## 📝 How to Use

1. **Homepage**: Open the app in your browser and click on the **"Try It Now"** button.
2. **Input Page**: Upload your file(s) and click **"Analyze"**.
3. **Output Page**: You'll be redirected to a results page showing the complete file analysis output in a readable format.

---

## 📂 Supported Files

- XLSX
- DOCX
- PDF
- EXE
- JPG
- MP4
- MP3

---

## 💡 Notes

- Ensure you're running on **Kali Linux** or a similar system where analysis logic commands are supported.
- Python version: **3.13+** is required.
