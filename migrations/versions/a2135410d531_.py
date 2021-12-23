"""empty message

Revision ID: a2135410d531
Revises: 843f47c1ea06
Create Date: 2021-12-23 14:22:51.573708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2135410d531'
down_revision = '843f47c1ea06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'genres')
    # ### end Alembic commands ###
