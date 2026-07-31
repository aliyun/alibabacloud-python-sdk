# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSQLWebSocketDomainRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        module: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # > Call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) API to query the details of all clusters in your account, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # The application module name.
        # 
        # - `SQLWebSocket`: The module for SQL development.
        # 
        # - `Assistant`: The module for the intelligent assistant.
        self.module = module
        # The region ID.
        # 
        # > Call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) API to query the region IDs supported by AnalyticDB for MySQL.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.module is not None:
            result['Module'] = self.module

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

