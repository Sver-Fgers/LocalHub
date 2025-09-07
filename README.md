# 🏘️ LocalHub – Community-Focused Web Application

## 📌 Overview

LocalHub is a Django-powered platform connecting members of local communities. Users can share news, organize events, chat in groups, and manage personal profiles. It emphasizes secure authentication, user-driven content, and a modern, responsive interface.  

---

## 🚀 Features

### 👤 User Management
- Register, login, and manage user accounts via frontend forms or API.  
- Edit profile details: name, bio, location, birth date, profile picture.  
- Secure authentication via Django and django-allauth, and JWT-based authentication for API access.  
- Only authenticated users can edit/delete their own profiles.

### 💬 Group Chat
- Users can post messages and comment on posts.  
- Edit or delete their own posts and comments.  
- Admins can manage only their own posts/comments.  
- Profiles link to each user’s chat activity.  

#### **API endpoints:**  
  
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/chat/api/posts/` | GET, POST | List all posts / create a post |
| `/chat/api/posts/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a specific post |
| `/chat/api/comments/` | GET, POST | List all comments / create a comment |
| `/chat/api/comments/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a specific comment |
| `/chat/api/profiles/` | GET, POST | List all profiles / create profile (admin only) |
| `/chat/api/profiles/<id>/` | GET, PUT, PATCH, DELETE | Manage individual profiles (owner/admin only) |

### 📰 News Feed (work-in-progress)
- Create, read, update, and delete news posts.
- Each post includes title, content, author, timestamp, and optional media.
- News feed displays the latest posts first.
- Only authors can modify or delete their own posts.

### 📅 Events (work-in-progress)
- Organize and manage community events.
- Events include title, description, date/time, location, and organizer.

### 🛡️ Volunteer & Vigilante Initiatives (work-in-progress)
- Sections for volunteering and reporting local issues.  

---

## 🖥️ UI & Templates

- Responsive layout using Bootstrap and custom CSS.  
- Modular templates: landing page, navigation, chat, and user profiles.  
- Accessible via desktop and mobile browsers.  

---

## ⚙️ Technical Details

- **Backend:** Django, Django REST Framework  
- **Frontend:** Django Templates, HTML, CSS, JavaScript  
- **Database:** SQLite (development)  
- **Authentication:** JWT via SimpleJWT, Django Auth  
- **Version Control:** Git & GitHub  

## App Structure

- `localhub/` – project settings, URLs, core views  
- `users/` – user and profile models, authentication  
- `group_chat/` – posts, comments, profile templates, API endpoints  
- `news/` – news posts (work-in-progress)  
- `events/` – community events (work-in-progress)  
- `landing/` – landing page, base templates  
- `communities/` – community management (work-in-progress)  

---

## 📦 Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/localhub.git
   cd localhub
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   Or use the provided Pipfile with pipenv.

3. Apply migrations:
   ```sh
   python manage.py migrate
   ```

4. Run the development server:
   ```sh
      python manage.py runserver
   ```

5. Access the app:
Open http://localhost:8000 in your browser.

## 🎯 Usage

### Frontend Flow
- Register or login.  

- Navigate to chat to create posts or comment.

- Edit or delete your own posts/comments.

- Edit your own profile.


### API Flow
- see 👉️ group chat [API documentation](API_documentation.md) for full breakdown


## 🤝 Contributing
- Fork the repository

- Create a feature branch (git checkout -b feature/feature-branch)

- Commit your changes (git commit -m 'Add features")

- Push to the branch (git push origin feature/feature-branch)

- Open a Pull Request

❗️Important Notice
This project is for educational and demonstration purposes.

I have only implemented minimal features to satisfy the requirement for ALX backend software engineering program.

I plan to complete the other features, polish the UI and integrate Django best practices for building applications, when I have the time.