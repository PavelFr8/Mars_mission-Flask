from .db_session import SqlAlchemyBase
import sqlalchemy as sa
import sqlalchemy.orm as orm
from werkzeug.security import generate_password_hash, check_password_hash


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    chief = sa.Column(sa.Integer)
    members = sa.Column(sa.String)
    email = sa.Column(sa.String)

    user = orm.relationship('User')






