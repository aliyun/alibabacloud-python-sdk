# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLogstashPluginsRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        page: int = None,
        size: int = None,
        source: str = None,
    ):
        # USER
        self.name = name
        # The ID of the request.
        self.page = page
        # The returned results.
        self.size = size
        # The description of the plug-in.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.page is not None:
            result['page'] = self.page

        if self.size is not None:
            result['size'] = self.size

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

