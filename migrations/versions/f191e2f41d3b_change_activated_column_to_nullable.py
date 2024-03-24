"""Change activated column to nullable

Revision ID: f191e2f41d3b
Revises: 5fbe3abd44ff
Create Date: 2024-03-24 13:36:00.146336

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f191e2f41d3b'
down_revision = '5fbe3abd44ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_accounts', schema=None) as batch_op:
        batch_op.alter_column('activated',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_accounts', schema=None) as batch_op:
        batch_op.alter_column('activated',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)

    # ### end Alembic commands ###