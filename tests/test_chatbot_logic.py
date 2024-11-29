import pytest
from chatbot.application.chatbot_logic import ChatbotLogic


@pytest.fixture
def chatbot() -> ChatbotLogic:
    """Fixture para criar uma instância do ChatbotLogic."""
    return ChatbotLogic()


def test_get_response_listar(chatbot: ChatbotLogic) -> None:
    """Teste para o comando 'listar'"""
    user_input = "listar"
    expected_response = (
        "Aqui estão os sintomas disponíveis:\n"
        "1. Febre\n"
        "2. Dor de cabeça\n"
        "3. Dor abdominal\n"
        "4. Cansaço excessivo\n"
        "5. Tosse\n"
        "6. Dificuldade para respirar\n"
        "7. Náusea ou vômito\n"
        "8. Diarreia\n"
        "9. Dor muscular\n"
        "10. Tontura"
    )
    assert chatbot.get_response(user_input) == expected_response


def test_get_response_selecionar_sintoma(chatbot: ChatbotLogic) -> None:
    """Teste para selecionar um sintoma"""
    user_input = "1"
    expected_response = (
        "Sintoma 'Febre' adicionado. Digite 'finalizar' para analisar os sintomas."
    )
    assert chatbot.get_response(user_input) == expected_response


def test_get_response_finalizar(chatbot: ChatbotLogic) -> None:
    """Teste para finalizar a seleção de sintomas"""
    chatbot.get_response("1")
    chatbot.get_response("5")
    chatbot.get_response("6")
    user_input = "finalizar"
    expected_response = (
        "Sugestão: Pode ser uma infecção respiratória ou gripe. "
        "Recomendo procurar um médico se os sintomas persistirem."
    )
    assert chatbot.get_response(user_input) == expected_response


def test_get_response_comando_invalido(chatbot: ChatbotLogic) -> None:
    """Teste para comando inválido"""
    user_input = "Oi"
    expected_response = (
        "Comando inválido. Digite 'listar' para ver os sintomas disponíveis "
        "ou 'finalizar' para analisar os sintomas."
    )
    assert chatbot.get_response(user_input) == expected_response
