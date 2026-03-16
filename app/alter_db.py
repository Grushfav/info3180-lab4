from app import create_app

app = create_app()
with app.app_context():
    app.db.engine.execute('ALTER TABLE user_profiles ALTER COLUMN password TYPE varchar(256);')
    print('Column altered')