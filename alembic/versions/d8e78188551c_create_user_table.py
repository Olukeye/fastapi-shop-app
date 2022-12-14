from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8e78188551c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.BigInteger(), nullable=False),
            sa.Column('username', sa.String(), nullable=False),
                sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                       sa.Column('verified', sa.Boolean(), server_default="False", nullable=False),
                           sa.Column('status', sa.String(), nullable=False),
                              sa.Column('role', sa.String(), nullable=False),
                                 sa.Column('created_at', sa.String(),server_default=sa.text('now()'), nullable=False),
                                    sa.Column('updated_at', sa.String(), server_default=sa.text('now()'), nullable=False),
                                       sa.PrimaryKeyConstraint('id'),
                                          sa.UniqueConstraint('email')
        )
    pass


def downgrade():
    op.drop_table('users')
    pass
