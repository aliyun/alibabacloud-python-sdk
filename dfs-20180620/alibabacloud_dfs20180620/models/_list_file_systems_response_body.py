# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dfs20180620 import models as main_models
from darabonba.model import DaraModel

class ListFileSystemsResponseBody(DaraModel):
    def __init__(
        self,
        file_systems: List[main_models.ListFileSystemsResponseBodyFileSystems] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.file_systems = file_systems
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.file_systems:
            for v1 in self.file_systems:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileSystems'] = []
        if self.file_systems is not None:
            for k1 in self.file_systems:
                result['FileSystems'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_systems = []
        if m.get('FileSystems') is not None:
            for k1 in m.get('FileSystems'):
                temp_model = main_models.ListFileSystemsResponseBodyFileSystems()
                self.file_systems.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFileSystemsResponseBodyFileSystems(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        file_system_id: str = None,
        file_system_name: str = None,
        metering_space_size: float = None,
        mount_point_count: int = None,
        number_of_directories: int = None,
        number_of_files: int = None,
        protocol_type: str = None,
        provisioned_throughput_in_mi_bps: int = None,
        region_id: str = None,
        space_capacity: int = None,
        storage_package_id: str = None,
        storage_type: str = None,
        throughput_mode: str = None,
        used_space_size: float = None,
        version: str = None,
        zone_id: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.file_system_id = file_system_id
        self.file_system_name = file_system_name
        self.metering_space_size = metering_space_size
        self.mount_point_count = mount_point_count
        self.number_of_directories = number_of_directories
        self.number_of_files = number_of_files
        self.protocol_type = protocol_type
        self.provisioned_throughput_in_mi_bps = provisioned_throughput_in_mi_bps
        self.region_id = region_id
        self.space_capacity = space_capacity
        self.storage_package_id = storage_package_id
        self.storage_type = storage_type
        self.throughput_mode = throughput_mode
        self.used_space_size = used_space_size
        self.version = version
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name

        if self.metering_space_size is not None:
            result['MeteringSpaceSize'] = self.metering_space_size

        if self.mount_point_count is not None:
            result['MountPointCount'] = self.mount_point_count

        if self.number_of_directories is not None:
            result['NumberOfDirectories'] = self.number_of_directories

        if self.number_of_files is not None:
            result['NumberOfFiles'] = self.number_of_files

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.provisioned_throughput_in_mi_bps is not None:
            result['ProvisionedThroughputInMiBps'] = self.provisioned_throughput_in_mi_bps

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.space_capacity is not None:
            result['SpaceCapacity'] = self.space_capacity

        if self.storage_package_id is not None:
            result['StoragePackageId'] = self.storage_package_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.throughput_mode is not None:
            result['ThroughputMode'] = self.throughput_mode

        if self.used_space_size is not None:
            result['UsedSpaceSize'] = self.used_space_size

        if self.version is not None:
            result['Version'] = self.version

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')

        if m.get('MeteringSpaceSize') is not None:
            self.metering_space_size = m.get('MeteringSpaceSize')

        if m.get('MountPointCount') is not None:
            self.mount_point_count = m.get('MountPointCount')

        if m.get('NumberOfDirectories') is not None:
            self.number_of_directories = m.get('NumberOfDirectories')

        if m.get('NumberOfFiles') is not None:
            self.number_of_files = m.get('NumberOfFiles')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('ProvisionedThroughputInMiBps') is not None:
            self.provisioned_throughput_in_mi_bps = m.get('ProvisionedThroughputInMiBps')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SpaceCapacity') is not None:
            self.space_capacity = m.get('SpaceCapacity')

        if m.get('StoragePackageId') is not None:
            self.storage_package_id = m.get('StoragePackageId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('ThroughputMode') is not None:
            self.throughput_mode = m.get('ThroughputMode')

        if m.get('UsedSpaceSize') is not None:
            self.used_space_size = m.get('UsedSpaceSize')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

