import sqlalchemy as sqla
CONNECTION_STRING = "mysql+pymysql://root:root@localhost:3007/workinauditory"

class Database():
    def __init__(self):
        self.engine = sqla.create_engine(CONNECTION_STRING)
        self.connection = self.engine.connect()
    
    def translate_to_dict(self,result_raw):
        result = []
        for r in result_raw:
            result.append(r._asdict())
        return result
    
    def get_animals(self):
        query = sqla.text("SELECT * FROM animals")
        result_raw = self.connection.execute(query).all()
        return self.translate_to_dict(result_raw)
    
    def del_animals(self, id):
        query = sqla.text("DELETE FROM animals WHERE id = :id")
        query = query.bindparams(sqla.bindparam("id", id))
        self.connection.execute(query)
        self.connection.commit()

    def add_animals(self, name):
        query = sqla.text("INSERT INTO animals (name VALUES) (:name)")
        query = query.bindparams(sqla.bindparam("name", name))
        self.connection.execute(query)
        self.connection.commit()

    def edit_animals(self, name):
        query = sqla.text("UPDATE animals SET name = :name WHERE id = :id")
        query = query.bindparams(sqla.bindparam("name", name))
        query = query.bindparams(sqla.bindparam("id", id))
        self.connection.execute(query)
        self.connection.commit()

if __name__ == "__name__":
    db = Database()
    db.del_animals