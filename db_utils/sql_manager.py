import sqlalchemy


# context manager for database
class sql_manager:
    
    def __init__(self):
        self.db_path = 'sqlite:///F:\\Python projects\\intma\\test.db'
        
    def __enter__(self):
        self.engine = sqlalchemy.create_engine(self.db_path, echo=True)
        return self.engine
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        
        self.engine.dispose()