# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMetaCategoryShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        owner_ids_shrink: str = None,
        parent_category_id: int = None,
        remark: str = None,
        tid: int = None,
    ):
        self.description = description
        # The name of the category.
        # 
        # This parameter is required.
        self.name = name
        self.owner_ids_shrink = owner_ids_shrink
        # The ID of the parent category. The new category is created under this parent category. If this value is left empty, the new category is of the first level.
        self.parent_category_id = parent_category_id
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
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_ids_shrink is not None:
            result['OwnerIds'] = self.owner_ids_shrink

        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerIds') is not None:
            self.owner_ids_shrink = m.get('OwnerIds')

        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

