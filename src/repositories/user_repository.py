from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
	return User(row["username"], row["password"]) if row else None

class UserRepository:
	def __init__(self, connection):
		self._connection = connection

	def create(self, user):
		cursor = self._connection.cursor()

		try:
			cursor.execute(" insert into users (username, password) values (?, ?)", (user.username, user.password)) 
		except sqlite3.IntegrityError:
			raise IntegrityError

		self._connection.commit()

		return user

	def find_by_username(self, username):
		cursor = self._connection.cursor()

		cursor.execute(" select * from users where username = ?", (username, ))

		row = cursor.fetchone()

		return get_user_by_row(row)

	def find_all(self):
		cursor = self._connection.cursor()

		cursor.execute("select * from users")

		rows = cursor.fetchall()

		return list(map(get_users_by_row, rows))

user_repository = UserRepository(get_database_connection())
