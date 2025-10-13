"""create user table

Revision ID: 2bcc62a0d4fb
Revises: 
Create Date: 2025-09-28 19:40:16.257207

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2bcc62a0d4fb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, comment='уникальный идентификатор'),
        sa.Column('name', sa.String(length=25), nullable=False, comment='имя пользователя'),
        sa.Column('surname', sa.String(length=25), nullable=False, comment='фамилия пользователя'),
        sa.Column('password', sa.String(length=50), nullable=False, comment='пароль пользователя'),
        sa.Column('email', sa.String(length=50), nullable=False, unique=True, comment='почтовый адрес пользователя'),
    )
    op.create_index('ix_users_email', 'users', ['email'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index('ix_users_email', table_name='users')
    op.drop_table('users')
