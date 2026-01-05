# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarSQLCollectorPolicyResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        request_id: str = None,
        sqlcollector_status: str = None,
    ):
        # The IDs of the clusters.
        self.dbcluster_id = dbcluster_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the SQL Explorer feature is enabled. Valid values:
        # 
        # *   **Enable**
        # *   **Disabled**
        self.sqlcollector_status = sqlcollector_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sqlcollector_status is not None:
            result['SQLCollectorStatus'] = self.sqlcollector_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SQLCollectorStatus') is not None:
            self.sqlcollector_status = m.get('SQLCollectorStatus')

        return self

