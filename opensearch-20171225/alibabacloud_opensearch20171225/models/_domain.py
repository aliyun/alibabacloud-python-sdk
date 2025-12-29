# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from darabonba.model import DaraModel

class Domain(DaraModel):
    def __init__(
        self,
        category: str = None,
        functions: Dict[str, List[str]] = None,
        name: str = None,
    ):
        self.category = category
        self.functions = functions
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.functions is not None:
            result['functions'] = self.functions

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('functions') is not None:
            self.functions = m.get('functions')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

