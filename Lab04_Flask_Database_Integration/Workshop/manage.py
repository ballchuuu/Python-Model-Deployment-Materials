from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

# if you are running this locally for development, please change host to "localhost"
# otherwise for production server, please change it to "0.0.0.0"
manager.add_command('runserver', Server(host='localhost'))

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
