from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Blog
from flask_migrate import Migrate, MigrateCommand


# Creating app instance
app = create_app('development')

# Create manager instance
manager = Manager(app)

# Migrate instance


manager.add_command('server', Server)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)


if __name__ == '__main__':
    manager.run()
    
    