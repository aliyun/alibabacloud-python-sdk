# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageMattingRequest(DaraModel):
    def __init__(
        self,
        back_ground_type: str = None,
        bg_color: str = None,
        image_url: str = None,
        target_height: int = None,
        target_width: int = None,
    ):
        # The URL of the image to process.
        # 
        # This parameter is required.
        self.back_ground_type = back_ground_type
        # The target image height in pixels.
        self.bg_color = bg_color
        # The URL of the original image. The image must be in JPG, JPEG, PNG, BMP, or WEBP format. The resolution must be between 256 × 256 and 3000 × 3000 pixels. The file size cannot exceed 10 MB.<br>**Example**: `"https://ae01.alicdn.com/kf/S342f0070dc9f4be09a6cbed34e90dc8fs.jpg"`.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The target image width in pixels.
        self.target_height = target_height
        # The background type of the returned image. Valid values:
        # - WHITE_BACKGROUND: white background.
        # - TRANSPARENT: transparent background.
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

