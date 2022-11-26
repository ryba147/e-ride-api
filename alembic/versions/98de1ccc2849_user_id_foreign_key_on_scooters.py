"""user_id foreign key on scooters

Revision ID: 98de1ccc2849
Revises: 68f69d7efcf8
Create Date: 2022-11-26 01:44:49.121363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98de1ccc2849'
down_revision = '68f69d7efcf8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('scooters_user_id_fkey', 'scooters', type_='foreignkey')
    op.create_foreign_key(None, 'scooters', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'scooters', type_='foreignkey')
    op.create_foreign_key('scooters_user_id_fkey', 'scooters', 'roles', ['user_id'], ['id'])
    # ### end Alembic commands ###
