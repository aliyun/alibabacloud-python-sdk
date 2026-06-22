# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class Illustration(DaraModel):
    def __init__(
        self,
        image_index: int = None,
        image_path: str = None,
        normalized_box: List[float] = None,
        page_number: int = None,
        text: str = None,
        type: str = None,
    ):
        # The zero-based image index in a file that contains multiple images, such as a multi-page TIFF file.
        self.image_index = image_index
        # The path to the image file containing the illustration.
        self.image_path = image_path
        # An array of four floating-point numbers that defines the normalized box for the illustration in [x_min, y_min, x_max, y_max] format. The coordinates are normalized to a range of [0, 1] relative to the page dimensions.
        self.normalized_box = normalized_box
        # The one-based page number where the illustration is located.
        self.page_number = page_number
        # The text associated with the illustration.
        self.text = text
        # The type of the illustration, such as `figure` or `chart`.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_index is not None:
            result['ImageIndex'] = self.image_index

        if self.image_path is not None:
            result['ImagePath'] = self.image_path

        if self.normalized_box is not None:
            result['NormalizedBox'] = self.normalized_box

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIndex') is not None:
            self.image_index = m.get('ImageIndex')

        if m.get('ImagePath') is not None:
            self.image_path = m.get('ImagePath')

        if m.get('NormalizedBox') is not None:
            self.normalized_box = m.get('NormalizedBox')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

