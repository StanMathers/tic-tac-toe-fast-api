"""added status

Revision ID: 79055ecd2ebc
Revises: 4d84a83ae5b0
Create Date: 2022-11-12 11:19:15.645077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79055ecd2ebc'
down_revision = '4d84a83ae5b0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('status')
    # ### end Alembic commands ###