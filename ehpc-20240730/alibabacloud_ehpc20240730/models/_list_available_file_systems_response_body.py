# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class ListAvailableFileSystemsResponseBody(DaraModel):
    def __init__(
        self,
        file_system_list: List[main_models.ListAvailableFileSystemsResponseBodyFileSystemList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The file systems.
        self.file_system_list = file_system_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.file_system_list:
            for v1 in self.file_system_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileSystemList'] = []
        if self.file_system_list is not None:
            for k1 in self.file_system_list:
                result['FileSystemList'].append(k1.to_map() if k1 else None)

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
        self.file_system_list = []
        if m.get('FileSystemList') is not None:
            for k1 in m.get('FileSystemList'):
                temp_model = main_models.ListAvailableFileSystemsResponseBodyFileSystemList()
                self.file_system_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAvailableFileSystemsResponseBodyFileSystemList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        file_system_id: str = None,
        file_system_type: str = None,
        mount_target_list: List[main_models.ListAvailableFileSystemsResponseBodyFileSystemListMountTargetList] = None,
        protocol_type: str = None,
        status: str = None,
        storage_type: str = None,
        vpc_id: str = None,
    ):
        # The time when the file system was created.
        self.create_time = create_time
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The type of the file system. Valid values:
        # 
        # *   standard: general-purpose network-attached storage (NAS) file system
        # *   extreme: extreme NAS file system
        self.file_system_type = file_system_type
        # The mount targets of the file system.
        self.mount_target_list = mount_target_list
        # The protocol type of the file system. Valid values:
        # 
        # *   nfs
        # *   smb
        # *   cpfs
        self.protocol_type = protocol_type
        # The state of the file system. Valid values:
        # 
        # *   Pending: The file system is processing a task.
        # *   Running: The file system is available. You can perform subsequent operations, such as creating a mount target, only when the file system is in the Running state.
        # *   Stopped: The file system is unavailable.
        # *   Extending: The file system is being scaled out.
        # *   Stopping: The file system is being stopped.
        # *   Deleting: The file system is being deleted.
        self.status = status
        # The storage type of the file system.
        # 
        # *   Valid values if FileSystemType is set to standard: Capacity and Performance.
        # *   Valid values if FileSystemType is set to extreme: standard and advance.
        self.storage_type = storage_type
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.mount_target_list:
            for v1 in self.mount_target_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        result['MountTargetList'] = []
        if self.mount_target_list is not None:
            for k1 in self.mount_target_list:
                result['MountTargetList'].append(k1.to_map() if k1 else None)

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        self.mount_target_list = []
        if m.get('MountTargetList') is not None:
            for k1 in m.get('MountTargetList'):
                temp_model = main_models.ListAvailableFileSystemsResponseBodyFileSystemListMountTargetList()
                self.mount_target_list.append(temp_model.from_map(k1))

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListAvailableFileSystemsResponseBodyFileSystemListMountTargetList(DaraModel):
    def __init__(
        self,
        mount_target_domain: str = None,
        network_type: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The address of the mount target.
        self.mount_target_domain = mount_target_domain
        # The network type. Valid values: Valid values:
        # 
        # *   vpc
        self.network_type = network_type
        # The state of the mount target. Valid values:
        # 
        # *   Active: The mount target is available.
        # *   Inactive: The mount target is unavailable.
        # *   Pending: The mount target is being mounted.
        # *   Deleting: The mount target is being deleted.
        self.status = status
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

