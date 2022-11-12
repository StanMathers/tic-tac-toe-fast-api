"""Created positions

Revision ID: 0694f1dd111a
Revises: 6d64b1471abb
Create Date: 2022-11-12 14:51:11.428382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0694f1dd111a'
down_revision = '6d64b1471abb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('positions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('playerer_id', sa.Integer(), nullable=True),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.ForeignKeyConstraint(['playerer_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('positions')
    # ### end Alembic commands ###
