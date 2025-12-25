# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MetaCategory(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        create_time: str = None,
        depth: int = None,
        description: str = None,
        name: str = None,
        owner_ids: List[int] = None,
        owner_nick_names: List[str] = None,
        parent_category_id: int = None,
        remark: str = None,
    ):
        self.category_id = category_id
        self.create_time = create_time
        self.depth = depth
        self.description = description
        self.name = name
        self.owner_ids = owner_ids
        self.owner_nick_names = owner_nick_names
        self.parent_category_id = parent_category_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.depth is not None:
            result['Depth'] = self.depth

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids

        if self.owner_nick_names is not None:
            result['OwnerNickNames'] = self.owner_nick_names

        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Depth') is not None:
            self.depth = m.get('Depth')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')

        if m.get('OwnerNickNames') is not None:
            self.owner_nick_names = m.get('OwnerNickNames')

        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

