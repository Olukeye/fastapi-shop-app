"""create category table

Revision ID: 38655e6540ea
Revises: 30b359410aa9
Create Date: 2022-09-23 13:04:59.878739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38655e6540ea'
down_revision = '30b359410aa9'
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
