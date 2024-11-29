from typing import List, Dict


class ChatbotLogic:
    def __init__(self) -> None:
        self.sintomas: Dict[int, str] = {
            1: "Febre",
            2: "Dor de cabeça",
            3: "Dor abdominal",
            4: "Cansaço excessivo",
            5: "Tosse",
            6: "Dificuldade para respirar",
            7: "Náusea ou vômito",
            8: "Diarreia",
            9: "Dor muscular",
            10: "Tontura",
        }

        self.ajudas: Dict[frozenset, str] = {
            frozenset({1, 5, 6}): (
                "Pode ser uma infecção respiratória ou gripe. "
                "Recomendo procurar um médico se os sintomas persistirem."
            ),
            frozenset({2, 9, 4}): (
                "Pode ser tensão muscular ou fadiga. Beba água e descanse. "
                "Consulte um médico se a dor continuar."
            ),
            frozenset({3, 7, 8}): (
                "Pode ser uma infecção gastrointestinal. Beba líquidos e procure ajuda "
                "médica se os sintomas se agravarem."
            ),
            frozenset({1, 4, 10}): (
                "Pode ser desidratação ou febre alta. Beba água e monitore "
                "sua temperatura."
            ),
        }

        # Lista de sintomas selecionados
        self.sintomas_selecionados: List[int] = []

    def get_response(self, user_input: str) -> str:
        """Processa a entrada do usuário e retorna a resposta do chatbot."""

        # Comando 'listar' ou 'sintomas'
        if user_input.lower() in {"listar", "sintomas"}:
            sintomas_list = "\n".join(
                [f"{codigo}. {sintoma}" for codigo, sintoma in self.sintomas.items()]
            )
            return f"Aqui estão os sintomas disponíveis:\n{sintomas_list}"

        # Verificação para selecionar sintoma
        elif user_input.isdigit() and int(user_input) in self.sintomas:
            sintoma = int(user_input)
            if sintoma not in self.sintomas_selecionados:
                self.sintomas_selecionados.append(sintoma)
                return (
                    f"Sintoma '{self.sintomas[sintoma]}' adicionado. "
                    "Digite 'finalizar' para analisar os sintomas."
                )
            else:
                return f"O sintoma '{self.sintomas[sintoma]}' já foi selecionado."

        # Finalizar seleção de sintomas e sugerir ajuda
        elif user_input.lower() == "finalizar":
            if not self.sintomas_selecionados:
                return (
                    "Nenhum sintoma foi selecionado. "
                    "Digite 'listar' para ver os sintomas disponíveis."
                )

            sintomas_set = frozenset(self.sintomas_selecionados)
            for condicao, ajuda in self.ajudas.items():
                if condicao.issubset(sintomas_set):
                    return f"Sugestão: {ajuda}"

            # Caso nenhum conjunto de sintomas corresponda a uma condição
            return (
                "Os sintomas não correspondem a uma condição específica. "
                "Procure um médico para um diagnóstico mais preciso."
            )

        # Comando inválido
        return (
            "Comando inválido. Digite 'listar' para ver os sintomas disponíveis "
            "ou 'finalizar' para analisar os sintomas."
        )
