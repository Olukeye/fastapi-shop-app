"""create users table

Revision ID: d29e03391316
Revises: 
Create Date: 2022-09-14 18:50:51.234445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd29e03391316'
down_revision = None
branch_labels = None
depends_on = None



def upgrade():
    op.create_table('users',
        sa.Column('id', sa.BigInteger(), primary_key=True, nullable=False),
            sa.Column('username', sa.String(), nullable=False),
                sa.Column('email', sa.String(), unique=True, nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                       sa.Column('verified', sa.Boolean(), server_default="False", nullable=False),
                           sa.Column('status', sa.String(), nullable=False),
                              sa.Column('role', sa.String(), nullable=False),
                                 sa.Column('created_at', sa.String(), nullable=False),
                                    sa.Column('updated_at', sa.String(), nullable=False)
        )
    pass


def downgrade():
    op.drop_table('users')
    pass


