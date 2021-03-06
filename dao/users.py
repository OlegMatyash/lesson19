from dao.model.users import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_new):
        ent = User(**user_new)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_upd):
        user = self.get_one(user_upd.get("id"))
        user.name = user_upd.get("name")
        user.password = user_upd.get("password")

        self.session.add(user)
        self.session.commit()
