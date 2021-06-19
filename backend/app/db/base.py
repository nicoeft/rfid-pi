# Import all the models, so that Base has them before being
# imported by Alembic
from api.app.db.base_class import Base  # noqa
from api.app.models.user import User  # noqa