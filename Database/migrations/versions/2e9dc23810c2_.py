"""empty message

Revision ID: 2e9dc23810c2
Revises: 
Create Date: 2019-03-23 02:16:03.562190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e9dc23810c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Garbage_Can',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('one_full', sa.Float(), nullable=False),
    sa.Column('two_full', sa.Float(), nullable=False),
    sa.Column('three_full', sa.Float(), nullable=False),
    sa.Column('four_full', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('waste',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_type', sa.String(length=250), nullable=True),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('garbage_can_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['garbage_can_id'], ['Garbage_Can.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('waste')
    op.drop_table('Garbage_Can')
    # ### end Alembic commands ###