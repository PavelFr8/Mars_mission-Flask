from .db_session import SqlAlchemyBase
import sqlalchemy as sa
import sqlalchemy.orm as orm


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    chief = sa.Column(sa.Integer)
    members = sa.Column(sa.String, sa.ForeignKey('users.id'))
    email = sa.Column(sa.String)






