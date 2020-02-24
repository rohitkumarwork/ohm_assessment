"""New migration script

Revision ID: 451e88f872d8
Revises: 00000000
Create Date: 2020-02-24 17:48:23.393414

"""

# revision identifiers, used by Alembic.
revision = '451e88f872d8'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('''UPDATE user SET `point_balance`=5000 
        WHERE `user_id` = 1''')

    op.execute('''INSERT INTO `rel_user`(`user_id`, `rel_lookup`, `attribute`) 
        VALUES (2, 'LOCATION', 'USA')''')

    op.execute('''UPDATE user SET `tier`='Silver' WHERE `user_id` = 3''')


def downgrade():
    op.execute('''UPDATE user SET `point_balance`=0 
        WHERE `user_id` = 1''')

    op.execute('''DELETE FROM `rel_user` WHERE `user_id`=2''')

    op.execute('''UPDATE user SET `tier`=Carbon 
        WHERE `user_id` = 3''')    
