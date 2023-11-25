import types
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


def write_images_to_dir(
    images: Union[list, types.GeneratorType],
    target_path: Union[Path, str],
    n_digits: int = 5,
    start: int = 0,
):
    target_path = Path(target_path)

    for i, image in enumerate(images, start=start):
        output_path = target_path / f"{i}:0{n_digits}"

        cv2.imwrite(str(output_path), image)
