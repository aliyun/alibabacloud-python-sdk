# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIndexesRequest(DaraModel):
    def __init__(
        self,
        logic: bool = None,
        table_id: str = None,
        tid: int = None,
    ):
        # Specifies whether the table is a logical table.
        self.logic = logic
        # The ID of the table.
        # 
        # This parameter is required.
        self.table_id = table_id
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
        if self.logic is not None:
            result['Logic'] = self.logic

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

