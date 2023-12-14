# installation

Clone the repository
Navigate to the project directory
Install Python dependencies using pip
  pip install -r requirements.txt
Apply database migrations
  python manage.py migrate
Start the Django development server
  python manage.py runserver

#API ENDPOINTS
The API includes the following endpoints:

    POST /signup: User registration endpoint.
    POST /login: User login endpoint to get authentication tokens.
    POST /create_post: Endpoint to create a new post.
    POST /like_post: Endpoint to like a post.
    POST /comment_post: Endpoint to comment on a post.
    POST /follow: Endpoint to follow a user.
    GET /following: Endpoint to retrieve users a user is following.
    GET /followers: Endpoint to retrieve a user's followers.
    GET /posts: Endpoint to retrieve a user's posts.
    GET /all_posts: Endpoint to retrieve all posts.
    GET /view_post/{id}: Endpoint to view a specific post.
    POST /edit_post/{id}: Endpoint to edit a post.
    DELETE /delete_post/{id}: Endpoint to delete a post.
    POST /unfollow: Endpoint to unfollow a user.
    POST /like_post/{post_id}: Endpoint to like a specific post.
    POST /unlike_post/{post_id}: Endpoint to unlike a specific post.
    POST /logout: Endpoint to log out a user by invalidating tokens.

#serializers
 ContentSerializer
- Maps the Post model for content.
 UserSerializer
- Serializes the User model, including username, email, and password.
 UserListSerializer
- Serializes the User model to retrieve user IDs, usernames, and emails.
 PostSerializer
- Maps the Post model.
 PostListSerializer
- Includes user information using the UserListSerializer within the Post model.
 LikeSerializer
- Serializes the Like model.
CommentSerializer
- Serializes the Comment model.
 FollowSerializer
- Serializes the Follow model.
 FollowListSerializer
- Includes user and followed user information using the UserListSerializer within the Follow model.
PostLikesSerializer
- Includes user information using the UserListSerializer within the Like model.

## Usage
These serializers define the structure for representing Django model instances in a format suitable for API responses. They are utilized across various API endpoints to serialize and deserialize data, ensuring seamless communication between the Django backend and any client applications.

## Models Overview
 Post Model
- `user`: ForeignKey to the User model, representing the user who created the post.
- `title`: CharField storing the title of the post.
- `content`: TextField for the post content.
- `created_at`: DateTimeField recording the creation timestamp.
- `updated_at`: DateTimeField tracking the last update timestamp.

 Like Model
- `user`: ForeignKey to the User model, indicating the user who liked the post.
- `post`: ForeignKey to the Post model, linking the like to a specific post.
- `created_at`: DateTimeField capturing the like creation time.
- **Note**: The unique_together constraint ensures that a user can like a post only once.

Comment Model
- `user`: ForeignKey to the User model, specifying the user who commented.
- `post`: ForeignKey to the Post model, associating the comment with a post.
- `content`: TextField holding the comment content.
- `created_at`: DateTimeField marking the comment creation time.

Follow Model
- `user`: ForeignKey to the User model, representing the follower.
- `followed_user`: ForeignKey to the User model, identifying the user being followed.
- `created_at`: DateTimeField indicating when the follow relationship was created.

## Usage
These models define the core data structures and relationships necessary for creating a social media platform. They can be utilized in Django views, serializers, and other parts of the application to handle posts, likes, comments, and follow relationships.

## __pycache__ Directory

The __pycache__ directory is automatically created by Python to store compiled bytecode files (.pyc) generated during the execution of Python modules. This directory improves the performance of subsequent imports by caching the compiled bytecode, reducing the need for recompilation.
Purpose

    Bytecode Caching: Python compiles modules into bytecode for execution. The __pycache__ directory stores these compiled bytecode files for reuse when the corresponding source file is imported again.
    Improved Performance: Storing bytecode in the __pycache__ directory speeds up the import process, especially for larger projects or modules with complex dependencies.

Usage

    Automatic Generation: Python automatically generates the __pycache__ directory when a module is imported for the first time.
    Version Specific: Each __pycache__ subdirectory corresponds to the Python version used. Different versions of Python will create separate __pycache__ directories.
    Can be Ignored: The __pycache__ directory can be safely ignored and excluded from version control systems (e.g., Git). It's created and managed by Python itself.