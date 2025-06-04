# 📝 simple To-Do List

A minimalist and professional-looking **To-Do List web application** built using **Python (Flask)**, **HTML**, **CSS**, and **SQLite**, featuring a **custom 12-hour time input form (no JavaScript)**, task status toggle, and a responsive dark UI.

---

## 🚀 Features

- ✅ Add tasks with:
  - Task title
  - Due date
  - Custom 12-hour time selection (AM/PM)
- 🌓 Clean **Dark Theme** with modern UI
- ✔️ Mark tasks as completed / incomplete
- 🗑️ Delete tasks
- 📅 Sorts tasks by due date
- 💻 Responsive layout (mobile-friendly)
- 🧠 Built using only:
  - Flask (Python)
  - HTML & CSS
  - SQLite for storage
  - No JavaScript used

---

## 📸 Preview

![screenshot](https://github.com/user-attachments/assets/5d89cb8c-67c3-4539-b152-198162fc6a0f)
 <!-- Add screenshot.png in repo if available -->

---

## 🛠️ Tech Stack

| Tech         | Purpose                          |
|--------------|----------------------------------|
| Python       | Backend server logic             |
| Flask        | Web framework (routes, templates)|
| SQLite       | Local database for tasks         |
| HTML + CSS   | Frontend layout and styling      |

---

## 📂 Project Structure
```bash
todo_web/
│
├── app.py # Main Flask backend
├── todo.db # SQLite database
├── templates/
│ └── index.html # UI layout
├── static/
│ └── style.css # Styling (Dark theme)
└── README.md # This file
```
---
## 🧪 How to Run Locally
1. Install dependencies:
```bash
pip install flask flask_sqlalchemy
```

2. Run the app:
```bash
python app.py
```
3. Open in browser:
http://127.0.0.1:5000/

---

## 📌 Note 
Uses `<select>` for 12-hour time (no JS) to keep UI clean and lightweight.

## 🚧 Future Enhancements

- User authentication to allow multiple users with private task lists  
- Task categories/tags for better organization  
- Reminder notifications (email or push notifications)  
- Task priority levels and filtering options  



