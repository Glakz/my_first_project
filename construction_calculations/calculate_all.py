"""Модуль расчёта количества кирпичей, объёма раствора и необходимости подрезки."""

from operator import itemgetter
from typing import Optional, Union, Dict, Any

from get_parameters import get_brick_parameters, get_mortar_parameters, get_wall_parameters


def calculate_all(brick_lwh: Optional[Dict[str, float]] = None,
                  wall_lwh: Optional[Dict[str, float]] = None,
                  mortar: Optional[Union[int, float]] = None) -> Dict[str, Any]:
    """Выполняет полный расчёт материалов для стены.

    Если какой-либо из параметров не передан, он запрашивается у пользователя
    через соответствующие функции из модуля get_parameters.

    Args:
        brick_lwh: Словарь с ключами 'length', 'width', 'height' (мм).
        wall_lwh: Словарь с ключами 'length', 'thickness', 'height' (мм).
        mortar: Толщина растворного шва (мм).

    Returns:
        Словарь с результатами:
            - total_bricks: количество целых кирпичей (int)
            - mortar_volume_mm3: объём раствора в кубических миллиметрах (float)
            - mortar_volume_liters: объём раствора в литрах (float)
            - trim_info: информация о подрезке (словарь, возвращаемый
              функцией calculation_of_remains_and_trim)
    """
    if brick_lwh is None:
        brick_lwh = get_brick_parameters()
    if wall_lwh is None:
        wall_lwh = get_wall_parameters()
    if mortar is None:
        mortar = get_mortar_parameters()

    brick_length, brick_width, brick_height = itemgetter('length', 'width', 'height')(brick_lwh)
    wall_length, wall_thickness, wall_height = itemgetter('length', 'thickness', 'height')(wall_lwh)

    # Количество целых кирпичей по каждому направлению
    n_length = (wall_length + mortar) // (brick_width + mortar)          # вдоль длины стены
    n_thick = (wall_thickness + mortar) // (brick_length + mortar)       # по толщине стены
    row_height = brick_height + mortar
    n_height = wall_height // row_height                                 # по высоте

    total_bricks = n_length * n_thick * n_height

    # Объёмы
    wall_volume_mm3 = wall_length * wall_thickness * wall_height
    brick_volume_mm3 = brick_length * brick_width * brick_height
    total_bricks_volume_mm3 = total_bricks * brick_volume_mm3
    mortar_volume_mm3 = wall_volume_mm3 - total_bricks_volume_mm3
    mortar_volume_liters = mortar_volume_mm3 / 1_000_000

    trim_info = calculation_of_remains_and_trim(
        brick_length, brick_width, brick_height,
        wall_length, wall_thickness, wall_height,
        mortar, n_length, n_thick, n_height
    )

    return {
        "total_bricks": total_bricks,
        "mortar_volume_mm3": mortar_volume_mm3,
        "mortar_volume_liters": mortar_volume_liters,
        "trim_info": trim_info
    }


def calculation_of_remains_and_trim(
    brick_length: float, brick_width: float, brick_height: float,
    wall_length: float, wall_thickness: float, wall_height: float,
    mortar: float, n_length: int, n_thick: int, n_height: int
) -> Dict[str, Any]:
    """Рассчитывает необходимость подрезки кирпича по трём измерениям.

    Если остаток по какому-либо направлению положителен и **не превышает**
    толщину растворного шва, он может быть заполнен раствором.
    Если остаток больше шва – требуется подрезка всех кирпичей, попадающих
    в соответствующее сечение.

    Args:
        brick_length: Длина кирпича (мм).
        brick_width: Ширина кирпича (мм).
        brick_height: Высота кирпича (мм).
        wall_length: Длина стены (мм).
        wall_thickness: Толщина стены (мм).
        wall_height: Высота стены (мм).
        mortar: Толщина растворного шва (мм).
        n_length: Количество кирпичей по длине.
        n_thick: Количество кирпичей по толщине.
        n_height: Количество кирпичей по высоте.

    Returns:
        Словарь:
            - cut_bricks_total (int): общее количество подрезанных кирпичей.
            - cut_len (int): подрезка из-за остатка по длине.
            - cut_thick (int): подрезка из-за остатка по толщине.
            - cut_height (int): подрезка из-за остатка по высоте.
            - remainders (dict): остатки ('length', 'thickness', 'height') в мм.
            - message (str): текстовое описание для пользователя.
    """
    # Остатки
    remainder_len = wall_length - (n_length * brick_width + (n_length - 1) * mortar)
    remainder_thick = wall_thickness - (n_thick * brick_length + (n_thick - 1) * mortar)
    remainder_height = wall_height - (n_height * brick_height + (n_height - 1) * mortar)

    cut_bricks = 0
    cut_len = 0
    cut_thick = 0
    cut_height = 0
    messages = []

    # Подрезка по длине
    if remainder_len > mortar:
        cut_len = n_thick * n_height
        cut_bricks += cut_len
        messages.append(f"по длине остаток {remainder_len:.1f} мм > {mortar} мм → подрезается {cut_len} шт.")
    elif 0 < remainder_len <= mortar:
        messages.append(f"по длине остаток {remainder_len:.1f} мм ≤ {mortar} мм → заполняется раствором (подрезка не нужна).")

    # Подрезка по толщине
    if remainder_thick > mortar:
        cut_thick = n_length * n_height
        cut_bricks += cut_thick
        messages.append(f"по толщине остаток {remainder_thick:.1f} мм > {mortar} мм → подрезается {cut_thick} шт.")
    elif 0 < remainder_thick <= mortar:
        messages.append(f"по толщине остаток {remainder_thick:.1f} мм ≤ {mortar} мм → заполняется раствором.")

    # Подрезка по высоте
    if remainder_height > mortar:
        cut_height = n_length * n_thick
        cut_bricks += cut_height
        messages.append(f"по высоте остаток {remainder_height:.1f} мм > {mortar} мм → подрезается {cut_height} шт.")
    elif 0 < remainder_height <= mortar:
        messages.append(f"по высоте остаток {remainder_height:.1f} мм ≤ {mortar} мм → заполняется раствором.")

    if cut_bricks == 0:
        full_message = "Подрезка не требуется – все кирпичи целые."
    else:
        full_message = f"Требуется подрезка {cut_bricks} кирпичей.\n    " + "\n    ".join(messages)

    return {
        "cut_bricks_total": cut_bricks,
        "cut_len": cut_len,
        "cut_thick": cut_thick,
        "cut_height": cut_height,
        "remainders": {
            "length": remainder_len,
            "thickness": remainder_thick,
            "height": remainder_height
        },
        "message": full_message
    }