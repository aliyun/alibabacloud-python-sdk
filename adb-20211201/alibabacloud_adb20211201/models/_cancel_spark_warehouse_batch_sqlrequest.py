# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelSparkWarehouseBatchSQLRequest(DaraModel):
    def __init__(
        self,
        agency: str = None,
        dbcluster_id: str = None,
        query_id: str = None,
    ):
        # The name of the client, which can be up to 16 characters in length. Specify a descriptive name that makes it easy to identify.
        self.agency = agency
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The query ID of the Spark SQL statement.
        # 
        # This parameter is required.
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agency is not None:
            result['Agency'] = self.agency

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agency') is not None:
            self.agency = m.get('Agency')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        return self

