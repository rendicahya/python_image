from pathlib import Path
from typing import Union

import cv2
from assertpy.assertpy import assert_that


def load_image_dir(
    path: Union[Path, str], flag: int = cv2.IMREAD_COLOR, sort: bool = False
):
    assert_that(path).is_directory().is_readable()

    path = Path(path)
    supported_formats = (
        ".bmp",
        ".jpeg",
        ".jpg",
        ".png",
        ".tiff",
        ".tif",
        ".gif",
        ".webp",
        ".jp2",
        ".j2k",
        ".pbm",
        ".pgm",
        ".ppm",
        ".sr",
        ".ras",
        ".jpeg2000",
        ".exr",
    )

    for file in (sorted(path) if sort else path).iterdir():
        if not file.is_file or not file.suffix in supported_formats:
            continue

        yield cv2.imread(str(file), flag)
