"""Add person tabe

Revision ID: 848a0a9c1ca6
Revises: 
Create Date: 2020-09-27 13:57:37.021421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '848a0a9c1ca6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('account',
                    sa.Column('id', sa.INTEGER, primary_key=True),
                    sa.Column('timestamp', sa.TIMESTAMP, server_default=sa.func.now())
                    )


def downgrade():
    op.drop_table('account')
