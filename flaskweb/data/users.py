from .db_session import SqlAlchemyBase
import sqlalchemy as sa
import sqlalchemy.orm as orm


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    age = sa.Column(sa.Integer)
    position = sa.Column(sa.String)
    speciality = sa.Column(sa.String)
    address = sa.Column(sa.String)
    hashed_password = sa.Column(sa.String)
    email = sa.Column(sa.String, unique=True)
    modified_date = sa.Column(sa.DateTime)

    users = orm.relationship('Jobs', back_populates='user')

    def __repr__(self) -> str:
        return f'<{self.id}> {self.name} {self.email}'







