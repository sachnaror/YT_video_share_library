# 📺 YT Video Share Library

A **FastAPI + PostgreSQL** backend that powers a YouTube-like video sharing platform.
This app demonstrates modern **async + sync ORM patterns**, modular APIs, and JWT-based authentication.

---

## 🚀 Features

- 👤 **Users**: Signup, login, JWT auth
- 🎥 **Videos**: CRUD operations, play page with view counts
- 👍👎 **Reactions**: Likes, dislikes, comments
- 🗄️ **Database**: PostgreSQL with `asyncpg` for async and SQLAlchemy ORM for sync
- 🔄 **Migrations**: Alembic-managed schema changes
- ⚡ **FastAPI**: Async-first Python web framework

---

## 📂 Project Structure

```
YT_video_share_library/
│── main.py                  # FastAPI entrypoint
│── users/                   # User-related APIs, models, db
│── videos/                  # Video-related APIs, models, db
│── reactions/               # Likes, dislikes, comments
│── alembic/                 # DB migrations
│── requirements.txt         # Dependencies

```

---

## 🛠️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/YT_video_share_library.git
cd YT_video_share_library
```

### 2️⃣ Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup PostgreSQL
```sql
CREATE DATABASE yt_video_db;
CREATE USER yt_user WITH PASSWORD 'yt_pass';
GRANT ALL PRIVILEGES ON DATABASE yt_video_db TO yt_user;
```

### 5️⃣ Run migrations
```bash
alembic upgrade head
```

### 6️⃣ Start the app
```bash
uvicorn main:app --reload
```

App will be available at 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔑 API Endpoints

- **Users**
  - `POST /users/signup` → Register a new user
  - `POST /users/login` → Login & get JWT
- **Videos**
  - `GET /videos/` → List all videos
  - `POST /videos/` → Upload new video
  - `GET /videos/{id}` → Get video details
  - `DELETE /videos/{id}` → Delete video
- **Reactions**
  - `POST /likes/` → Like a video
  - `POST /dislikes/` → Dislike a video
  - `POST /comments/` → Add comment

---

## 🧪 Testing

Run unit tests using pytest:
```bash
pytest
```

---

## 🤝 Contributing
PRs are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---


## Setup
```
source venv/bin/activate
pip install -r requirements.txt
source venv/bin/activate
uvicorn videos.main:app --reload --host 0.0.0.0 --port 8002
uvicorn reactions.main:app --reload --host 0.0.0.0 --port 8003
uvicorn users.main:app --reload --host 0.0.0.0 --port 8000
```

### Docs
- videos:http://127.0.0.1:8002/videos/docs
- users:http://127.0.0.1:8000/users/docs
- reactions:http://127.0.0.1:8003/reactions/docs

### Structure

```
├── YT_video_share_library/
│   ├── requirements.txt
│   ├── alembic.ini
│   ├── fix_imports.py
│   ├── README.md
│   ├── main.py
│   ├── reactions/
│   │   └── main.py
│   │   ├── api/
│   │   │   ├── db.py
│   │   │   ├── user.py
│   │   │   ├── models.py
│   │   │   └── videos.py
│   │   │   ├── routers/
│   │   │   │   ├── likes.py
│   │   │   │   ├── dislikes.py
│   │   │   │   └── comments.py
│   │   │   ├── db_manager/
│   │   │   │   ├── likes.py
│   │   │   │   ├── dislikes.py
│   │   │   │   └── comments.py
│   ├── videos/
│   │   ├── api/
│   │   │   ├── db_manager.py
│   │   │   ├── service.py
│   │   │   ├── db.py
│   │   │   ├── models.py
│   │   │   ├── utils.py
│   │   │   └── videos.py
│   ├── users/
│   │   ├── api/
│   │   │   ├── db_manager.py
│   │   │   ├── db.py
│   │   │   ├── models.py
│   │   │   ├── users.py
│   │   │   └── utils.py
│   ├── alembic/
│   │   ├── script.py.mako
│   │   ├── env.py
│   │   └── README
│   │   └── versions/


```

## 📩 Contact

| Name              | Details                             |
|-------------------|-------------------------------------|
| **👨‍💻 Developer**  | Sachin Arora                      |
| **📧 Email**      | [sachnaror@gmail.com](mailto:sacinaror@gmail.com) |
| **📍 Location**   | Noida, India                       |
| **📂 GitHub**     | [github.com/sachnaror](https://github.com/sachnaror) |
| **🌐 Youtube**    | [about.me/sachin-arora](https://www.youtube.com/@sachnaror4841/videos) |
| **🌐 Blog**       | [about.me/sachin-arora](https://medium.com/@schnaror) |
| **🌐 Website**    | [about.me/sachin-arora](https://about.me/sachin-arora) |
| **🌐 Twitter**    | [about.me/sachin-arora](https://twitter.com/sachinhep) |
| **📱 Phone**      | [+91 9560330483](tel:+919560330483) |
