# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCostUnitRequest(DaraModel):
    def __init__(
        self,
        owner_uid: int = None,
        page_num: int = None,
        page_size: int = None,
        parent_unit_id: int = None,
    ):
        # The owner of the financial unit.
        # 
        # This parameter is required.
        self.owner_uid = owner_uid
        # The page number.
        self.page_num = page_num
        # The number of entries per page. Maximum value: 300.
        self.page_size = page_size
        # The ID of the parent financial unit. A value of -1 indicates the root of the financial unit tree.
        # 
        # This parameter is required.
        self.parent_unit_id = parent_unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')

        return self

