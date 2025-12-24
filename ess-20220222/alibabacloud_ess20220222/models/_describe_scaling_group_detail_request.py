# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeScalingGroupDetailRequest(DaraModel):
    def __init__(
        self,
        output_format: str = None,
        owner_id: int = None,
        region_id: str = None,
        scaling_group_id: str = None,
    ):
        # The output format. Set the value to yaml.
        self.output_format = output_format
        self.owner_id = owner_id
        # The region ID of the scaling group. For more information, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

