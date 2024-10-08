"""empty message

Revision ID: d56c92acb12a
Revises: a5cffa318ac2
Create Date: 2024-09-09 04:54:23.665651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd56c92acb12a'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('films',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=False),
    sa.Column('episode_id', sa.Integer(), nullable=True),
    sa.Column('opening_crawl', sa.String(length=500), nullable=True),
    sa.Column('director', sa.String(length=100), nullable=True),
    sa.Column('producer', sa.String(length=100), nullable=True),
    sa.Column('release_date', sa.DateTime(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('birth_year', sa.String(length=10), nullable=True),
    sa.Column('eye_color', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('hair_color', sa.String(length=50), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Float(), nullable=True),
    sa.Column('skin_color', sa.String(length=50), nullable=True),
    sa.Column('homeworld', sa.String(length=250), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('climate', sa.String(length=50), nullable=True),
    sa.Column('diameter', sa.String(length=50), nullable=True),
    sa.Column('gravity', sa.String(length=50), nullable=True),
    sa.Column('orbital_period', sa.String(length=50), nullable=True),
    sa.Column('population', sa.String(length=50), nullable=True),
    sa.Column('rotation_period', sa.String(length=50), nullable=True),
    sa.Column('surface_water', sa.String(length=50), nullable=True),
    sa.Column('terrain', sa.String(length=100), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('classification', sa.String(length=100), nullable=True),
    sa.Column('designation', sa.String(length=50), nullable=True),
    sa.Column('average_height', sa.String(length=50), nullable=True),
    sa.Column('skin_colors', sa.String(length=100), nullable=True),
    sa.Column('hair_colors', sa.String(length=100), nullable=True),
    sa.Column('eye_colors', sa.String(length=100), nullable=True),
    sa.Column('average_lifespan', sa.String(length=50), nullable=True),
    sa.Column('homeworld', sa.String(length=250), nullable=True),
    sa.Column('language', sa.String(length=100), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('starships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('model', sa.String(length=250), nullable=True),
    sa.Column('manufacturer', sa.String(length=250), nullable=True),
    sa.Column('cost_in_credits', sa.String(length=50), nullable=True),
    sa.Column('length', sa.String(length=50), nullable=True),
    sa.Column('max_atmosphering_speed', sa.String(length=50), nullable=True),
    sa.Column('crew', sa.Integer(), nullable=True),
    sa.Column('passengers', sa.Integer(), nullable=True),
    sa.Column('cargo_capacity', sa.String(length=50), nullable=True),
    sa.Column('consumables', sa.String(length=50), nullable=True),
    sa.Column('hyperdrive_rating', sa.String(length=50), nullable=True),
    sa.Column('MGLT', sa.String(length=50), nullable=True),
    sa.Column('starship_class', sa.String(length=100), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('model', sa.String(length=250), nullable=True),
    sa.Column('manufacturer', sa.String(length=250), nullable=True),
    sa.Column('cost_in_credits', sa.String(length=50), nullable=True),
    sa.Column('length', sa.String(length=50), nullable=True),
    sa.Column('max_atmosphering_speed', sa.String(length=50), nullable=True),
    sa.Column('crew', sa.Integer(), nullable=True),
    sa.Column('passengers', sa.Integer(), nullable=True),
    sa.Column('cargo_capacity', sa.String(length=50), nullable=True),
    sa.Column('consumables', sa.String(length=50), nullable=True),
    sa.Column('vehicle_class', sa.String(length=100), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('films_people',
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['people.id'], )
    )
    op.create_table('films_planets',
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], )
    )
    op.create_table('films_species',
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.Column('species_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['species_id'], ['species.id'], )
    )
    op.create_table('films_starships',
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.Column('starship_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['starship_id'], ['starships.id'], )
    )
    op.create_table('films_vehicles',
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], )
    )
    op.create_table('people_species',
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('species_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['species_id'], ['species.id'], )
    )
    op.create_table('user_favorite_films',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('user_favorite_planets',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('user_favorite_species',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('species_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['species_id'], ['species.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('user_favorite_starships',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('starship_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['starship_id'], ['starships.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('user_favorite_vehicles',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], )
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('user_favorite_vehicles')
    op.drop_table('user_favorite_starships')
    op.drop_table('user_favorite_species')
    op.drop_table('user_favorite_planets')
    op.drop_table('user_favorite_films')
    op.drop_table('people_species')
    op.drop_table('films_vehicles')
    op.drop_table('films_starships')
    op.drop_table('films_species')
    op.drop_table('films_planets')
    op.drop_table('films_people')
    op.drop_table('vehicles')
    op.drop_table('users')
    op.drop_table('starships')
    op.drop_table('species')
    op.drop_table('planets')
    op.drop_table('people')
    op.drop_table('films')
    # ### end Alembic commands ###
