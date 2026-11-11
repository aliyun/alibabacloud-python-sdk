# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProductVideoGenerationShrinkRequest(DaraModel):
    def __init__(
        self,
        aspect_ratio: str = None,
        duration: int = None,
        product_images_shrink: str = None,
        product_title: str = None,
        resolution: str = None,
        script: str = None,
    ):
        # The aspect ratio. Default value: 9:16. Valid values: 16:9, 1:1, 3:4, and 9:16.
        self.aspect_ratio = aspect_ratio
        # The video duration in seconds. Default value: 15. If no script is provided, the value must be an integer from 5 to 15. If a script is provided, the value must be an integer from 5 to 30. A value of 15.0 is treated as 15.
        self.duration = duration
        # The public image URLs. At least one image URL is required. Each URL must start with http:// or https:// after leading and trailing whitespaces are removed.
        # 
        # This parameter is required.
        self.product_images_shrink = product_images_shrink
        # The product title. This parameter is required.
        # 
        # This parameter is required.
        self.product_title = product_title
        # The resolution. Default value: 720P. Valid values: 720P and 1080P. The value is case-insensitive and is automatically converted to uppercase by the service.
        self.resolution = resolution
        # The existing storyboard script. If this parameter is not provided or is left blank, automatic planning is used.
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aspect_ratio is not None:
            result['aspect_ratio'] = self.aspect_ratio

        if self.duration is not None:
            result['duration'] = self.duration

        if self.product_images_shrink is not None:
            result['product_images'] = self.product_images_shrink

        if self.product_title is not None:
            result['product_title'] = self.product_title

        if self.resolution is not None:
            result['resolution'] = self.resolution

        if self.script is not None:
            result['script'] = self.script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aspect_ratio') is not None:
            self.aspect_ratio = m.get('aspect_ratio')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('product_images') is not None:
            self.product_images_shrink = m.get('product_images')

        if m.get('product_title') is not None:
            self.product_title = m.get('product_title')

        if m.get('resolution') is not None:
            self.resolution = m.get('resolution')

        if m.get('script') is not None:
            self.script = m.get('script')

        return self

