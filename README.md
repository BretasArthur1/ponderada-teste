# **Caso de Teste: Buscar um Aluno por ID**

## **Objetivo**
Verificar se o sistema retorna corretamente os dados de um aluno específico ao buscar por seu ID.

## **Pré-condições**
1. O sistema deve estar rodando e acessível.
2. Deve haver pelo menos um aluno cadastrado no banco de dados.
3. O sistema deve contar o método de busca esperado como get/students/{id}


## **Procedimento de Teste**
1. Fazer uma requisição HTTP **GET** para o endpoint de busca de aluno, fornecendo um ID válido.
2. Verificar se a resposta tem código **200 OK**.
3. Validar se os dados retornados correspondem ao aluno esperado.

## **Entrada de Dados**
- **ID do aluno:** `1` (Ex de ID)

## **Resultado Esperado**
- O sistema deve retornar um código **200 OK**.
- O corpo da resposta deve conter os detalhes corretos do aluno, como:
  ```json
    {
        "data": [
            {
            "id": "1",
            "nome": "Nome do Aluno",
            "data_nascimento": "AAAA-MM-DDTHH:MM:SS.SSSZ",
            "responsavel_nome": "Nome do Responsável",
            "responsavel_tipo": "Tipo de Responsável",
            "responsavel_email": "email@exemplo.com",
            "responsavel_telefone": "+55 XX XXXXX-XXXX",
            "atendimento_unidade_anterior": true,
            "mais_casos_familia": false,
            "observacoes_casos_familia": "Observações sobre casos na família"
            }
        ]
    }
  ```

## **Resultado Obtido**
*(Preencher após a execução do teste)*  
Exemplo: O sistema retornou corretamente os dados do aluno.

## **Pós-condição**
O sistema permanece no mesmo estado, sem alterações nos dados.