# 🏎️ Car Game (Игра "Автогонка")

Простая аркадная игра на **Pygame**. Управляй машиной, избегая столкновений с врагами. Набирай очки за время выживания.

## Simple Arcade Racing Game

Simple arcade game made with **Pygame**. Control your car, avoid enemy cars, earn points for survival time.

## Установка / Installation

```bash
# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Установить зависимости
pip install pygame pygame-menu
```

## Управление / Controls

| Клавиша | Действие / Action |
|---------|-------------------|
| ←→    | Движение машины / Move |
| Space   | Пауза / Pause |
| ESC     | Выход в меню / Exit to menu |

## Функции / Features

- ✅ Меню с вводом имени
- ✅ Плавное управление
- ✅ Генерация врагов и полос
- ✅ Детекция столкновений
- ✅ Эффект тряски при ударе
- ✅ Таблица лидеров (топ-5)
- ✅ Сохранение в `table_score/scores.json`
- ✅ Пауза и FPS 60

## Запуск / Run

```bash
cd game/
python main.py
```

## Разработка / Development

Проект разбит на модули по принципу единственной ответственности:
- `config.py` - все константы в одном месте
- `Player` класс - вся логика игрока
- `Generators` - спавн и обновление объектов

**Исправленные баги оригинала:**
- Удаление врагов по правильной координате Y
- Правильный подсчет max_score
- `screen.fill()` в правильном месте
- Импорты констант

## Требования / Requirements

- Python 3.8+
- pygame 2.6+
- pygame-menu 4.5+

## Лицензия / License

MIT

