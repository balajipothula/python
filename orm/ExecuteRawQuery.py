import psycopg2

from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy import text


def lambda_handler(event, context):

  dialect  = "postgres"
  driver   = "psycopg2"
  host     = "127.0.0.1"
  port     =  5432
  user     = "postgres"
  password = "Postgres#123"
  database = "emp"
  echo     = True,
  connect_timeout = 60

  print("PsycopgVersion: " + str(psycopg2.__version__))
  connect = psycopg2.connect(host     = host,
                             port     = port,
                             user     = user,
                             password = password,
                             database = database)
  cursor  = connect.cursor()
  cursor.execute("SELECT version()")
  print(cursor.fetchone())
  cursor.close()
  connect.close()

  print("SQLAlchemyVersion: " + str(sqlalchemy.__version__))
  engine     = create_engine("sqlite:///emp.db")
  url        = URL(drivername = dialect + "+" + driver,
                   username   = username,
                   password   = password,
                   host       = host,
                   port       = port,
                   database   = database,
                   query      = None)
  engine     = create_engine(url,
                             echo = echo,
                             connect_args = { "connect_timeout": connect_timeout })
  connect    = engine.connect()
  query      = text(""" SELECT count(*) AS "Count" FROM "public"."Emp" """)
  query      = text(""" SELECT version() """)
  result_set = connect.execute(query)
  print(result_set.fetchone())

  inspect = inspect(engine)
  columns = inspect.get_columns("Emp")
  for column in columns: print(column.name)


lambda_handler(event = None, context = None)
