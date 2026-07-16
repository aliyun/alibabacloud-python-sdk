# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageCroppingRequest(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        target_height: int = None,
        target_width: int = None,
    ):
        # URL of the image to be processed
        # 
        # This parameter is required.
        self.image_url = image_url
        # Target height
        # 
        # This parameter is required.
        self.target_height = target_height
        # Target width
        # 
        # This parameter is required.
        self.target_width = target_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.target_height is not None:
            result['TargetHeight'] = self.target_height

        if self.target_width is not None:
            result['TargetWidth'] = self.target_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('TargetHeight') is not None:
            self.target_height = m.get('TargetHeight')

        if m.get('TargetWidth') is not None:
            self.target_width = m.get('TargetWidth')

        return self

