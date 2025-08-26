# Appium Mobile Testing Project

Проект автоматизированного тестирования мобильного приложения с использованием Appium, Python 3.12, pytest и паттерна Page Object.

## Структура проекта

```bash
appium-pytest/
├── pages/                 # Page Objects
│   ├── __init__.py
│   ├── base_page.py      # Базовый класс для всех страниц
│   └── login_page.py     # Страница логина
├── tests/                # Тесты
│   ├── __init__.py
│   └── test_login.py     # Тесты логина
├── conftest.py           # Конфигурация pytest и фикстуры
├── pytest.ini            # Настройки pytest
├── requirements.txt      # Зависимости
├── login_app.apk         # Тестируемое приложение
└── README.md             # Документация
```

## Установка и настройка

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Установка Appium Server

```bash
npm install -g appium
```

### 3. Установка Android SDK и эмулятора

- Установите Android Studio
- Создайте Android Virtual Device (AVD)
- Убедитесь, что ANDROID_HOME настроен в переменных окружения

### 4. Запуск Appium Server

```bash
appium
```

## Запуск тестов

### Запуск всех тестов

```bash
pytest
```

## Конфигурация

### Настройки Appium и параметры командной строки в conftest.py

### Переменные окружения

Убедитесь, что установлены:
- Python 3.12
- Node.js и npm
- Android SDK
- Java JDK

## Troubleshooting

### Проблемы с подключением к Appium
1. Убедитесь, что Appium Server запущен
2. Проверьте, что порт 4723 свободен
3. Проверьте настройки эмулятора

### Проблемы с эмулятором
1. Убедитесь, что AVD создан и запущен
2. Проверьте, что ANDROID_HOME настроен
3. Проверьте версию Android SDK

### Проблемы с APK
1. Убедитесь, что файл login_app.apk находится в корне проекта или по пути указанному в переменной `--apk-path`
2. Проверьте, что APK совместим с версией Android эмулятора

## Для переопределения base-path, по умолчанию /
``appium --base-path /wd/hub --log-level info``
