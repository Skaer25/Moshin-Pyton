# Файл для анализа данных (например, настроения)

def analyze_mood(text):
    if "хорошо" in text.lower() or "круто" in text.lower():
        return "позитив"
    elif "плохо" in text.lower() or "грустно" in text.lower():
        return "негатив"
    else:
        return "нейтрал"
