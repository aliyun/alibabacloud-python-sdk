# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindResourceControlRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        resource_control_name: str = None,
        target_type: str = None,
        target_value: str = None,
    ):
        # The PolarDB cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The region ID of the PolarDB cluster.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query available regions.
        self.region_id = region_id
        # The name of the resource control rule. The name must be 1 to 63 ASCII bytes in length, start with a letter, and can contain only letters, digits, and underscores.
        # 
        # This parameter is required.
        self.resource_control_name = resource_control_name
        # The type of the binding target. Valid values: USER, DATABASE, QUERY, CONNECTION. The value is case-insensitive.
        # 
        # This parameter is required.
        self.target_type = target_type
        # The value of the binding target. The format depends on the value of TargetType. For more information, see the table below.
        # 
        # This parameter is required.
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_control_name is not None:
            result['ResourceControlName'] = self.resource_control_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceControlName') is not None:
            self.resource_control_name = m.get('ResourceControlName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        return self

