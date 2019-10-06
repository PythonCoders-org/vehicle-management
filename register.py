from app import db
from app.models import Users
from datetime import date
from werkzeug.security import generate_password_hash

#Admin User
u = Users(username = 'admin', email = 'admin@example.com', userid = '1', date = date.today(), user_role = 'admin', password = generate_password_hash('admin'))

db.session.add(u)
db.session.commit()