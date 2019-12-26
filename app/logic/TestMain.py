import mysql.connector

from app.logic.repository.BaseRepository import BaseRepository
from app.logic.repository.TournamentRepository import TournamentRepository

#print(TournamentRepository.initialize_db())

A = TournamentRepository()
print((A.create_db()))
print((A.initialize_table()))

