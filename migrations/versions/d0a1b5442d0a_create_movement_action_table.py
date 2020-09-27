"""new

Revision ID: d0a1b5442d0a
Revises: d35842a8d058
Create Date: 2020-09-27 15:22:03.784426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0a1b5442d0a'
down_revision = 'd35842a8d058'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "movement_action",
        sa.Column('movement_action_id', sa.Integer, primary_key=True),
        sa.Column('repetition', sa.Integer, nullable=False),
        sa.Column('weight', sa.Integer, nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('movement_id', sa.Integer(), nullable=False),
        # sa.ForeignKeyConstraint(('movement_id',), ['movement.movement_id'], ),
    )
    op.create_foreign_key(
        'fk_movement_action',
        'movement_action', 'movement',
        ['movement_id'], ['movement_id'],
    )


def downgrade():
    op.drop_constraint('fk_movement_action', 'movement-action', type_='foreignkey')
    op.drop_table('movement_action')
