"""Adding category column in the pitches table

Revision ID: 38f0d9dad316
Revises: 1e22c95e079c
Create Date: 2018-05-19 22:22:15.922082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38f0d9dad316'
down_revision = '1e22c95e079c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'category')
    # ### end Alembic commands ###
