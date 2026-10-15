# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageMattingAsyncRequest(DaraModel):
    def __init__(
        self,
        back_ground_type: str = None,
        bg_color: str = None,
        image_url: str = None,
        target_height: int = None,
        target_width: int = None,
    ):
        # Specifies the background format of the returned image. Valid values:
        # - WHITE_BACKGROUND: Returns an image with a white background.
        # - TRANSPARENT: Returns an image with a transparent background.
        # 
        # This parameter is required.
        self.back_ground_type = back_ground_type
        # The BGR color value of the background. Default value: white.
        self.bg_color = bg_color
        # The URL of the original image. The image must be in JPG, JPEG, PNG, BMP, or WEBP format. The resolution must be between 100 × 100 and 3000 × 3000 pixels, and the file size cannot exceed 10 MB.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The expected height of the cropped image. If you do not specify this parameter, the original height of the image is used. Unit: pixels. Valid values: 100 to 5000.
        self.target_height = target_height
        # The expected width of the cropped image. If you do not specify this parameter, the original width of the image is used. Unit: pixels. Valid values: 100 to 5000.
        self.target_width = target_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.back_ground_type is not None:
            result['BackGroundType'] = self.back_ground_type

        if self.bg_color is not None:
            result['BgColor'] = self.bg_color

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.target_height is not None:
            result['TargetHeight'] = self.target_height

        if self.target_width is not None:
            result['TargetWidth'] = self.target_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackGroundType') is not None:
            self.back_ground_type = m.get('BackGroundType')

        if m.get('BgColor') is not None:
            self.bg_color = m.get('BgColor')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('TargetHeight') is not None:
            self.target_height = m.get('TargetHeight')

        if m.get('TargetWidth') is not None:
            self.target_width = m.get('TargetWidth')

        return self

