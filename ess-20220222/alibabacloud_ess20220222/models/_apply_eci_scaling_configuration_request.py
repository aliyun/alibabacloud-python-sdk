# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyEciScalingConfigurationRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        format: str = None,
        region_id: str = None,
        scaling_configuration_id: str = None,
        scaling_group_id: str = None,
    ):
        # The content of the configuration file.
        # 
        # This parameter is required.
        self.content = content
        # Optional. Set the value to YAML.
        self.format = format
        # The region ID.
        self.region_id = region_id
        # The ID of the scaling configuration.
        # 
        # If you want the system to update a scaling configuration of the Elastic Container Instance type based on a YAML configuration file, you must specify `ScalingConfigurationId`. If you do not specify `ScalingConfigurationId`, the system creates a new scaling configuration based on the YAML configuration file.
        self.scaling_configuration_id = scaling_configuration_id
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
        if self.content is not None:
            result['Content'] = self.content

        if self.format is not None:
            result['Format'] = self.format

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

