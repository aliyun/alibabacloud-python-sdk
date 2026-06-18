# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class CreateNodeGroupRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_group: main_models.CreateNodeGroupRequestNodeGroup = None,
        node_unit: Dict[str, Any] = None,
    ):
        # The ID of the cluster to which the node group belongs.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The configurations of the node group.
        # 
        # This parameter is required.
        self.node_group = node_group
        # The configuration of the node unit.
        self.node_unit = node_unit

    def validate(self):
        if self.node_group:
            self.node_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.node_group is not None:
            result['NodeGroup'] = self.node_group.to_map()

        if self.node_unit is not None:
            result['NodeUnit'] = self.node_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NodeGroup') is not None:
            temp_model = main_models.CreateNodeGroupRequestNodeGroup()
            self.node_group = temp_model.from_map(m.get('NodeGroup'))

        if m.get('NodeUnit') is not None:
            self.node_unit = m.get('NodeUnit')

        return self

class CreateNodeGroupRequestNodeGroup(DaraModel):
    def __init__(
        self,
        az: str = None,
        file_system_mount_enabled: bool = None,
        image_id: str = None,
        key_pair_name: str = None,
        login_password: str = None,
        machine_type: str = None,
        node_group_description: str = None,
        node_group_name: str = None,
        ram_role_name: str = None,
        system_disk: main_models.CreateNodeGroupRequestNodeGroupSystemDisk = None,
        user_data: str = None,
        virtual_gpu_enabled: bool = None,
    ):
        # The availability zone of the node group.
        # 
        # This parameter is required.
        self.az = az
        # Specifies whether to enable file system mounting.
        self.file_system_mount_enabled = file_system_mount_enabled
        # The image ID for the nodes.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The name of the key pair for SSH login.
        self.key_pair_name = key_pair_name
        # The password to log in to the nodes.
        self.login_password = login_password
        # The machine type for the nodes.
        # 
        # This parameter is required.
        self.machine_type = machine_type
        # The description of the node group.
        self.node_group_description = node_group_description
        # The name of the node group.
        # 
        # This parameter is required.
        self.node_group_name = node_group_name
        # The name of the RAM role to attach to the nodes. You can call the RAM API `ListRoles` operation to query the RAM roles that you have created. The trust entity of the specified role must be Intelligent Computing Lingjun.<br>**Note:** You cannot detach an existing role by clearing this parameter.<br>
        self.ram_role_name = ram_role_name
        # The system disk configuration for the nodes.
        self.system_disk = system_disk
        # The user data passed to the nodes at launch.
        self.user_data = user_data
        # Specifies whether to enable GPU virtualization.
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

        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.login_password is not None:
            result['LoginPassword'] = self.login_password

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.node_group_description is not None:
            result['NodeGroupDescription'] = self.node_group_description

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.virtual_gpu_enabled is not None:
            result['VirtualGpuEnabled'] = self.virtual_gpu_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Az') is not None:
            self.az = m.get('Az')

        if m.get('FileSystemMountEnabled') is not None:
            self.file_system_mount_enabled = m.get('FileSystemMountEnabled')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('NodeGroupDescription') is not None:
            self.node_group_description = m.get('NodeGroupDescription')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.CreateNodeGroupRequestNodeGroupSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VirtualGpuEnabled') is not None:
            self.virtual_gpu_enabled = m.get('VirtualGpuEnabled')

        return self

class CreateNodeGroupRequestNodeGroupSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        performance_level: str = None,
        size: int = None,
    ):
        # The type of the system disk. Valid values:
        # 
        # - `cloud_essd`: ESSD.
        self.category = category
        # The performance level of the ESSD system disk. Valid values:
        # 
        # - `PL0`: A single disk delivers up to 10,000 random read/write IOPS.
        # 
        # - `PL1`: A single disk delivers up to 50,000 random read/write IOPS.
        self.performance_level = performance_level
        # The size of the system disk, in GB.
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

