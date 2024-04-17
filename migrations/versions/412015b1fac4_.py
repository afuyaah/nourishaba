"""empty message

Revision ID: 412015b1fac4
Revises: 
Create Date: 2024-04-14 06:42:20.563942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '412015b1fac4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_user')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=5000),
               existing_nullable=True)

    with op.batch_alter_table('user_delivery_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('full_name', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('phone_number', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('alt_phone_number', sa.String(length=20), nullable=True))
        batch_op.alter_column('address_line',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_delivery_info', schema=None) as batch_op:
        batch_op.alter_column('address_line',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.drop_column('alt_phone_number')
        batch_op.drop_column('phone_number')
        batch_op.drop_column('full_name')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)

    op.create_table('_alembic_tmp_user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=15), nullable=True),
    sa.Column('name', sa.VARCHAR(length=120), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=5000), nullable=True),
    sa.Column('registration_date', sa.DATETIME(), nullable=True),
    sa.Column('last_login_date', sa.DATETIME(), nullable=True),
    sa.Column('last_login_ip', sa.VARCHAR(length=15), nullable=True),
    sa.Column('role_id', sa.INTEGER(), nullable=True),
    sa.Column('confirmed', sa.BOOLEAN(), nullable=True),
    sa.Column('confirmation_token', sa.VARCHAR(length=64), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('confirmation_token')
    )
    # ### end Alembic commands ###