# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AiTryOnRequest(DaraModel):
    def __init__(
        self,
        cloth_image_url: str = None,
        cloth_type: str = None,
        model_image_url: str = None,
        resolution: str = None,
    ):
        # The URL of the clothing image. Only one image is supported. The URL must be a publicly accessible `http`/`https` address. The image must be in JPG, JPEG, PNG, BMP, or WEBP format, with a resolution between 256 × 256 and 2049 × 2049 pixels, and a file size of no more than 10 MB.<br>
        # 
        # This parameter is required.
        self.cloth_image_url = cloth_image_url
        # The clothing type. If specified, the value must be one of the following: tops/bottoms/dresses/tops_and_bottoms/shoes/hats. If not specified, the system automatically identifies the type.
        self.cloth_type = cloth_type
        # The URL of the model image. Only one image is supported. The URL must be a publicly accessible `http`/`https` address. The image must be in JPG, JPEG, PNG, BMP, or WEBP format, with a resolution between 256 × 256 and 2049 × 2049 pixels, and a file size of no more than 10 MB.<br>
        # 
        # This parameter is required.
        self.model_image_url = model_image_url
        # The output image resolution. The synchronous API supports only 1K.
        # 
        # This parameter is required.
        self.resolution = resolution

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloth_image_url is not None:
            result['ClothImageUrl'] = self.cloth_image_url

        if self.cloth_type is not None:
            result['ClothType'] = self.cloth_type

        if self.model_image_url is not None:
            result['ModelImageUrl'] = self.model_image_url

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClothImageUrl') is not None:
            self.cloth_image_url = m.get('ClothImageUrl')

        if m.get('ClothType') is not None:
            self.cloth_type = m.get('ClothType')

        if m.get('ModelImageUrl') is not None:
            self.model_image_url = m.get('ModelImageUrl')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        return self

