# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarFsQuotaRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        path: str = None,
        polar_fs_instance_id: str = None,
        quota_type: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # > To find the cluster ID for enterprise, basic, or data lakehouse edition clusters, call the [DescribeDBClusters](https://help.aliyun.com/document_detail/2319131.html) operation.
        self.dbcluster_id = dbcluster_id
        # The destination path.
        self.path = path
        # The PolarFS instance ID.
        # 
        # This parameter is required.
        self.polar_fs_instance_id = polar_fs_instance_id
        # The quota type to query.
        self.quota_type = quota_type
        # The region ID.
        # 
        # > Call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to find the IDs of all available regions in your account.
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

        if self.path is not None:
            result['Path'] = self.path

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

