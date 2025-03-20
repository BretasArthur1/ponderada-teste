import requests
import os 
import dotenv
import pytest


dotenv.load_dotenv()


# Essa classe é responsável por obter os dados do aluno e realizar as requisicoes que serao testadas
class RequestData:
    def __init__(self):
        self.id = os.getenv("ALUNO_ID")
        self.base_url = os.getenv("BASE_URL")
        self.url = f"{self.base_url}/users/{self.id}"
        self.headers = {
            "Content-Type": "application/json"
        }

    def get_aluno_by_id(self):
        response = requests.get(self.url, headers=self.headers)
        assert response.status_code == 200, f"Erro ao buscar aluno: {response.status_code, response.text}"
        data = response.json()
        return data

# Essa fixture é responsável por criar uma instância da classe RequestData
@pytest.fixture
def req_data():
    return RequestData()

# Essa função é responsável por testar a função get_aluno_by_id
def test_get_aluno_by_id(req_data):
    data = req_data.get_aluno_by_id()
    
    assert data["data"][0]["id"] == req_data.id, f"ID do aluno nao corresponde ao esperado: {data['data'][0]['id']}"
    assert data["data"][0]["nome"] == "Maria Cecília Bastos Duarte", f"nome nao corresponde ao esperado: {data['data'][0]['nome']}"
    assert data["data"][0]["data_nascimento"] == "2003-10-16T00:00:00.000Z", f"data_nascimento nao corresponde ao esperado: {data['data'][0]['data_nascimento']}"
    assert data["data"][0]["responsavel_nome"] == "Kelly Fernandes Sampaio", f"responsavel_nome nao corresponde ao esperado: {data['data'][0]['responsavel_nome']}"
    assert data["data"][0]["responsavel_tipo"] == "Filho(a)", f"responsavel_tipo nao corresponde ao esperado: {data['data'][0]['responsavel_tipo']}"
    assert data["data"][0]["responsavel_email"] == "upsilon369@exemplo.com", f"responsavel_email nao corresponde ao esperado: {data['data'][0]['responsavel_email']}"
    assert data["data"][0]["responsavel_telefone"] == "+55 23 90360-8843", f"responsavel_telefone nao corresponde ao esperado: {data['data'][0]['responsavel_telefone']}"
    assert data["data"][0]["atendimento_unidade_anterior"] == True, f"atendimento_unidade_anterior nao corresponde ao esperado: {data['data'][0]['atendimento_unidade_anterior']}"
    assert data["data"][0]["mais_casos_familia"] == False, f"mais_casos_familia nao corresponde ao esperado: {data['data'][0]['mais_casos_familia']}"
    assert data["data"][0]["observacoes_casos_familia"] == "Não há histórico familiar", f"observacoes_casos_familia nao corresponde ao esperado: {data['data'][0]['observacoes_casos_familia']}"



if __name__ == "__main__":
    req = RequestData()
    test_get_aluno_by_id(req)