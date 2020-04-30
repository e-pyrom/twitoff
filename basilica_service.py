import basilica
import os
from dotenv import load_dotenv

load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection("BASILICA_API_KEY")
print(type(connection))

breakpoint()
embedding = connection.embed_sentence("Hey, this is a cool tweet", model='twitter')