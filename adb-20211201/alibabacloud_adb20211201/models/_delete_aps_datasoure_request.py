# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteApsDatasoureRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        datasource_id: int = None,
        region_id: str = None,
    ):
        # The ID of the AnalyticDB for MySQL cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The data source ID.
        # 
        # This parameter is required.
        self.datasource_id = datasource_id
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

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

