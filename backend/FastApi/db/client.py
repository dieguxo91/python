from pymongo import MongoClient

db_client = MongoClient() # si no ponemos nada usara el localhost

db_client_ip = MongoClient("mongodb+srv://dieguxo91:darkonce91@cluster0.gvvq31n.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp").prueba # metemos la url 