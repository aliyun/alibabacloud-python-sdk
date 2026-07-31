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
        # The database account name for the cluster.
        # 
        # This parameter is required.
        self.account_name = account_name
        # <props="china">The cluster ID for the Enterprise Edition, Basic Edition, or Data Lakehouse Edition.
        # <props="intl">The cluster ID for the Data Lakehouse Edition.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # If the response is truncated, use the `Marker` value from the response in this field to retrieve the next set of results.
        self.marker = marker
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

