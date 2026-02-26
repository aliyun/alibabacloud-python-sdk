# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Category(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        is_leaf: bool = None,
        level: int = None,
        name: str = None,
        parent_id: int = None,
    ):
        self.category_id = category_id
        self.is_leaf = is_leaf
        self.level = level
        self.name = name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['categoryId'] = self.category_id

        if self.is_leaf is not None:
            result['isLeaf'] = self.is_leaf

        if self.level is not None:
            result['level'] = self.level

        if self.name is not None:
            result['name'] = self.name

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categoryId') is not None:
            self.category_id = m.get('categoryId')

        if m.get('isLeaf') is not None:
            self.is_leaf = m.get('isLeaf')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        return self

