from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models import User, Provider, Transaction


def handle_event(rfid_uuid, provider_id) -> (str, bool):
    session: Session = SessionLocal()
    provider = session.query(Provider).get(provider_id)
    if not provider:
        error_msg = f"Provider:{provider_id} not found"
        return error_msg, False
    if provider.balance < provider.payment_amount:
        error_msg = f"Provider:{provider_id} has not enough funds"
        provider.is_active = False
        session.commit()
        return error_msg, False
    user = session.query(User).filter_by(rfid_uuid=rfid_uuid).first()
    if not user:
        error_msg = f"User doesn't exist"
        return error_msg, False
    print(f"User: {user.id}")
    if user.is_admin:
        print("ADMIN USER")
        provider.balance += provider.payment_amount
        msg = f"Deposited: {provider.payment_amount} - Total is:{provider.balance}"
        session.commit()
        return msg, True
    if user.balance >= provider.payment_amount:
        msg = do_transaction(provider, session, user)
        return msg, True
    error_msg = f"Insufficient balance: {user.balance} , minimum is {provider.payment_amount}"
    return error_msg, False


def do_transaction(provider, session, user):
    user.balance -= provider.payment_amount
    transaction = Transaction(user_id=user.id, provider_id=provider.id, amount=provider.payment_amount)
    session.add(transaction)
    session.commit()
    msg = f"Transaction {transaction.id} succesfull - Amount: {transaction.amount}"
    return msg
