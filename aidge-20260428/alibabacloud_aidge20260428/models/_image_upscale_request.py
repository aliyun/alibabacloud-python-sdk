# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageUpscaleRequest(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        upscale_factor: int = None,
    ):
        # The URL of the original image. It must be a publicly accessible image URL. Private network addresses such as localhost are not supported. The width and height of the input image must be greater than 100 pixels and less than 3,000 pixels. The width and height of the upscaled image must not exceed 3,000 pixels.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The upscaling factor of the image. Valid values: 2 and 4. Default value: 2.
        self.upscale_factor = upscale_factor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.upscale_factor is not None:
            result['UpscaleFactor'] = self.upscale_factor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('UpscaleFactor') is not None:
            self.upscale_factor = m.get('UpscaleFactor')

        return self

