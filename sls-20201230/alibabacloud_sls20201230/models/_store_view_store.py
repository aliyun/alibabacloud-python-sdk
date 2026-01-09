# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StoreViewStore(DaraModel):
    def __init__(
        self,
        project: str = None,
        query: str = None,
        store_name: str = None,
    ):
        # This parameter is required.
        self.project = project
        self.query = query
        # This parameter is required.
        self.store_name = store_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project is not None:
            result['project'] = self.project

        if self.query is not None:
            result['query'] = self.query

        if self.store_name is not None:
            result['storeName'] = self.store_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('storeName') is not None:
            self.store_name = m.get('storeName')

        return self

