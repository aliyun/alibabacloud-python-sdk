# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyFileSystemRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        file_system_name: str = None,
        input_region_id: str = None,
        provisioned_throughput_in_mi_bps: int = None,
        space_capacity: int = None,
        throughput_mode: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.file_system_id = file_system_id
        self.file_system_name = file_system_name
        # This parameter is required.
        self.input_region_id = input_region_id
        self.provisioned_throughput_in_mi_bps = provisioned_throughput_in_mi_bps
        self.space_capacity = space_capacity
        self.throughput_mode = throughput_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.provisioned_throughput_in_mi_bps is not None:
            result['ProvisionedThroughputInMiBps'] = self.provisioned_throughput_in_mi_bps

        if self.space_capacity is not None:
            result['SpaceCapacity'] = self.space_capacity

        if self.throughput_mode is not None:
            result['ThroughputMode'] = self.throughput_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('ProvisionedThroughputInMiBps') is not None:
            self.provisioned_throughput_in_mi_bps = m.get('ProvisionedThroughputInMiBps')

        if m.get('SpaceCapacity') is not None:
            self.space_capacity = m.get('SpaceCapacity')

        if m.get('ThroughputMode') is not None:
            self.throughput_mode = m.get('ThroughputMode')

        return self

