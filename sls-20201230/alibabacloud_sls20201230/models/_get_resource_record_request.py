# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceRecordRequest(DaraModel):
    def __init__(
        self,
        include_system_records: bool = None,
    ):
        # Specifies whether to allow retrieving system built-in records.
        self.include_system_records = include_system_records

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_system_records is not None:
            result['includeSystemRecords'] = self.include_system_records

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('includeSystemRecords') is not None:
            self.include_system_records = m.get('includeSystemRecords')

        return self

