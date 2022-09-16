"""create_products_table

Revision ID: 311d38c9892c
Revises: 011e18152980
Create Date: 2022-09-15 14:23:07.471594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '311d38c9892c'
down_revision = '011e18152980'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('products',
        sa.Column('id', sa.BigInteger(), nullable=False),
            sa.Column('name', sa.String(), nullable=False),
               sa.Column('state', sa.String(), nullable=False),
                  sa.Column('city', sa.String(), nullable=False),
                     sa.Column('slug', sa.String(), unique=True, nullable=False),
                        sa.Column('description', sa.String(), nullable=False),
                           sa.Column('price', sa.Integer(), nullable=False),
                              sa.Column('image', sa.String(), nullable=False),
                                 sa.Column('category_id', sa.BigInteger(), sa.ForeignKey('categories.id', ondelete='CASCADE')),
                                    sa.Column('created_at', sa.String(), server_default=sa.text('now()'), nullable=False),
                                       sa.Column('updated_at', sa.String(), server_default=sa.text('now()'), nullable=False),
                                           sa.PrimaryKeyConstraint('id'),
                                              sa.UniqueConstraint('name')
        )
    pass


def downgrade():
    op.drop_table('products')
    pass