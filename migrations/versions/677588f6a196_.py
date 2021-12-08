"""empty message

Revision ID: 677588f6a196
Revises: ed8da7e50eb7
Create Date: 2021-12-08 15:27:41.856173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '677588f6a196'
down_revision = 'ed8da7e50eb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###