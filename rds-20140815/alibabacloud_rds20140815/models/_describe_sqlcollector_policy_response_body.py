# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSQLCollectorPolicyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sqlcollector_status: str = None,
        storage_period: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The status of the SQL Explorer (SQL Audit) feature. Valid values:
        # 
        # *   **Enable**
        # *   **Disabled**
        self.sqlcollector_status = sqlcollector_status
        # A reserved parameter.
        self.storage_period = storage_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sqlcollector_status is not None:
            result['SQLCollectorStatus'] = self.sqlcollector_status

        if self.storage_period is not None:
            result['StoragePeriod'] = self.storage_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SQLCollectorStatus') is not None:
            self.sqlcollector_status = m.get('SQLCollectorStatus')

        if m.get('StoragePeriod') is not None:
            self.storage_period = m.get('StoragePeriod')

        return self

