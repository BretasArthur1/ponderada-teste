import os
import dotenv

dotenv.load_dotenv()

class EnvManager:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.aluno_id = os.getenv("ALUNO_ID")
        self.headers = {
            "Content-Type": "application/json"
        }      
    def get_base_url(self):
        return self.base_url
    
    def get_aluno_id(self):
        return self.aluno_id
    
    def get_headers(self):
        return self.headers

    
        