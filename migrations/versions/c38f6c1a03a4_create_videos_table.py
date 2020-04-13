"""create videos table

Revision ID: c38f6c1a03a4
Revises: ec03cb2683cb
Create Date: 2020-04-06 13:32:32.799338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c38f6c1a03a4'
down_revision = 'ec03cb2683cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('video',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('video_url', sa.String(length=150), nullable=True),
    sa.Column('video_name', sa.String(length=20), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_video_timestamp'), 'video', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_video_timestamp'), table_name='video')
    op.drop_table('video')
    # ### end Alembic commands ###
