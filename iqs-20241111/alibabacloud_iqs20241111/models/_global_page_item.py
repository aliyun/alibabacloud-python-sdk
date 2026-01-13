# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GlobalPageItem(DaraModel):
    def __init__(
        self,
        link: str = None,
        snippet: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.link = link
        self.snippet = snippet
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.link is not None:
            result['link'] = self.link

        if self.snippet is not None:
            result['snippet'] = self.snippet

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('link') is not None:
            self.link = m.get('link')

        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

