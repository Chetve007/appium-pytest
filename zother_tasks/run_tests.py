#!/usr/bin/env python3
"""
Скрипт для запуска автотестов
"""

import os
import sys
import subprocess
import argparse
from datetime import datetime


def run_command(command):
    """Выполнение команды с выводом результата"""
    print(f"Выполняется команда: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.stdout:
        print("STDOUT:")
        print(result.stdout)
    
    if result.stderr:
        print("STDERR:")
        print(result.stderr)
    
    return result.returncode == 0


def create_reports_dir():
    """Создание папки для отчетов"""
    reports_dir = "../reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
        print(f"Создана папка: {reports_dir}")


def run_tests(test_type="all", parallel=False, generate_reports=True):
    """Запуск тестов"""
    create_reports_dir()
    
    # Базовые опции pytest
    pytest_options = ["pytest", "-v"]
    
    # Добавление маркеров в зависимости от типа тестов
    if test_type == "smoke":
        pytest_options.extend(["-m", "smoke"])
    elif test_type == "login":
        pytest_options.extend(["-m", "login"])
    elif test_type == "registration":
        pytest_options.extend(["-m", "registration"])
    elif test_type == "home":
        pytest_options.extend(["-m", "home"])
    
    # Параллельное выполнение
    if parallel:
        pytest_options.extend(["-n", "auto"])
    
    # Генерация отчетов
    if generate_reports:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pytest_options.extend([
            "--html", f"reports/report_{timestamp}.html",
            "--self-contained-html",
            "--junitxml", f"reports/junit_{timestamp}.xml"
        ])
    
    # Выполнение команды
    command = " ".join(pytest_options)
    success = run_command(command)
    
    if success:
        print("\n✅ Тесты выполнены успешно!")
        if generate_reports:
            print(f"📊 Отчеты сохранены в папке reports/")
    else:
        print("\n❌ Тесты завершились с ошибками!")
        sys.exit(1)


def main():
    """Основная функция"""
    parser = argparse.ArgumentParser(description="Запуск автотестов Appium")
    parser.add_argument(
        "--type", 
        choices=["all", "smoke", "login", "registration", "home"],
        default="all",
        help="Тип тестов для запуска"
    )
    parser.add_argument(
        "--parallel", 
        action="store_true",
        help="Запуск тестов параллельно"
    )
    parser.add_argument(
        "--no-reports", 
        action="store_true",
        help="Не генерировать отчеты"
    )
    
    args = parser.parse_args()
    
    print("🚀 Запуск автотестов Appium")
    print(f"📋 Тип тестов: {args.type}")
    print(f"⚡ Параллельное выполнение: {'Да' if args.parallel else 'Нет'}")
    print(f"📊 Генерация отчетов: {'Нет' if args.no_reports else 'Да'}")
    print("-" * 50)
    
    run_tests(
        test_type=args.type,
        parallel=args.parallel,
        generate_reports=not args.no_reports
    )


if __name__ == "__main__":
    main()
