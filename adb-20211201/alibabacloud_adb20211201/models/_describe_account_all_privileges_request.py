# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAccountAllPrivilegesRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dbcluster_id: str = None,
        marker: str = None,
        region_id: str = None,
    ):
        # The name of the database account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies the start position marker from which to return results. If you receive a response indicating that the results are truncated, set this parameter to the value of the `Marker` parameter in the response that you received.
        self.marker = marker
        # The region ID of the cluster.
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
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

