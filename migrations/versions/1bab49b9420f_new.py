"""new

Revision ID: 1bab49b9420f
Revises: d0a1b5442d0a
Create Date: 2020-09-29 17:10:15.096827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bab49b9420f'
down_revision = 'd0a1b5442d0a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'abc',sa.Column('movement_action_id', sa.Integer, primary_key=True),
        sa.Column('repetition', sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table('ac')
