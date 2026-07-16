# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDoctorReportComponentSummaryRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        component_type: str = None,
        date_time: str = None,
        region_id: str = None,
    ):
        # Cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Select component filter type. Values:
        # 
        # - compute
        # 
        # - hive
        # 
        # - hdfs
        # 
        # - yarn
        # 
        # - oss
        # 
        # - hbase
        # 
        # This parameter is required.
        self.component_type = component_type
        # Report date.
        # 
        # This parameter is required.
        self.date_time = date_time
        # Region ID.
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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

