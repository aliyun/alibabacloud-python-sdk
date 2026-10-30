# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeFileSystemsResponseBody(DaraModel):
    def __init__(
        self,
        file_systems: List[main_models.DescribeFileSystemsResponseBodyFileSystems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The collection of file system information.
        self.file_systems = file_systems
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total count.
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
        self.file_systems = []
        if m.get('FileSystems') is not None:
            for k1 in m.get('FileSystems'):
                temp_model = main_models.DescribeFileSystemsResponseBodyFileSystems()
                self.file_systems.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeFileSystemsResponseBodyFileSystems(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        creation_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        file_system_id: str = None,
        file_system_name: str = None,
        metered_size: int = None,
        mount_targets: List[main_models.DescribeFileSystemsResponseBodyFileSystemsMountTargets] = None,
        pay_type: str = None,
        protocol_type: str = None,
        status: str = None,
        storage_type: str = None,
    ):
        # The capacity. Unit: MiB.
        self.capacity = capacity
        # The time when the file system was created.
        self.creation_time = creation_time
        # The description.
        self.description = description
        # The region ID.
        self.ens_region_id = ens_region_id
        # The file system ID.
        self.file_system_id = file_system_id
        # The file system name.
        self.file_system_name = file_system_name
        # The file system usage.
        # Non-real-time usage. It indicates the maximum usage in the previous hour. Unit: bytes.
        self.metered_size = metered_size
        # The collection of mount target information.
        self.mount_targets = mount_targets
        # The billing method. Valid values: PostPaid (pay-as-you-go).
        self.pay_type = pay_type
        # The file system protocol type. Valid values:
        # 
        # - NFS: NFS protocol.
        # - SMB: SMB protocol.
        self.protocol_type = protocol_type
        # The file system status. Valid values:
        # 
        # - pending: The file system is processing a node.
        # - running: The file system is active. You can perform What to do next, such as creating a mount target, only when the status is running.
        # - stopped: The file system is unavailable.
        # - extending: The file system is being expanded.
        # - stopping: The file system is being stopped.
        # - deleting: The file system is being deleted.
        self.status = status
        # The storage type. Valid values:
        # 
        # - capacity: Storage-optimized.
        # - performance: Extreme.
        self.storage_type = storage_type

    def validate(self):
        if self.mount_targets:
            for v1 in self.mount_targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name

        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size

        result['MountTargets'] = []
        if self.mount_targets is not None:
            for k1 in self.mount_targets:
                result['MountTargets'].append(k1.to_map() if k1 else None)

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')

        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')

        self.mount_targets = []
        if m.get('MountTargets') is not None:
            for k1 in m.get('MountTargets'):
                temp_model = main_models.DescribeFileSystemsResponseBodyFileSystemsMountTargets()
                self.mount_targets.append(temp_model.from_map(k1))

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

class DescribeFileSystemsResponseBodyFileSystemsMountTargets(DaraModel):
    def __init__(
        self,
        mount_target_domain: str = None,
        mount_target_name: str = None,
        net_work_id: str = None,
        status: str = None,
    ):
        # The mount target path.
        self.mount_target_domain = mount_target_domain
        # The mount target name.
        self.mount_target_name = mount_target_name
        # The network ID.
        self.net_work_id = net_work_id
        # The mount target status. Valid values:
        # 
        # - active: Available.
        # - inactive: Unavailable.
        # - pending: Processing a task.
        # - deleting: Being deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain

        if self.mount_target_name is not None:
            result['MountTargetName'] = self.mount_target_name

        if self.net_work_id is not None:
            result['NetWorkId'] = self.net_work_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        if m.get('MountTargetName') is not None:
            self.mount_target_name = m.get('MountTargetName')

        if m.get('NetWorkId') is not None:
            self.net_work_id = m.get('NetWorkId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

