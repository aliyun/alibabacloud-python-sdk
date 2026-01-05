# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPartitionRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        table_id: str = None,
    ):
        # The partition name.
        # 
        # This parameter is required.
        self.name = name
        # The table ID. You can refer to the result returned by the ListTables operation and [Concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # This parameter is required.
        self.table_id = table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.table_id is not None:
            result['TableId'] = self.table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        return self

