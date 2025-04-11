# Главный файл для запуска бота

from anekdot import show_anekdot
from input_data import get_user_input
from analyze import analyze_mood
from output_community import show_community

def main():
    print("Приветсвтую вас, дорогой пользователь! Я ваш текстовый бот-помощник. Чего хотите?")
    while True:
        print("\nМеню:")
        print("1 — Анекдот")
        print("2 — Сообщество по настроению")
        print("0 — Выход")
        
        choice = input("Введи номер команды: ")
        
        if choice == "1":
            show_anekdot()
        elif choice == "2":
            mood = get_user_input("Как дела, твои пользователь? Напишите ваше настроение: ")
            mood_result = analyze_mood(mood)
            show_community(mood_result)
        elif choice == "0":
            print("До скорой встречи, пользователь! Заходи ещё!")
            break
        else:
            print("Такой команды нет, попробуй ещё раз!")

if __name__ == "__main__":
    main()
