# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLogicTableRouteConfigRequest(DaraModel):
    def __init__(
        self,
        table_id: int = None,
        tid: int = None,
    ):
        # The ID of the logical table. You can call the [ListLogicTables](https://www.alibabacloud.com/help/en/data-management-service/latest/listlogictables) operation to query the ID of the logical table.
        # 
        # This parameter is required.
        self.table_id = table_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://www.alibabacloud.com/help/en/data-management-service/latest/getuseractivetenant) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

