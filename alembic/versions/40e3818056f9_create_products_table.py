"""create products table

Revision ID: 40e3818056f9
Revises: 38655e6540ea
Create Date: 2022-09-23 13:06:18.189385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40e3818056f9'
down_revision = '38655e6540ea'
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
                              # sa.Column('image', sa.String(), nullable=False),
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