# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDBTaskSQLJobRequest(DaraModel):
    def __init__(
        self,
        dbtask_group_id: int = None,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
    ):
        # The ID of the SQL task group. You can call the [GetStructSyncJobDetail](https://help.aliyun.com/document_detail/206160.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.dbtask_group_id = dbtask_group_id
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the tenant.
        # 
        # > : To view the ID of the tenant, log on to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbtask_group_id is not None:
            result['DBTaskGroupId'] = self.dbtask_group_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBTaskGroupId') is not None:
            self.dbtask_group_id = m.get('DBTaskGroupId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

