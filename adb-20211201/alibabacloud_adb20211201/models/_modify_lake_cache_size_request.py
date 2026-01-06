# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLakeCacheSizeRequest(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        dbcluster_id: str = None,
        enable_lake_cache: bool = None,
    ):
        # The lake cache size that you want to set. Unit: GB.
        self.capacity = capacity
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable the lake cache feature.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is required.
        self.enable_lake_cache = enable_lake_cache

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.enable_lake_cache is not None:
            result['EnableLakeCache'] = self.enable_lake_cache

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EnableLakeCache') is not None:
            self.enable_lake_cache = m.get('EnableLakeCache')

        return self

