from models import db, User
import pytest



@pytest.fixture()
def user():
    user = User(1231, "test_role", 0)
    db.session.add(user)
    db.session.commit()
    yield user
    db.session.delete(user)
    db.session.commit()

