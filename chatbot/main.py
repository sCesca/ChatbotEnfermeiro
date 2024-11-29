from chatbot.application.chatbot_logic import ChatbotLogic
from chatbot.presentation.chatbot_interface_gui import ChatbotInterfaceGUI


def main() -> None:
    logic = ChatbotLogic()
    gui = ChatbotInterfaceGUI(logic)
    gui.start()


if __name__ == "__main__":
    main()
