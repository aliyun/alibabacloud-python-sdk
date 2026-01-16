# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIndexTemplatesRequest(DaraModel):
    def __init__(
        self,
        index_template: str = None,
        page: int = None,
        size: int = None,
    ):
        self.index_template = index_template
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_template is not None:
            result['indexTemplate'] = self.index_template

        if self.page is not None:
            result['page'] = self.page

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('indexTemplate') is not None:
            self.index_template = m.get('indexTemplate')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

