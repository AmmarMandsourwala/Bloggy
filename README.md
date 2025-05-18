
# FlaskBlog

A full-fledged blog application built using Flask. FlaskBlog is a comprehensive blog app developed using Flask, a micro web framework in Python. This README provides a step-by-step guide to setting up, configuring, and using FlaskBlog.

---

## 📌 Generating a Secret Key in `__init__.py`

1. Open your terminal.  
2. Start the Python interactive shell:
   ```bash
   $ python
   ```
3. Generate a secret key using the `secrets` module:
   ```python
   >>> import secrets
   >>> secrets.token_hex(16)
   ```
4. Copy the generated key and paste it into the `__init__.py` file:
   ```python
   app.config['SECRET_KEY'] = 'GENERATED_KEY'
   ```
5. Save the file and run the application.

---

## ⚙️ Setting Up and Using FlaskBlog with `flask_sqlalchemy`

1. Navigate to the FlaskBlog directory:
   ```bash
   $ cd FlaskBlog
   ```

2. Launch the Python interactive shell:
   ```bash
   $ python
   ```

3. Initialize the database and create tables:
   ```python
   >>> from FlaskBlog import db, app
   >>> from FlaskBlog.models import User, Post
   >>> with app.app_context():
   ...     db.create_all()
   ```

4. Create a new user:
   ```python
   >>> with app.app_context():
   ...     new_user = User(username='username', email='email', password='password')
   ...     db.session.add(new_user)
   ...     db.session.commit()
   ```

5. Retrieve all users to verify creation:
   ```python
   >>> with app.app_context():
   ...     all_users = User.query.all()
   ...     print(all_users)
   ```

6. Create a new post:
   ```python
   >>> with app.app_context():
   ...     new_post = Post(title='title', content='content', user_id=1)
   ...     db.session.add(new_post)
   ...     db.session.commit()
   ```

---

## 🔐 Encrypting and Verifying Passwords with Flask-Bcrypt

1. Start the Python shell:
   ```bash
   $ python
   ```

2. Import and use `flask_bcrypt`:
   ```python
   >>> from flask_bcrypt import Bcrypt
   >>> bcrypt = Bcrypt()
   >>> password = 'password'
   >>> hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
   >>> hashed_password
   >>> bcrypt.check_password_hash(hashed_password, password)
   ```

---

## 🕒 Generating Secure Time System Tokens

1. Launch Python:
   ```bash
   $ python
   ```

2. Import the required module:
   ```python
   >>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
   ```

3. Initialize the serializer:
   ```python
   >>> s = Serializer('secret', 30)
   ```

4. Generate a token:
   ```python
   >>> token = s.dumps({'user_id': 1}).decode('utf-8')
   >>> token
   ```

5. Verify the token (within 30 seconds):
   ```python
   >>> s.loads(token)
   {'user_id': 1}
   ```

---

## ✅ Summary

This guide covers:
- Flask app initialization with a secret key
- User and post creation with SQLAlchemy
- Password encryption using Flask-Bcrypt
- Secure token generation and verification using ItsDangerous

With these tools and steps, you can begin developing a full-featured Flask blog application.
