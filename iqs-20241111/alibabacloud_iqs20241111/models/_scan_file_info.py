# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScanFileInfo(DaraModel):
    def __init__(
        self,
        angle: int = None,
        height: int = None,
        image_base_64: bytes = None,
        width: int = None,
    ):
        self.angle = angle
        self.height = height
        self.image_base_64 = image_base_64
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.angle is not None:
            result['angle'] = self.angle

        if self.height is not None:
            result['height'] = self.height

        if self.image_base_64 is not None:
            result['imageBase64'] = self.image_base_64

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('angle') is not None:
            self.angle = m.get('angle')

        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('imageBase64') is not None:
            self.image_base_64 = m.get('imageBase64')

        if m.get('width') is not None:
            self.width = m.get('width')

        return self

