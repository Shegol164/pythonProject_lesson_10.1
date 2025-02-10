import json
import os
from typing import Any
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"

def operation(open_file: Any) -> Any:
    """Принимает на вход имя JSON-файла по пути ./data/ и
    возвращает список словарей с данными о финансовых транзакциях"""
    open_file += ".json"
    try:
        with open(DATA_DIR / open_file, "r", encoding="utf-8") as jf:
            data = json.load(jf)
    except Exception as e:
        print(f"Ошибка {e}")
        return []
    except FileNotFoundError as e:
        print(f"Ошибка {e}")
        return []
    return data
