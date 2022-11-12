"""test

Revision ID: 31340fcac8ac
Revises: e7e99a3a290a
Create Date: 2022-11-12 11:28:06.185976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31340fcac8ac'
down_revision = 'e7e99a3a290a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('winner_player_id', sa.Integer(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['status.id'], ),
    sa.ForeignKeyConstraint(['winner_player_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_status')
    # ### end Alembic commands ###
