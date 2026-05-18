# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMountPointRequest(DaraModel):
    def __init__(
        self,
        access_group_id: str = None,
        description: str = None,
        file_system_id: str = None,
        input_region_id: str = None,
        network_type: str = None,
        use_performance_mode: bool = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # This parameter is required.
        self.access_group_id = access_group_id
        self.description = description
        # This parameter is required.
        self.file_system_id = file_system_id
        # This parameter is required.
        self.input_region_id = input_region_id
        # This parameter is required.
        self.network_type = network_type
        self.use_performance_mode = use_performance_mode
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.use_performance_mode is not None:
            result['UsePerformanceMode'] = self.use_performance_mode

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('UsePerformanceMode') is not None:
            self.use_performance_mode = m.get('UsePerformanceMode')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

