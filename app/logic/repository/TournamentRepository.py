from app.logic.repository.BaseRepository import BaseRepository


class TournamentRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def initialize_table(self):
        sql = """USE db_main;
         CREATE TABLE IF NOT EXISTS 
                        tournament (id_ INTEGER PRIMARY KEY,
                                    name char(250) NOT NULL,
                                    date char(20),
                                    place char(100)    
                        );"""
        cursor = self.get_cursor()
        cursor.execute(sql, multi=True)
        self.close_connection()
