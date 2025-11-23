import sqlalchemy as sa
from random import choice,randint,shuffle

class PasswordManagerBE:
    def __init__(self) -> None:
        self.engine = sa.create_engine('sqlite:///passwords.db')
        self.connection = self.engine.connect()
        self.meta_data = sa.MetaData()

        self.passwords = sa.Table('passwords', self.meta_data,
                             sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                             sa.Column('website', sa.String()),
                             sa.Column('email', sa.String()),
                             sa.Column('password', sa.String())
                             )
        
        self.meta_data.create_all(self.engine)

    def save_data(self, p_website, p_email, p_password):
        with self.connection.begin():
            insert_query = self.passwords.insert().values(website=p_website ,email = p_email, password = p_password)
            self.connection.execute(insert_query)
    

    def search_data(self, website):
        with self.connection.begin():
            search = "%{website.strip().lower()}%"
            select_query = self.passwords.select().where(sa.func.lower(self.passwords.c.website).like(f"%{website.strip().lower()}%"))
            result = self.connection.execute(select_query).fetchone()
            return result
        

    def close_conn(self):
        self.connection.close()

    def generate_password(self):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = "1234567890"
        symbols = "-+=!@#$%^&*"

        letters_list = [choice(letters) for _ in range(1, randint(8, 12))]
        num_list = [choice(nums) for num in range(1, randint(3, 5))]
        symbol_list = [choice(symbols) for symbol in range(1, randint(3, 5))]

        password_list = letters_list + num_list + symbol_list
        shuffle(password_list)
        password = "".join(password_list)
        return password
        

        