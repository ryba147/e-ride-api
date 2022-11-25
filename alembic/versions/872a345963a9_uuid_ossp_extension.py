"""uuid-ossp extension

Revision ID: 872a345963a9
Revises: 
Create Date: 2022-11-26 00:46:51.752635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '872a345963a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')  # for uuid_generate_v4


def downgrade() -> None:
    op.execute('DROP EXTENSION IF EXISTS "uuid-ossp";')
