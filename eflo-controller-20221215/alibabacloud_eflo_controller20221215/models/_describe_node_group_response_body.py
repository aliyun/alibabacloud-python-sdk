# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class DescribeNodeGroupResponseBody(DaraModel):
    def __init__(
        self,
        az: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        create_time: str = None,
        file_system_mount_enabled: bool = None,
        image_id: str = None,
        image_name: str = None,
        key_pair_name: str = None,
        login_type: str = None,
        machine_type: str = None,
        node_count: str = None,
        node_group_description: str = None,
        node_group_id: str = None,
        node_group_name: str = None,
        request_id: str = None,
        system_disk: main_models.DescribeNodeGroupResponseBodySystemDisk = None,
        update_time: str = None,
        user_data: str = None,
        virtual_gpu_enabled: bool = None,
    ):
        self.az = az
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.create_time = create_time
        self.file_system_mount_enabled = file_system_mount_enabled
        self.image_id = image_id
        self.image_name = image_name
        self.key_pair_name = key_pair_name
        self.login_type = login_type
        self.machine_type = machine_type
        self.node_count = node_count
        self.node_group_description = node_group_description
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name
        # Id of the request
        self.request_id = request_id
        self.system_disk = system_disk
        self.update_time = update_time
        self.user_data = user_data
        self.virtual_gpu_enabled = virtual_gpu_enabled

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.az is not None:
            result['Az'] = self.az

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.login_type is not None:
            result['LoginType'] = self.login_type

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_group_description is not None:
            result['NodeGroupDescription'] = self.node_group_description

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.virtual_gpu_enabled is not None:
            result['VirtualGpuEnabled'] = self.virtual_gpu_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Az') is not None:
            self.az = m.get('Az')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FileSystemMountEnabled') is not None:
            self.file_system_mount_enabled = m.get('FileSystemMountEnabled')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeGroupDescription') is not None:
            self.node_group_description = m.get('NodeGroupDescription')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.DescribeNodeGroupResponseBodySystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VirtualGpuEnabled') is not None:
            self.virtual_gpu_enabled = m.get('VirtualGpuEnabled')

        return self

class DescribeNodeGroupResponseBodySystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        performance_level: str = None,
        size: int = None,
    ):
        self.category = category
        self.performance_level = performance_level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

