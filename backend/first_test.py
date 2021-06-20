from app.db.session import SessionLocal
from app.models import User
from app.utils.users import handle_event

db =SessionLocal()
u1 = db.query(User).get(1)
u2 = db.query(User).get(2)
u3 = db.query(User).get(3)
u1.rfid_uuid = "78-222-116-43-207"
u2.rfid_uuid = "7-200-167-181-221"
u2.is_admin = True
u3.rfid_uuid = "55-13-225-181-110"
db.commit()

handle_event(u1.rfid_uuid,1)
handle_event(u2.rfid_uuid,1)
handle_event(u3.rfid_uuid,1)