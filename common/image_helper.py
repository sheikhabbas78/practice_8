import os
import re
from werkzeug.datastructures import FileStorage
from flask_uploads import IMAGES, UploadSet
from typing import Union

IMAGE_SET = UploadSet("images", IMAGES)


def save_image(image: FileStorage, folder:str= None, filename: str= None,) -> str:
    return IMAGE_SET.save(image, folder, filename )


def get_path(filename: str, folder: str) -> str:
    return IMAGE_SET.path(filename, folder)


def find_image_any_format(filename: str, folder: str) -> Union['str', 'None']:
    for _format in IMAGES:
        avatar = f'{filename}.{_format}'
        avatar_path = IMAGE_SET.path(filename, folder)
        if os.path.isfile(avatar_path):
            return avatar_path
    return None


def _retreive_filename(file: Union[str, FileStorage]) -> str:
    if isinstance(file, FileStorage):
        return file.filename
    return file


def is_filename_safe(file: Union[str, FileStorage]) ->bool:
    filename = _retreive_filename(file)
    allowed_format = "|".join(IMAGES)
    regex = f"^[a-zA-Z0-9][a-zA-Z0-9_()-\.]*\.({allowed_format})$"
    return re.match(regex, filename) is not None


def get_basename(file: Union[str, FileStorage]) -> str:
    filename = _retreive_filename(file)
    return os.path.split(filename)[1]


def get_extension(file: Union[str, FileStorage]) -> str:
    filename = _retreive_filename(file)
    return os.path.splitext(filename)[1]






