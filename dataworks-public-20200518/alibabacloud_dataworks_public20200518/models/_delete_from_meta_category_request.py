# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFromMetaCategoryRequest(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        table_guid: str = None,
    ):
        # The ID of the category.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The GUID of the metatable.
        # 
        # This parameter is required.
        self.table_guid = table_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        return self

