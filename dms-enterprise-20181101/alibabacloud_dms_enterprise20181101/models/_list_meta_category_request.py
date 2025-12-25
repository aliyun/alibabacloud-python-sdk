# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMetaCategoryRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        parent_category_id: int = None,
        tid: int = None,
    ):
        # The number of the page to return. Pages start from page 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The parent category ID.
        self.parent_category_id = parent_category_id
        # The tenant ID. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

