# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTableDBTopologyRequest(DaraModel):
    def __init__(
        self,
        table_guid: str = None,
        tid: int = None,
    ):
        # The GUID of the table in DMS.
        # 
        # > 
        # 
        # *   If the database to which the table belongs is a logical database, you can call the [ListLogicTables](https://help.aliyun.com/document_detail/141875.html) operation to obtain the GUID. The value of the ReturnGuid parameter must be set to true.
        # 
        # *   If the database to which the table belongs is a physical database, you can call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to obtain the GUID. The value of the ReturnGuid parameter must be set to true.
        # 
        # This parameter is required.
        self.table_guid = table_guid
        # The ID of the tenant.
        # 
        # > To view the tenant ID, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html).
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

