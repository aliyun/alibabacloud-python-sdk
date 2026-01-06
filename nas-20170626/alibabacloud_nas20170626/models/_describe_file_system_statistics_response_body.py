# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeFileSystemStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        file_system_statistics: main_models.DescribeFileSystemStatisticsResponseBodyFileSystemStatistics = None,
        file_systems: main_models.DescribeFileSystemStatisticsResponseBodyFileSystems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The statistics of file systems.
        self.file_system_statistics = file_system_statistics
        # The queried file systems.
        self.file_systems = file_systems
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of file system entries.
        self.total_count = total_count

    def validate(self):
        if self.file_system_statistics:
            self.file_system_statistics.validate()
        if self.file_systems:
            self.file_systems.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_statistics is not None:
            result['FileSystemStatistics'] = self.file_system_statistics.to_map()

        if self.file_systems is not None:
            result['FileSystems'] = self.file_systems.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemStatistics') is not None:
            temp_model = main_models.DescribeFileSystemStatisticsResponseBodyFileSystemStatistics()
            self.file_system_statistics = temp_model.from_map(m.get('FileSystemStatistics'))

        if m.get('FileSystems') is not None:
            temp_model = main_models.DescribeFileSystemStatisticsResponseBodyFileSystems()
            self.file_systems = temp_model.from_map(m.get('FileSystems'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeFileSystemStatisticsResponseBodyFileSystems(DaraModel):
    def __init__(
        self,
        file_system: List[main_models.DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystem] = None,
    ):
        self.file_system = file_system

    def validate(self):
        if self.file_system:
            for v1 in self.file_system:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileSystem'] = []
        if self.file_system is not None:
            for k1 in self.file_system:
                result['FileSystem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_system = []
        if m.get('FileSystem') is not None:
            for k1 in m.get('FileSystem'):
                temp_model = main_models.DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystem()
                self.file_system.append(temp_model.from_map(k1))

        return self

class DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystem(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        charge_type: str = None,
        create_time: str = None,
        description: str = None,
        expired_time: str = None,
        file_system_id: str = None,
        file_system_type: str = None,
        metered_iasize: int = None,
        metered_size: int = None,
        packages: main_models.DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackages = None,
        protocol_type: str = None,
        region_id: str = None,
        status: str = None,
        storage_type: str = None,
        zone_id: str = None,
    ):
        # The capacity of the file system.
        # 
        # Unit: GiB.
        self.capacity = capacity
        # The billing method.
        # 
        # Valid values:
        # 
        # *   Subscription: The subscription billing method is used.
        # *   PayAsYouGo: The pay-as-you-go billing method is used.
        # *   Package: A storage plan is attached to the file system.
        self.charge_type = charge_type
        # The time when the NAS file system was created.
        self.create_time = create_time
        # The description of the file system.
        self.description = description
        # The time when the file system expires.
        self.expired_time = expired_time
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: CPFS file system
        self.file_system_type = file_system_type
        # The storage usage of the Infrequent Access (IA) storage medium.
        # 
        # Unit: bytes.
        self.metered_iasize = metered_iasize
        # The storage usage of the file system.
        # 
        # The value of this parameter is the maximum storage usage of the file system over the last hour. Unit: bytes.
        self.metered_size = metered_size
        # The information about storage plans.
        self.packages = packages
        # The protocol type of the file system.
        # 
        # Valid values:
        # 
        # *   NFS: Network File System (NFS)
        # *   SMB: Server Message Block (SMB)
        # *   cpfs: the protocol type supported by the CPFS file system
        self.protocol_type = protocol_type
        # The region ID.
        self.region_id = region_id
        # The status of the file system.
        # 
        # This parameter is returned for Extreme NAS file systems and Cloud Parallel File Storage (CPFS) file systems. Valid values:
        # 
        # *   Pending: The file system is being created or modified.
        # *   Running: The file system is available. Before you create a mount target for the file system, make sure that the file system is in the Running state.
        # *   Stopped: The file system is unavailable.
        # *   Extending: The file system is being scaled out.
        # *   Stopping: The file system is being disabled.
        # *   Deleting: The file system is being deleted.
        self.status = status
        # The storage type.
        # 
        # Valid values:
        # 
        # *   Valid values for General-purpose NAS file systems: Capacity and Performance.
        # *   Valid values for Extreme NAS file systems: standard and advance.
        # *   Valid values for CPFS file systems: advance_100 (100 MB/s/TiB baseline) and advance_200 (200 MB/s/TiB baseline).
        self.storage_type = storage_type
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.packages:
            self.packages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.metered_iasize is not None:
            result['MeteredIASize'] = self.metered_iasize

        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size

        if self.packages is not None:
            result['Packages'] = self.packages.to_map()

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('MeteredIASize') is not None:
            self.metered_iasize = m.get('MeteredIASize')

        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')

        if m.get('Packages') is not None:
            temp_model = main_models.DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackages()
            self.packages = temp_model.from_map(m.get('Packages'))

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackages(DaraModel):
    def __init__(
        self,
        package: List[main_models.DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackagesPackage] = None,
    ):
        self.package = package

    def validate(self):
        if self.package:
            for v1 in self.package:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Package'] = []
        if self.package is not None:
            for k1 in self.package:
                result['Package'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package = []
        if m.get('Package') is not None:
            for k1 in m.get('Package'):
                temp_model = main_models.DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackagesPackage()
                self.package.append(temp_model.from_map(k1))

        return self

class DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackagesPackage(DaraModel):
    def __init__(
        self,
        expired_time: str = None,
        package_id: str = None,
        size: int = None,
        start_time: str = None,
    ):
        # The end time of the validity period for the storage plan.
        self.expired_time = expired_time
        # The ID of the storage plan.
        self.package_id = package_id
        # The capacity of the storage plan.
        self.size = size
        # The start time of the validity period for the storage plan.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.package_id is not None:
            result['PackageId'] = self.package_id

        if self.size is not None:
            result['Size'] = self.size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeFileSystemStatisticsResponseBodyFileSystemStatistics(DaraModel):
    def __init__(
        self,
        file_system_statistic: List[main_models.DescribeFileSystemStatisticsResponseBodyFileSystemStatisticsFileSystemStatistic] = None,
    ):
        self.file_system_statistic = file_system_statistic

    def validate(self):
        if self.file_system_statistic:
            for v1 in self.file_system_statistic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileSystemStatistic'] = []
        if self.file_system_statistic is not None:
            for k1 in self.file_system_statistic:
                result['FileSystemStatistic'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_system_statistic = []
        if m.get('FileSystemStatistic') is not None:
            for k1 in m.get('FileSystemStatistic'):
                temp_model = main_models.DescribeFileSystemStatisticsResponseBodyFileSystemStatisticsFileSystemStatistic()
                self.file_system_statistic.append(temp_model.from_map(k1))

        return self

class DescribeFileSystemStatisticsResponseBodyFileSystemStatisticsFileSystemStatistic(DaraModel):
    def __init__(
        self,
        expired_count: int = None,
        expiring_count: int = None,
        file_system_type: str = None,
        metered_size: int = None,
        total_count: int = None,
    ):
        # The number of expired file systems.
        self.expired_count = expired_count
        # The number of expiring file systems.
        # 
        # File systems whose expiration time is less than or equal to seven days away from the current time are counted.
        self.expiring_count = expiring_count
        # The type of the file system.
        self.file_system_type = file_system_type
        # The storage usage of the file system.
        # 
        # The value of this parameter is the maximum storage usage of the file system over the last hour.
        # 
        # Unit: bytes.
        self.metered_size = metered_size
        # The number of file systems of the current type.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expired_count is not None:
            result['ExpiredCount'] = self.expired_count

        if self.expiring_count is not None:
            result['ExpiringCount'] = self.expiring_count

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredCount') is not None:
            self.expired_count = m.get('ExpiredCount')

        if m.get('ExpiringCount') is not None:
            self.expiring_count = m.get('ExpiringCount')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

