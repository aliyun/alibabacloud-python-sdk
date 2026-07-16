# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterConfigInXMLRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        dbcluster_id: str = None,
        reason: str = None,
        region_id: str = None,
    ):
        # The configuration parameters to modify. Call the [DescribeDBClusterConfigInXML](https://help.aliyun.com/document_detail/452210.html) operation to query the current configuration parameters. Then, modify the returned parameters.
        # 
        # > When you modify a parameter, you must include all other configuration parameters in the request. If a parameter is not included, it retains its initial value or the modification fails.
        # 
        # This parameter is required.
        self.config = config
        # The cluster ID. Call the [DescribeDBClusters](https://help.aliyun.com/document_detail/170879.html) operation to query the IDs of all clusters in a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The reason for the modification.
        self.reason = reason
        # The region ID. Call the [DescribeRegions](https://help.aliyun.com/document_detail/170875.html) operation to query available region IDs.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

