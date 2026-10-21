# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageRecognitionAsyncShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        image_url: str = None,
        non_object_detect_elements_shrink: str = None,
        object_detect_elements_shrink: str = None,
        return_border_pixel: int = None,
        return_character: int = None,
        return_character_prop: int = None,
        return_product_num: int = None,
        return_product_prop: int = None,
    ):
        # The business ID of the caller. It is recorded upon acceptance and returned as is when you query the result of the asynchronous task.
        self.biz_id = biz_id
        # The image URL. The image must be in JPG, JPEG, PNG, BMP, or WEBP format. The resolution must be between 256 × 256 and 3000 × 3000 pixels, and the file size cannot exceed 10 MB.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The types of elements to detect outside the image subject. Valid values:
        # - 1: watermark
        # - 2: logo
        # - 3: text
        # - 4: text-containing color block
        # You can specify multiple values. This parameter and ObjectDetectElements cannot be empty at the same time.
        self.non_object_detect_elements_shrink = non_object_detect_elements_shrink
        # The types of elements to detect on the image subject. Valid values:
        # - 1: watermark
        # - 2: logo
        # - 3: text
        # - 4: text-containing color block
        # You can specify multiple values.
        self.object_detect_elements_shrink = object_detect_elements_shrink
        # Specifies whether to return the marginalization distance of the subject. Valid values:
        # - 1: yes
        # - 0: no
        # Default value: 0.
        self.return_border_pixel = return_border_pixel
        # Specifies whether to return the OCR result of the text in the recognized area. Valid values:
        # - 1: yes
        # - 0: no
        # Default value: 0.
        self.return_character = return_character
        # Specifies whether to return the text proportion. Valid values:
        # - 1: yes
        # - 0: no
        # Default value: 0.
        # This parameter takes effect only when the following two conditions are met:
        # 1. ReturnCharacter is set to 1.
        # 2. ObjectDetectElements or NonObjectDetectElements is set to 3, which means text needs to be recognized.
        self.return_character_prop = return_character_prop
        # Specifies whether to return the number of subjects. Valid values:
        # - 1: yes
        # - 0: no
        # Default value: 0.
        self.return_product_num = return_product_num
        # Specifies whether to return the area proportion of the subject. Valid values:
        # - 1: yes
        # - 0: no
        # Default value: 0.
        self.return_product_prop = return_product_prop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.non_object_detect_elements_shrink is not None:
            result['NonObjectDetectElements'] = self.non_object_detect_elements_shrink

        if self.object_detect_elements_shrink is not None:
            result['ObjectDetectElements'] = self.object_detect_elements_shrink

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
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('NonObjectDetectElements') is not None:
            self.non_object_detect_elements_shrink = m.get('NonObjectDetectElements')

        if m.get('ObjectDetectElements') is not None:
            self.object_detect_elements_shrink = m.get('ObjectDetectElements')

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

