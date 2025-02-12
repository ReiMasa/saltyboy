"""Initial

Revision ID: 908066480906
Revises:
Create Date: 2021-12-17 23:10:42.825657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "908066480906"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "fighter",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=False, unique=True),
        sa.Column("tier", sa.String(1), nullable=False),
        sa.Column("created_time", sa.DateTime(), nullable=False),
        sa.Column("last_updated", sa.DateTime(), nullable=False),
        sa.Column("best_streak", sa.Integer(), nullable=False),
    )

    op.create_table(
        "match",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column(
            "fighter_red",
            sa.Integer(),
            sa.ForeignKey("fighter.id", onupdate="CASCADE", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "fighter_blue",
            sa.Integer(),
            sa.ForeignKey("fighter.id", onupdate="CASCADE", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "winner",
            sa.Integer(),
            sa.ForeignKey("fighter.id", onupdate="CASCADE", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("bet_red", sa.Integer(), nullable=False),
        sa.Column("bet_blue", sa.Integer(), nullable=False),
        sa.Column("streak_red", sa.Integer(), nullable=False),
        sa.Column("streak_blue", sa.Integer(), nullable=False),
        sa.Column("tier", sa.String(1), nullable=False),
        sa.Column("match_format", sa.String(16), nullable=False),
        sa.Column("colour", sa.String(8), nullable=False)
    )


def downgrade():
    op.drop_table("match")
    op.drop_table("fighter")
