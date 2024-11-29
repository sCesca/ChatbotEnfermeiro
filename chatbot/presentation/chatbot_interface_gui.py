from typing import List, Optional
import tkinter as tk
from chatbot.application.chatbot_logic import ChatbotLogic


class ChatbotInterfaceGUI:
    def __init__(self, chatbot_logic: ChatbotLogic) -> None:
        self.chatbot_logic = chatbot_logic
        self.root = tk.Tk()
        self.root.title("Chatbot Enfermeiro")
        self.create_widgets()

    def create_widgets(self) -> None:
        """Cria os widgets da interface gráfica."""
        # Área para exibir o histórico de conversas
        self.chat_log = tk.Text(self.root, state='disabled', bg="#f0f0f0")
        self.chat_log.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Área para exibir comandos disponíveis
        self.commands_label = tk.Label(
            self.root, text="Comandos disponíveis:", font=("Arial", 12), anchor="w"
        )
        self.commands_label.pack(fill=tk.X, padx=10)
        self.commands_area = tk.Text(
            self.root, height=5, wrap=tk.WORD, state='disabled', bg="#f0f0f0"
        )
        self.commands_area.pack(pady=5, padx=10, fill=tk.X)
        self.update_commands([
            "listar - Exibe a lista de sintomas.",
            "Digite o número do sintoma para selecioná-lo.",
            "finalizar - Analisa os sintomas selecionados."
        ])

        # Campo de entrada para o usuário
        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10, padx=10, fill=tk.X)
        self.entry.bind("<Return>", self.send_message)

        # Botão para enviar mensagens
        self.send_button = tk.Button(
            self.root, text="Enviar", command=self.send_message, font=("Arial", 12)
        )
        self.send_button.pack(pady=5)

        # Mensagem inicial
        self.display_message(
            "Chatbot", "Olá! Sou o Chatbot Enfermeiro. Como posso ajudá-lo?"
        )

    def update_commands(self, commands: List[str]) -> None:
        """Atualiza a lista de comandos exibidos na interface."""
        self.commands_area.config(state='normal')
        self.commands_area.delete(1.0, tk.END)
        self.commands_area.insert(tk.END, "\n".join(commands))
        self.commands_area.config(state='disabled')

    def display_message(self, sender: str, message: str) -> None:
        """Exibe uma mensagem no histórico de conversas."""
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, f"{sender}: {message}\n")
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)

    def send_message(self, event: Optional[tk.Event] = None) -> None:
        """Lida com a entrada do usuário."""
        user_input = self.entry.get()
        if user_input:
            self.display_message("Você", user_input)
            response = self.chatbot_logic.get_response(user_input)
            self.display_message("Chatbot", response)
            self.entry.delete(0, tk.END)

    def start(self) -> None:
        """Inicia a interface gráfica."""
        self.root.mainloop()
