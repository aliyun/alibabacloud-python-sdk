# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Partition(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        data_size: int = None,
        modify_time: int = None,
        name: str = None,
        record_count: int = None,
        table_id: str = None,
    ):
        self.create_time = create_time
        self.data_size = data_size
        self.modify_time = modify_time
        self.name = name
        self.record_count = record_count
        self.table_id = table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.record_count is not None:
            result['RecordCount'] = self.record_count

        if self.table_id is not None:
            result['TableId'] = self.table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        return self

