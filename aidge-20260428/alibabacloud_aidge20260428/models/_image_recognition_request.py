# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ImageRecognitionRequest(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        non_object_detect_elements: List[int] = None,
        object_detect_elements: List[int] = None,
        return_border_pixel: int = None,
        return_character: int = None,
        return_character_prop: int = None,
        return_product_num: int = None,
        return_product_prop: int = None,
    ):
        # The URL of the image to recognize.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The list of non-subject element types to detect. Valid values: 1 (background), 2 (border), 3 (watermark), and 4 (collage).
        self.non_object_detect_elements = non_object_detect_elements
        # The list of subject element types to detect. Valid values: 1 (product subject), 2 (model), 3 (text), and 4 (logo).
        self.object_detect_elements = object_detect_elements
        # Specifies whether to return border pixel information. Valid values: 1 (return) and 0 (do not return).
        self.return_border_pixel = return_border_pixel
        # Specifies whether to return text information. Valid values: 1 (return) and 0 (do not return).
        self.return_character = return_character
        # Specifies whether to return text property information. Valid values: 1 (return) and 0 (do not return).
        self.return_character_prop = return_character_prop
        # Specifies whether to return the product count. Valid values: 1 (return) and 0 (do not return).
        self.return_product_num = return_product_num
        # Specifies whether to return product property information. Valid values: 1 (return) and 0 (do not return).
        self.return_product_prop = return_product_prop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.non_object_detect_elements is not None:
            result['NonObjectDetectElements'] = self.non_object_detect_elements

        if self.object_detect_elements is not None:
            result['ObjectDetectElements'] = self.object_detect_elements

        if self.return_border_pixel is not None:
            result['ReturnBorderPixel'] = self.return_border_pixel

        if self.return_character is not None:
            result['ReturnCharacter'] = self.return_character

        if self.return_character_prop is not None:
            result['ReturnCharacterProp'] = self.return_character_prop

        if self.return_product_num is not None:
            result['ReturnProductNum'] = self.return_product_num

        if self.return_product_prop is not None:
            result['ReturnProductProp'] = self.return_product_prop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('NonObjectDetectElements') is not None:
            self.non_object_detect_elements = m.get('NonObjectDetectElements')

        if m.get('ObjectDetectElements') is not None:
            self.object_detect_elements = m.get('ObjectDetectElements')

        if m.get('ReturnBorderPixel') is not None:
            self.return_border_pixel = m.get('ReturnBorderPixel')

        if m.get('ReturnCharacter') is not None:
            self.return_character = m.get('ReturnCharacter')

        if m.get('ReturnCharacterProp') is not None:
            self.return_character_prop = m.get('ReturnCharacterProp')

        if m.get('ReturnProductNum') is not None:
            self.return_product_num = m.get('ReturnProductNum')

        if m.get('ReturnProductProp') is not None:
            self.return_product_prop = m.get('ReturnProductProp')

        return self

