# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateMetaCategoryRequest(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        description: str = None,
        name: str = None,
        owner_ids: List[int] = None,
        remark: str = None,
        tid: int = None,
    ):
        # The category ID.
        # 
        # This parameter is required.
        self.category_id = category_id
        self.description = description
        # The updated name of the category.
        self.name = name
        self.owner_ids = owner_ids
        self.remark = remark
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

