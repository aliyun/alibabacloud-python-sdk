# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetaTableColumnRequest(DaraModel):
    def __init__(
        self,
        table_guid: str = None,
        tid: int = None,
    ):
        # The globally unique identifier (GUID) of the table in Data Management (DMS).
        # 
        # *   If the database to which the table belongs is a logical database, you can call the [ListLogicTables](https://help.aliyun.com/document_detail/141875.html) operation to obtain the value of this parameter.
        # *   If the database to which the table belongs is a physical database, you can call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.table_guid = table_guid
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to obtain the tenant ID.
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

