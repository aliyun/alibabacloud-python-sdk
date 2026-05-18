# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFileSystemRequest(DaraModel):
    def __init__(
        self,
        data_redundancy_type: str = None,
        dedicated_cluster_id: str = None,
        description: str = None,
        file_system_name: str = None,
        input_region_id: str = None,
        partition_number: int = None,
        protocol_type: str = None,
        provisioned_throughput_in_mi_bps: int = None,
        space_capacity: int = None,
        storage_set_name: str = None,
        storage_type: str = None,
        throughput_mode: str = None,
        zone_id: str = None,
    ):
        self.data_redundancy_type = data_redundancy_type
        self.dedicated_cluster_id = dedicated_cluster_id
        self.description = description
        # This parameter is required.
        self.file_system_name = file_system_name
        # This parameter is required.
        self.input_region_id = input_region_id
        self.partition_number = partition_number
        # This parameter is required.
        self.protocol_type = protocol_type
        self.provisioned_throughput_in_mi_bps = provisioned_throughput_in_mi_bps
        # This parameter is required.
        self.space_capacity = space_capacity
        self.storage_set_name = storage_set_name
        # This parameter is required.
        self.storage_type = storage_type
        self.throughput_mode = throughput_mode
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type

        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.partition_number is not None:
            result['PartitionNumber'] = self.partition_number

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.provisioned_throughput_in_mi_bps is not None:
            result['ProvisionedThroughputInMiBps'] = self.provisioned_throughput_in_mi_bps

        if self.space_capacity is not None:
            result['SpaceCapacity'] = self.space_capacity

        if self.storage_set_name is not None:
            result['StorageSetName'] = self.storage_set_name

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.throughput_mode is not None:
            result['ThroughputMode'] = self.throughput_mode

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')

        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('PartitionNumber') is not None:
            self.partition_number = m.get('PartitionNumber')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('ProvisionedThroughputInMiBps') is not None:
            self.provisioned_throughput_in_mi_bps = m.get('ProvisionedThroughputInMiBps')

        if m.get('SpaceCapacity') is not None:
            self.space_capacity = m.get('SpaceCapacity')

        if m.get('StorageSetName') is not None:
            self.storage_set_name = m.get('StorageSetName')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('ThroughputMode') is not None:
            self.throughput_mode = m.get('ThroughputMode')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

