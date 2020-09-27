"""new table creation

Revision ID: d35842a8d058
Revises: 
Create Date: 2020-09-27 15:08:51.524107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd35842a8d058'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('account')
