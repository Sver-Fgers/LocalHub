# 🏘️ LocalHub – Community-Focused Web Application

## 📌 Project Overview

LocalHub is a community-focused web application built with **Django**
It serves as a hub for local communities, enabling users to:
- Share **news**
- Post upcoming **events**
- Network through **chats**
- and Connect through **volunteer** or **vigilante** initiatives

The project integrates **authentication, user access based control, CRUD operations, database design and django REST framework (optional) for API**.
---

## ✨ Functional Requirements

### 1. 👤 User Management (CRUD)
- Create, Read, Update, and Delete users.
- Required fields: `Username`, `Email`, `Password`.
- Optional fields: `Profile Picture`, `name`, `Bio`, `Location`.
- Only authenticated users can update or delete their own account.

### 2. 📰 Local News (CRUD)
- Users can create, read, update, and delete **news posts**.
- Each news post includes: `Title`, `Content`, `Author`, `Timestamp`, optional `Media`.
- Only the author can update/delete their posts.
- News feed displays most recent posts first.

### 3. 📅 Events (CRUD)
- Users can create, read, update, and delete **events**.
- Each event includes: `Title`, `Description`, `Date/Time`, `Location`, `Organizer (User)`.
- Optional: allow users to RSVP or express interest.

### 4. 💬 Chat (CRUD)
- Users can create new posts and update previous ones
- Each chat includes: `creator`, `Description`

---

## ⚙️ Technical Requirements

### 🗄. Database
- Django ORM models for:
    - `Users`, `NewsPosts`, `Events`, `Group chat`, `Memberships`.
- Relationships:
    - Each post/event linked to a user.
    - Each user has only one profile.
    
### 🔐 Authentication & Authorization
- Built on Django’s authentication system.
- Restrict sensitive actions (create/edit/delete) to authenticated users.
- Users may only edit/delete their own content.
- (Optional) **JWT Authentication** for API security.

---

## 🛠 Tech Stack
- Frontend: Django Templates, HTML, CSS, JavaScript
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL (for deployment), SQLite (for development)
- **Authentication**: Django Auth
- **Version Control**: Git & GitHub