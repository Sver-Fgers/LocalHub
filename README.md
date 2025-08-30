# 🏘️ LocalHub – Community-Focused Web Application

## 📌 Overview

LocalHub is a Django-powered platform designed to connect members of local communities. It enables users to share news, organize events, chat in groups, and manage personal profiles. The app emphasizes secure authentication, user-driven content, and a modern, responsive interface.

---

## 🚀 Features

### 👤 User Management
- Register, login, and manage user accounts.
- Edit profile details: username, email, profile picture, bio, location, birth date.
- Secure authentication via Django and django-allauth.
- Only users can edit/delete their own profiles.

### 📰 News Feed (in-progress)
- Create, read, update, and delete news posts.
- Each post includes title, content, author, timestamp, and optional media.
- News feed displays the latest posts first.
- Only authors can modify or delete their own posts.

### 📅 Events (in-progress)
- Organize and manage community events.
- Events include title, description, date/time, location, and organizer.
- (Optional) RSVP or express interest in events.

### 💬 Group Chat 
- Post messages and comments in group chats.
- Edit or delete your own posts and comments.
- User profiles link to their chat activity.

### 🛡️ Volunteer & Vigilante Initiatives (in-progress)
- Sections for community volunteering and reporting issues

---

## 🖥️ UI & Templates

- Responsive design using Bootstrap and custom CSS
- Modular templates for landing page, navigation, sidebar, news, events, chat, and user profiles.
- Accessible via desktop and mobile browsers.

---

## ⚙️ Technical Details

- **Backend:** Django, Django REST Framework
- **Frontend:** Django Templates, HTML, CSS, JavaScript
- **Database:** SQLite (development)
- **Authentication:** Django Auth, django-allauth (social login)
- **Version Control:** Git & GitHub

### App Structure

- [`localhub`](localhub/) – Project settings, URLs, core views.
- [`users`](users/) – User and profile models, authentication logic.
- [`news`](news/) – News post models and views.
- [`events`](events/) – Event models and views.
- [`group_chat`](group_chat/) – Group chat, posts, comments, and profile templates.
- [`landing`](landing/) – Landing page, navigation, and base templates.
- [`communities`](communities/) – Community management (optional/extendable).

---

## 🏁 Getting Started

1. **Clone the repository:**
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


#### 🧩 Extending LocalHub
I plan to complete the other apps for more community features.
Integrate REST APIs for mobile or third-party access.
Customize templates for branding and UX.