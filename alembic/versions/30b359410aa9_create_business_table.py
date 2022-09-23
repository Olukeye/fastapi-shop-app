"""create business table

Revision ID: 30b359410aa9
Revises: d8e78188551c
Create Date: 2022-09-23 13:02:29.079837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30b359410aa9'
down_revision = 'd8e78188551c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('businesses',
        sa.Column('id', sa.BigInteger(), nullable=False),
            sa.Column('name', sa.String(), nullable=False),
               sa.Column('state', sa.String(), nullable=False),
                  sa.Column('city', sa.String(), nullable=False),
                     sa.Column('description', sa.String(),  nullable=False),
                        # sa.Column('url', sa.String(), nullable=False),
                           sa.Column('created_at', sa.String(), nullable=False),
                              sa.Column('updated_at', sa.String(), nullable=False),
                                 sa.Column('user_id', sa.BigInteger(), sa.ForeignKey('users.id')),
                                       sa.PrimaryKeyConstraint('id'),
                                          sa.UniqueConstraint('name')

        )
    pass


def downgrade():
    op.drop_table('businesses')
    pass