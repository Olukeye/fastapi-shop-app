"""create_category_table

Revision ID: 011e18152980
Revises: 69ed6dcf2efe
Create Date: 2022-09-15 14:01:33.726476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '011e18152980'
down_revision = '69ed6dcf2efe'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table('categories',
        sa.Column('id', sa.BigInteger(),nullable=False),
            sa.Column('name', sa.String(), nullable=False),
               sa.Column('slug', sa.String(),nullable=False),
                  sa.Column('business_id', sa.BigInteger(), sa.ForeignKey('businesses.id')),
                     sa.Column('created_at', sa.String(), server_default=sa.text('now()'), nullable=False),
                        sa.Column('updated_at', sa.String(), server_default=sa.text('now()'), nullable=False),
                           sa.PrimaryKeyConstraint('id'),
                               sa.UniqueConstraint('name'),
                                  sa.UniqueConstraint('slug')
        )
    pass


def downgrade():
    op.drop_table('categories')
    pass
