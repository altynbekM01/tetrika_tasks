#Tetrika

Решения и условия задач находятся в соответствующих директориях:
task_1/, task_2/, task_3/
## 🚀 Установка и запуск



1. Клонируйте репозиторий:
```
git clone https://github.com/altynbekM01/tetrika_tasks.git
```

2. Создайте и активируйте виртуальное окружение

```
python -m venv venv
source venv/bin/activate  # для Linux/macOS
.\venv\Scripts\activate   # для Windows
```

3. Установите зависимости:
```
pip install -r requirements.txt
```

Выполните одну из следующих команд для запуска конкретного задания:

```
python task_1/solution.py
python task_2/solution.py
python task_3/solution.py
```

Для тестирования решений использована библиотека pytest
Команда для запуска тестов
```
pytest
```

task_1 и task_2 покрыты юнит-тестами через pytest.

В task_3 тестирование выполнено вручную через встроенный блок if __name__ == "__main__"