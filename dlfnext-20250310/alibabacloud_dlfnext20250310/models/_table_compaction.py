# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TableCompaction(DaraModel):
    def __init__(
        self,
        catalog_id: str = None,
        cu_usage: float = None,
        last_compacted_file_time: int = None,
        max_level_0file_count: str = None,
        table_id: str = None,
    ):
        self.catalog_id = catalog_id
        self.cu_usage = cu_usage
        self.last_compacted_file_time = last_compacted_file_time
        self.max_level_0file_count = max_level_0file_count
        self.table_id = table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_id is not None:
            result['catalogId'] = self.catalog_id

        if self.cu_usage is not None:
            result['cuUsage'] = self.cu_usage

        if self.last_compacted_file_time is not None:
            result['lastCompactedFileTime'] = self.last_compacted_file_time

        if self.max_level_0file_count is not None:
            result['maxLevel0FileCount'] = self.max_level_0file_count

        if self.table_id is not None:
            result['tableId'] = self.table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogId') is not None:
            self.catalog_id = m.get('catalogId')

        if m.get('cuUsage') is not None:
            self.cu_usage = m.get('cuUsage')

        if m.get('lastCompactedFileTime') is not None:
            self.last_compacted_file_time = m.get('lastCompactedFileTime')

        if m.get('maxLevel0FileCount') is not None:
            self.max_level_0file_count = m.get('maxLevel0FileCount')

        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')

        return self

