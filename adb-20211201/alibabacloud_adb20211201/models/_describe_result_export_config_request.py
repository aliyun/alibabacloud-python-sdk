# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResultExportConfigRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        export_type: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The export type. Valid values:
        # 
        # *   SLS: Indicates that the export destination is SLS.
        # *   OSS: Indicates that the export destination is OSS.
        self.export_type = export_type
        # The region ID.
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

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

