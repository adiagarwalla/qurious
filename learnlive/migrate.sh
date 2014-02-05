
# this is a migrate helper script, should make running migrations a less onerous task
mysql.server start
python manage.py schemamigration auth --auto
python manage.py schemamigration inclass --auto
python manage.py schemamigration dashboard --auto
python manage.py schemamigration bid_platform --auto
python manage.py schemamigration query_parser --auto

python manage.py migrate
