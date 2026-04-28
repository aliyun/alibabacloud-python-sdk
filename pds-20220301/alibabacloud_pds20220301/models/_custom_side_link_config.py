# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CustomSideLinkConfig(DaraModel):
    def __init__(
        self,
        icon: str = None,
        link: str = None,
        text: str = None,
    ):
        self.icon = icon
        self.link = link
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icon is not None:
            result['icon'] = self.icon

        if self.link is not None:
            result['link'] = self.link

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('link') is not None:
            self.link = m.get('link')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

