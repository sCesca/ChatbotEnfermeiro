from typing import List


class Repository:
    """Simula uma base de dados para armazenar dados de conversas."""

    def __init__(self) -> None:
        self.data: List[str] = []

    def save_message(self, message: str) -> None:
        self.data.append(message)

    def get_all_messages(self) -> List[str]:
        return self.data
