from datetime import datetime
from typing import Literal


SessionType = Literal["biling", "test_2", "test_4"]


def _write_line(line: str, file_path: str = "session.txt") -> None:
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        # Не ломаем бота, если файл недоступен.
        pass


def log_biling_session(
    tg_id: int,
    language_pair: str,
    score: int,
    total_questions: int,
    file_path: str = "session.txt",
) -> None:
    """Логирование сессии билингвального теста.

    Формат:
    YYYY-MM-DD HH:MM:SS;tg_id;biling;language_pair;score/total
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = (
        f"{timestamp};{tg_id};biling;{language_pair};"
        f"{score}/{total_questions}\n"
    )
    _write_line(line, file_path)


def log_simple_test_session(
    tg_id: int,
    test_type: SessionType,
    value: int,
    file_path: str = "session.txt",
) -> None:
    """Логирование сессии для тестов test_2 и test_4.

    Для test_2 в value пишем количество правильных слов.
    Для test_4 в value пишем 1 (правильно) или 0 (неправильно).

    Формат:
    YYYY-MM-DD HH:MM:SS;tg_id;test_type;-;value
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp};{tg_id};{test_type};-;{value}\n"
    _write_line(line, file_path)


def get_stats_for_user(
    tg_id: int,
    file_path: str = "session.txt",
) -> dict:
    """Возвращает простую статистику по пользователю.

    total_sessions   – сколько всего сессий.
    biling_count     – сколько билингв-тестов.
    biling_avg       – средний результат по билингв-тестам (0–1).
    test_2_count     – сколько раз пройден test_2.
    test_2_avg_words – среднее количество правильных слов в test_2.
    test_4_count     – сколько раз пройден test_4.
    test_4_correct   – доля корректных ответов в test_4 (0–1).
    """
    stats = {
        "total_sessions": 0,
        "biling_count": 0,
        "biling_avg": 0.0,
        "test_2_count": 0,
        "test_2_avg_words": 0.0,
        "test_4_count": 0,
        "test_4_correct": 0.0,
    }

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except OSError:
        return stats

    biling_sum_ratio = 0.0
    test_2_sum_words = 0
    test_4_sum_correct = 0

    for line in lines:
        parts = line.strip().split(";")
        if len(parts) != 5:
            continue

        _, line_tg_id, test_type, _, score_part = parts

        try:
            if int(line_tg_id) != tg_id:
                continue
        except ValueError:
            continue

        stats["total_sessions"] += 1

        if test_type == "biling":
            stats["biling_count"] += 1
            if "/" in score_part:
                num_str, den_str = score_part.split("/", 1)
                try:
                    num = int(num_str)
                    den = int(den_str)
                    if den > 0:
                        biling_sum_ratio += num / den
                except ValueError:
                    pass
        elif test_type == "test_2":
            stats["test_2_count"] += 1
            try:
                test_2_sum_words += int(score_part)
            except ValueError:
                pass
        elif test_type == "test_4":
            stats["test_4_count"] += 1
            try:
                test_4_sum_correct += int(score_part)  # 1 или 0
            except ValueError:
                pass

    if stats["biling_count"] > 0:
        stats["biling_avg"] = biling_sum_ratio / stats["biling_count"]

    if stats["test_2_count"] > 0:
        stats["test_2_avg_words"] = test_2_sum_words / stats["test_2_count"]

    if stats["test_4_count"] > 0:
        stats["test_4_correct"] = test_4_sum_correct / stats["test_4_count"]

    return stats

