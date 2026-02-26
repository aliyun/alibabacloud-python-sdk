# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageInsight(DaraModel):
    def __init__(
        self,
        caption: str = None,
        description: str = None,
    ):
        # Image summary.
        # 
        # >  Not supported.
        self.caption = caption
        # The description of the image.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption is not None:
            result['Caption'] = self.caption

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

