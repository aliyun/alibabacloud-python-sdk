# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigureResultExportShrinkRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        export_type: str = None,
        oss_info_shrink: str = None,
        region_id: str = None,
        sls_info_shrink: str = None,
    ):
        # The cluster ID.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to view the cluster IDs of all AnalyticDB for MySQL clusters in the destination region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The export type. Valid values:
        # 
        # - SLS: Exports data to SLS.
        # - OSS: Exports data to OSS.
        self.export_type = export_type
        # The OSS configuration information when the export destination is OSS.
        self.oss_info_shrink = oss_info_shrink
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The SLS configuration information when the export destination is SLS.
        self.sls_info_shrink = sls_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.oss_info_shrink is not None:
            result['OssInfo'] = self.oss_info_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sls_info_shrink is not None:
            result['SlsInfo'] = self.sls_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('OssInfo') is not None:
            self.oss_info_shrink = m.get('OssInfo')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlsInfo') is not None:
            self.sls_info_shrink = m.get('SlsInfo')

        return self

