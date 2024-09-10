from app.model import UserModel
from app.extensions import db
from sqlalchemy.exc import IntegrityError

class Auth:
    def user_register(name, email, password, pnumber):
        user = UserModel(name=name, email=email, pnumber=pnumber)
        user.set_password(password=password)

        try:
            db.session.add(user)
            db.session.commit()

            return user.email, 200
        
        except IntegrityError as e:
            return e, 400
        
    def login(email, pswd):
        user = UserModel.query.filter(UserModel.email==email).one()
        if user and user.check_password(pswd):
            return 'Success', 200
        
        return 'Error', 401


