# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FreeResourceItem(DaraModel):
    def __init__(
        self,
        available_number: int = None,
        cluster_id: str = None,
        cluster_name: str = None,
        free_resource_id: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        self.available_number = available_number
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.free_resource_id = free_resource_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time
        self.region_id = region_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_number is not None:
            result['AvailableNumber'] = self.available_number

        if self.cluster_id is not None:
            result['ClusterID'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.free_resource_id is not None:
            result['FreeResourceId'] = self.free_resource_id

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time

        if self.region_id is not None:
            result['RegionID'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableNumber') is not None:
            self.available_number = m.get('AvailableNumber')

        if m.get('ClusterID') is not None:
            self.cluster_id = m.get('ClusterID')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('FreeResourceId') is not None:
            self.free_resource_id = m.get('FreeResourceId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')

        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

