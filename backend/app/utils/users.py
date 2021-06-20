from app.core.config import AMOUNT_USER_PAYMENT, AMOUNT_ADMIN_DEPOSIT
from app.db.session import SessionLocal
from app.models.user import User
from sqlalchemy.orm import Session


def handle_user(user_id):
    session: Session = SessionLocal()
    user = session.query(User).get(user_id)
    if user:
        if user.is_admin:
            deposit()
        else:
            print(f"User:{user.username}")
            if user.balance >= AMOUNT_USER_PAYMENT:
                print(f"Previous balance:{user.balance}")
                user.balance -= AMOUNT_USER_PAYMENT
                print(f"Current balance:{user.balance}")
                session.commit()
            else:
                print(f"Insufficient balance: {user.balance} and minimum is {AMOUNT_USER_PAYMENT}")
    else:
        print(f"User:{user_id} not found")
    session.close()


def deposit():
    print(f"Deposited: {AMOUNT_ADMIN_DEPOSIT}")