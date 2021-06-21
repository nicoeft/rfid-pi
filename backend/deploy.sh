#!/usr/bin/expect

spawn ssh pi@192.168.1.22
expect "password"
send "raspberry\r"
send "cd /home/workspace/rfid-pi/backend && git pull origin main && source venv/bin/activate && uvicorn app.main:app --host 0.0.0.0 --reload \r"
interact