"""empty message

Revision ID: 2b18d25cd3fa
Revises: a5cffa318ac2
Create Date: 2024-02-18 19:40:17.906043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b18d25cd3fa'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=40), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('homeworld_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('character_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planet',
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('resident_id', sa.Integer(), nullable=False),
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['resident_id'], ['character.character_id'], ),
    sa.PrimaryKeyConstraint('planet_id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.character_id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.planet_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('film',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.Column('director', sa.String(length=40), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['character.character_id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.planet_id'], ),
    sa.PrimaryKeyConstraint('film_id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=80), nullable=True))
        batch_op.drop_constraint('user_email_key', type_='unique')
        batch_op.drop_column('email')
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.create_unique_constraint('user_email_key', ['email'])
        batch_op.drop_column('username')

    op.drop_table('film')
    op.drop_table('favorite')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###
