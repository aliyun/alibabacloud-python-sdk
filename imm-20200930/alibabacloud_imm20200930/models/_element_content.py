# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ElementContent(DaraModel):
    def __init__(
        self,
        content: str = None,
        time_range: List[int] = None,
        type: str = None,
        url: str = None,
    ):
        # The content of the element.
        # 
        # If the value of the Type parameter is image or link, this parameter indicates the placeholder text.
        self.content = content
        # The time range. The array length is fixed to 2. One element indicates the start time and the other one indicates the end time. Unit: milliseconds.
        self.time_range = time_range
        # The type of the element content.
        # 
        # Valid values:
        # 
        # *   text
        # *   image
        # *   link
        self.type = type
        # The link to the element content. This parameter takes effect only if the Type parameter is set to image or link.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.time_range is not None:
            result['TimeRange'] = self.time_range

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

