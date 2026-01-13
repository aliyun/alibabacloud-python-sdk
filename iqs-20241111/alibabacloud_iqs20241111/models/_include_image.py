# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IncludeImage(DaraModel):
    def __init__(
        self,
        height: int = None,
        image_link: str = None,
        width: int = None,
    ):
        self.height = height
        self.image_link = image_link
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['height'] = self.height

        if self.image_link is not None:
            result['imageLink'] = self.image_link

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('imageLink') is not None:
            self.image_link = m.get('imageLink')

        if m.get('width') is not None:
            self.width = m.get('width')

        return self

