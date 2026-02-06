# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppInfoRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        status: str = None,
    ):
        # The page number. Default value: **1**.
        self.page_no = page_no
        # The number of entries per page. Default value: **10**. Maximum value: **100**.
        self.page_size = page_size
        # The resource group ID to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The status of the application. You can specify the status of the applications that you want to query. After an application is created, it enters the **Normal** state. Valid values:
        # 
        # *   **Normal**
        # *   **Disable**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

