"""empty message

Revision ID: 4b46df09118e
Revises: 91a86c2f31bd
Create Date: 2025-06-21 14:12:43.625457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b46df09118e'
down_revision = '91a86c2f31bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('poems', schema=None) as batch_op:
        batch_op.add_column(sa.Column('brief_summary', sa.Text(), nullable=False))
        batch_op.drop_column('category')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('poems', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
        batch_op.drop_column('brief_summary')

    # ### end Alembic commands ###
