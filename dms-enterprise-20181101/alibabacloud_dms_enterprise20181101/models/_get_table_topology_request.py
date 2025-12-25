# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTableTopologyRequest(DaraModel):
    def __init__(
        self,
        table_guid: str = None,
        tid: int = None,
    ):
        # The GUID of the table in Data Management (DMS).
        # 
        # > 
        # > - You can call the [ListLogicTables](https://help.aliyun.com/document_detail/141875.html) operation with ReturnGuid set to true to query the GUIDs of logical tables in a specific logical database.
        # > - You can call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation with ReturnGuid set to true to query the GUIDs of tables in a specific physical database.
        # 
        # This parameter is required.
        self.table_guid = table_guid
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the DMS console. For more information, see the "View information about the current tenant" section of the [Tenant information](https://help.aliyun.com/document_detail/181330.html) topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

