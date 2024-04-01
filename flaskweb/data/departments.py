from .db_session import SqlAlchemyBase
import sqlalchemy as sa
import sqlalchemy.orm as orm


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    chief = sa.Column(sa.Integer, sa.ForeignKey('users.id'))  # Внешний ключ для связи с таблицей пользователей
    members = sa.Column(sa.String)
    email = sa.Column(sa.String)

    user = orm.relationship('User', back_populates='departments')

    def __repr__(self):
        return f"<Department(id={self.id}, title={self.title})>"