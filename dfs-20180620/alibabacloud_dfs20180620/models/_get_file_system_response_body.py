# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dfs20180620 import models as main_models
from darabonba.model import DaraModel

class GetFileSystemResponseBody(DaraModel):
    def __init__(
        self,
        file_system: main_models.GetFileSystemResponseBodyFileSystem = None,
        request_id: str = None,
    ):
        self.file_system = file_system
        self.request_id = request_id

    def validate(self):
        if self.file_system:
            self.file_system.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system is not None:
            result['FileSystem'] = self.file_system.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystem') is not None:
            temp_model = main_models.GetFileSystemResponseBodyFileSystem()
            self.file_system = temp_model.from_map(m.get('FileSystem'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFileSystemResponseBodyFileSystem(DaraModel):
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

