# 🏘️ LocalHub – Community-Focused Web Application

## 📌 Project Overview

LocalHub is a community-focused web application built with **Django** and **Django REST Framework (DRF)**.  
It serves as a hub for local communities, enabling users to:
- Share **news**
- Post upcoming **events**
- Create and join **groups**
- Connect through volunteer or vigilante initiatives

The project integrates **authentication, location-based access control, CRUD operations, database design, and RESTful APIs**. It manages user-generated content, relationships between users and communities, and filtering by location.

---

## ✨ Functional Requirements

### 1. 👤 User Management (CRUD)
- Create, Read, Update, and Delete users.
- Required fields: `Username`, `Email`, `Password`, `Location`.
- Optional fields: `Profile Picture`, `Bio`, `Contact Information`.
- Only authenticated users can update or delete their own account.

### 2. 🏠 Community Membership & Authentication
- Users must register with a **location** (city/town/neighborhood).
- Authentication ensures only community members access content for their location.
- Users cannot access posts or events from other communities.

### 3. 📰 Local News (CRUD)
- Users can create, read, update, and delete **news posts**.
- Each news post includes: `Title`, `Content`, `Author`, `Timestamp`, optional `Media`.
- Only the author can update/delete their posts.
- News feed displays most recent posts first.

### 4. 📅 Events (CRUD)
- Users can create, read, update, and delete **events**.
- Each event includes: `Title`, `Description`, `Date/Time`, `Location`, `Organizer (User)`.
- Optional: allow users to RSVP or express interest.

### 5. 👥 Groups (CRUD)
- Users can create and join groups (e.g., book club, gardening, vigilante).
- Each group includes: `Name`, `Description`, `Creator`, `Members`.
- Group creators can moderate membership and group content.

### 6. 📰📅 Community Feed
- Combined feed of **news + events** relevant to the user’s community.
- Posts ordered in **reverse chronological order** (latest first).
- Optional filters: by type (`news/events`), date, or keyword.

---

## ⚙️ Technical Requirements

### 🗄. Database
- Django ORM models for:
    - `Users`, `Communities`, `NewsPosts`, `Events`, `Groups`, `Memberships`.
- Relationships:
    - Each post/event linked to a user.
    - Each user belongs to exactly one community.
    - Groups track members and posts separately.

### 🔐 Authentication & Authorization
- Built on Django’s authentication system.
- Restrict sensitive actions (create/edit/delete) to authenticated users.
- Users may only edit/delete their own content.
- **Location-based access control** ensures exclusivity.
- (Optional) **JWT Authentication** for API security.

### 🌐 API Design
- REST API built with **Django REST Framework (DRF)**.
- Endpoints for:
    - Users
    - News posts
    - Events
    - Groups
    - Community feed
- RESTful principles (`GET`, `POST`, `PUT`, `DELETE`).
- Error handling with meaningful status codes (400, 401, 403, 404, 500).

### 🚀 Deployment
- Deploy on **Heroku** or **PythonAnywhere**.
- Ensure endpoints are **secure & publicly accessible**.
- Use **environment variables** for secrets (API keys, DB credentials).

### 📊 Pagination & Sorting
- Pagination for feeds with many posts/events.
- Sorting options: by **date, popularity, or relevance**.

---

## 🛠 Tech Stack
- Frontend: Django Templates (MVP), React (future)
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL (for deployment), SQLite (for development)
- **Authentication**: Django Auth
- **Deployment**: Heroku / PythonAnywhere
- **Version Control**: Git & GitHub

---
## 🚦 Project Status

- ✅ Planning & ERD completed
- ✅ Models & Database schema designed
- 🔄 In progress: API endpoint implementation

---

## 📌 Next Steps

- Build CRUD endpoints for Users, News, Events, and Groups
- Implement authentication & location-based access control.
- Add filtering & pagination for community feeds.
- Deploy to Heroku/PythonAnywhere.
