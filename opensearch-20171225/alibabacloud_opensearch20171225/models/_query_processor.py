# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class QueryProcessor(DaraModel):
    def __init__(
        self,
        active: bool = None,
        category: str = None,
        domain: str = None,
        indexes: List[str] = None,
        name: str = None,
        processors: List[Dict[str, Any]] = None,
    ):
        self.active = active
        self.category = category
        self.domain = domain
        self.indexes = indexes
        self.name = name
        self.processors = processors

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['active'] = self.active

        if self.category is not None:
            result['category'] = self.category

        if self.domain is not None:
            result['domain'] = self.domain

        if self.indexes is not None:
            result['indexes'] = self.indexes

        if self.name is not None:
            result['name'] = self.name

        if self.processors is not None:
            result['processors'] = self.processors

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('processors') is not None:
            self.processors = m.get('processors')

        return self

