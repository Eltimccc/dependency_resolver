from fastapi import HTTPException, status

from app.core.config import tasks, builds


def validate_build_request(build: str) -> bool:
    """
    Проверяет валидность запроса по имени билда.
    Имя билда должно быть непустой строкой без пробелов
    и не должно быть числом.
    Поднимает исключение HTTPException с кодом 400 и сообщением об ошибке.
    """
    if build.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Имя билда не должно быть числом.",
        )
    if not isinstance(build, str) or not build.strip() or " " in build:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Неправильное имя билда.",
        )

    return True


def validate_data() -> bool:
    """
    Проверяет наличие данных в tasks и builds.
    Поднимает исключение HTTPException с кодом 500
    и сообщением об ошибке при отсутствии данных.
    """
    if not tasks or not builds:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Данных нет. Проверьте наличие файлов builds.yaml и tasks.yaml.",
        )

    return True


def validate_build_exists(build: str, builds_data: list) -> bool:
    """
    Проверяет существование указанного билда.
    """
    build_names = [bld["name"] for bld in builds_data]

    if build not in build_names:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Указанный билд не найден.",
        )

    return True
