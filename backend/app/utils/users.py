from app.core.config import AMOUNT_USER_PAYMENT, AMOUNT_ADMIN_DEPOSIT
from app.db.session import SessionLocal
from app.models.provider import Provider
from app.models.user import User
from sqlalchemy.orm import Session


def handle_user(user_id, provider_id)->(str, bool):
    session: Session = SessionLocal()
    provider = session.query(Provider).get(provider_id)
    if not provider:
        error_msg=f"Provider:{provider_id} not found"
        return error_msg, False
    if provider.balance < provider.payment_amount:
        error_msg = f"Provider:{provider_id} has not enough funds"
        provider.is_active = False
        session.commit()
        return error_msg, False
    user = session.query(User).get(user_id)
    if not user:
        error_msg= f"User:{user_id} not found"
        return error_msg, False
    if user.is_admin:
        provider.balance += provider.payment_amount
        msg = f"Deposited: {provider.payment_amount} - Total is:{provider.balance}"
        return msg,True
    if user.balance >= provider.payment_amount:
        original_balance = user.balance
        user.balance -= provider.payment_amount
        msg= f"Original balance:{original_balance} - Current balance:{user.balance}"
        session.commit()
        return msg, True
    error_msg= f"Insufficient balance: {user.balance} , minimum is {provider.payment_amount}"
    return error_msg, False