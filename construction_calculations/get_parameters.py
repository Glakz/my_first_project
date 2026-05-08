"""Модуль ввода параметров кирпича, стены и растворного шва."""

from typing import Union

def get_float_input(param_name: str, default_value: Union[int, float]) -> Union[int, float]:
    """Запрашивает у пользователя число с возможностью пропуска (значение по умолчанию).

    Args:
        param_name: Название параметра на русском (выводится в приглашении).
        default_value: Значение по умолчанию, если пользователь вводит пустую строку.

    Returns:
        Введённое число (int или float) либо default_value, если ввод пропущен.

    Raises:
        Нет явных исключений – все ошибки ввода обрабатываются внутри.
    """
    while True:
        user_input = input(f"  {param_name} (по умолчанию {default_value}): ").strip()
        if user_input == "":
            return default_value
        try:
            value = float(user_input)
            return value
        except ValueError:
            print(f"  Ошибка: для параметра '{param_name}' нужно ввести число или оставить поле пустым "
                  f"(будет {default_value}).")


def get_brick_parameters() -> dict[str, float]:
    """Запрашивает размеры кирпича, возвращает словарь с англоязычными ключами.

    Returns:
        Словарь вида {'length': float, 'width': float, 'height': float},
        где значения в миллиметрах.
    """
    print("Для использования размеров кирпича по умолчанию нажмите: < Ввод >")
    print("Либо введите параметры кирпича сами (в мм):")
    length = get_float_input("Длина", 250)
    width = get_float_input("Ширина", 120)
    height = get_float_input("Высота", 65)
    return {"length": length, "width": width, "height": height}


def get_wall_parameters() -> dict[str, float]:
    """Запрашивает размеры стены, возвращает словарь с англоязычными ключами.

    Returns:
        Словарь вида {'length': float, 'thickness': float, 'height': float},
        где значения в миллиметрах.
    """
    print("Для использования размеров стены по умолчанию нажмите: < Ввод >")
    print("Либо введите параметры стены сами (в мм):")
    length = get_float_input("Длина", 10000)
    thickness = get_float_input("Толщина", 510)
    height = get_float_input("Высота", 3000)
    return {"length": length, "thickness": thickness, "height": height}


def get_mortar_parameters() -> float:
    """Запрашивает толщину растворного шва.

    Returns:
        Толщина шва в миллиметрах (float).
    """
    print("Для использования толщины растворного шва по умолчанию нажмите: < Ввод >")
    print("Либо введите толщину растворного шва сами (в мм):")
    mortar = get_float_input("Шов", 10)
    return mortar