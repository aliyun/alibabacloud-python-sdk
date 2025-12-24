# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEciScalingConfigurationDetailRequest(DaraModel):
    def __init__(
        self,
        output_format: str = None,
        region_id: str = None,
        scaling_configuration_id: str = None,
        scaling_group_id: str = None,
    ):
        # The output format. Set the value to YAML.
        self.output_format = output_format
        # The region ID of the scaling group to which the scaling configuration belongs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the scaling configuration based on which elastic container instances are created.
        # 
        # This parameter is required.
        self.scaling_configuration_id = scaling_configuration_id
        # The ID of the scaling group to which the scaling configuration belongs.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

