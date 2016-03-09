"""
Configuration of 'memos' Flask app. 
Edit to fit development or deployment environment.

"""
import random 

#Secrets are held in the main directory of the project

### My local development environment
PORT=5000
DEBUG = True
GOOGLE_LICENSE_KEY = "local_client_secret.json"

### On ix.cs.uoregon.edu (Michal Young's instance of MongoDB)
#PORT=random.randint(5000,8000)
#DEBUG = False # Because it's unsafe to run outside localhost
#GOOGLE_LICENSE_KEY = "ix_client_secret.json"

