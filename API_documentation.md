## Group Chat API Usage

**Base URL**  
http://127.0.0.1:8000/chat/api/

**Authentication**  
All endpoints require JWT authentication. Include the token in headers:  
`Authorization: Bearer <your_token>`

---

### User Authentication Endpoints
1. Register a User
`POST http://127.0.0.1:8000/chat/api/register/`

Description: register new user

Request Body:
```json
{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "strongpassword123"
}
```

2. Login User  
`POST http://127.0.0.1:8000/api/token/`  

Description: Logs in a user and returns a JWT token for authentication.  

Request Body (JSON):
```json
{
  "username": "testuser",
  "password": "strongpassword123"
}
```

Response (200 OK):

```json  
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```
Save the access token for subsequent requests.

### User Profile Endpoints

1. Get Current User Profile

GET http://127.0.0.1:8000/chat/api/profiles/<id>/

Description: Retrieve a user’s profile.

Response (200 OK):

```json
{
  "user_id": 2,
  "name": "null",
  "bio": "null",
  "birth_date": "null",
  "location": "null",
  "picture": null
}
```

2. Update Profile

PUT http://127.0.0.1:8000/chat/api/profiles/<id>/

Description: Update your profile (owner/admin only).

Request Body (JSON):

```json
{
  "name": "User Updated",
  "bio": "Updated bio",
  "location": "New City"
}
```

Response (200 OK):

```json
{
    "user_id": 2,
    "name": "User Updated",
    "bio": "Updated bio",
    "location": "New City"
  }
```

### Posts Endpoints

1. List/Create Posts

GET/POST http://127.0.0.1:8000/chat/api/posts/

Description: List all posts or create a new post (authenticated users only).

Create Post Request Body (JSON):

```json
{
  "body": "This is a new community post."
}
```

Response (POST 201 Created):

```json
{
  "id": 2,
  "author": "testuser",
  "body": "This is a new community post.",
  "created_on": "2025-09-06T16:45:00Z"
}
```

2. Retrieve/Update/Delete Specific Post

GET/PUT/PATCH/DELETE http://127.0.0.1:8000/chat/api/posts/<id>/

Description: Manage a specific post (owner/admin only).

Update Post Request Body (JSON):

```json
{
  "body": "Updated post content."
}
```

Response (PUT 200 OK):

```json
{
  "id": 2,
  "author": "testuser",
  "body": "Updated post content",
  "created_on": "2025-09-06T16:45:00Z"
}
```

### Comments Endpoints
1. List/Create Comments

GET/POST http://127.0.0.1:8000/chat/api/comments/

Description: List all comments or add a new comment to a post.

Create Comment Request Body (JSON):

```json
{
  "post": 12,
  "body": "Great post!"
}
```
Response (POST 201 Created):

```json
{  
  "id": 2,
  "post": 12,
  "author": "testuser",
  "body": "Great post!",
  "created_on": "2025-09-06T16:50:00Z"
}
```

2. Retrieve/Update/Delete Specific Comment

GET/PUT/PATCH/DELETE http://127.0.0.1:8000/chat/api/comments/<id>/

Description: Manage a specific comment (owner/admin only).

Update Comment Request Body (JSON):

```json
{
  "body": "Updated comment content."
}
```

Response (PUT 200 OK):

```json
{
  "id": 2,
  "post": 12,
  "author": "testuser",
  "body": "Updated comment content",
  "created_on": "2025-09-06T16:50:00Z"
}
```
