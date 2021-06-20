from app.utils.users import handle_user, deposit

USER_WITH_BALANCE = 1
USER_WITHOUT_BALANCE = 2
USER_NOT_FOUND = 555

handle_user(USER_WITH_BALANCE)
handle_user(USER_WITHOUT_BALANCE)
handle_user(USER_NOT_FOUND)
deposit()
