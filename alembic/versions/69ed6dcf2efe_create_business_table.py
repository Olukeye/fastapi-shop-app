"""create_business_table

Revision ID: 69ed6dcf2efe
Revises: d29e03391316
Create Date: 2022-09-15 11:08:13.556838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69ed6dcf2efe'
down_revision = 'd29e03391316'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table('businesses',
        sa.Column('id', sa.BigInteger(), primary_key=True, nullable=False),
            sa.Column('name', sa.String(), nullable=False),
               sa.Column('state ', sa.String(), nullable=False),
                  sa.Column('city', sa.String(), nullable=False),
                     sa.Column('description', sa.Boolean(), server_default="False", nullable=False),
                        sa.Column('logo', sa.String(), nullable=False),
                           sa.Column('created_at', sa.String(), nullable=False),
                              sa.Column('updated_at', sa.String(), nullable=False),
                                 sa.Column('user_id', sa.BigInteger(), sa.ForeignKey('users.id'), primary_key=True),

        )
    pass


def downgrade():
    op.drop_table('businesses')
    pass