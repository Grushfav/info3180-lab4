from app import app, db
from sqlalchemy import text

with app.app_context():
    with db.engine.connect() as conn:
        conn.execute(text('ALTER TABLE user_profiles ALTER COLUMN password TYPE varchar(256);'))
        conn.commit()
    print('Column altered')