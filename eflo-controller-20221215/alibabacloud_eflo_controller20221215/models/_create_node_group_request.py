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
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The node ID.
        # 
        # This parameter is required.
        self.node_group = node_group
        # The node information.
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
        # The zone.
        # 
        # This parameter is required.
        self.az = az
        # Specifies whether file storage mounting is supported.
        self.file_system_mount_enabled = file_system_mount_enabled
        # The image ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The password.
        self.login_password = login_password
        # The instance type.
        # 
        # This parameter is required.
        self.machine_type = machine_type
        # The description of the node group.
        self.node_group_description = node_group_description
        # The name of the node group.
        # 
        # This parameter is required.
        self.node_group_name = node_group_name
        # The name of the Resource Access Management (RAM) role for the node. You can call the ListRoles operation of RAM to query the RAM roles that you have created. The trusted entity of the specified role must be Lingjun Intelligent Computing.
        # Note: You cannot clear an existing role.
        self.ram_role_name = ram_role_name
        # The system cloud disk configuration details of the node.
        self.system_disk = system_disk
        # The custom executable shell script. The script must be Base64-encoded. The maximum size of the raw data is 16 KB.
        self.user_data = user_data
        # Specifies whether to enable GPU virtualization splitting.
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
        encrypted: bool = None,
        kmskey_id: str = None,
        performance_level: str = None,
        size: int = None,
    ):
        # The cloud disk type. Valid values:
        # 
        # - cloud_essd: ESSD.
        self.category = category
        # Specifies whether to encrypt the system cloud disk. Valid values:
        # - true: Encrypts the system cloud disk.
        # - false: Does not encrypt the system cloud disk.
        # 
        # Default value: false.
        # 
        # 
        # >Notice: When you use a shared encrypted image to create a cloud disk based on an encrypted snapshot, you must set the Encrypted parameter to true for the cloud disk to ensure that the created cloud disk is encrypted by using the key of the recipient.
        # 
        # > Encrypting the system cloud disk during instance creation is not supported in Zone D of China (Hong Kong) and Zone A of Singapore.
        self.encrypted = encrypted
        # The KMS key ID corresponding to the system cloud disk.
        # 
        # If Encrypted is set to true but KMSKeyId is not specified, the default key is used for encryption, and the KMSKeyId value is returned after the instance is created.
        # - If the cloud disk is created from a non-shared encrypted snapshot, the encryption key used by the snapshot is used by default.
        # - If the cloud disk is created from a shared encrypted snapshot, the service key is used by default.
        # - If the cloud disk is created in a region where account-level default encryption for Elastic Block Storage (EBS) is enabled, the specified account-level key is used by default.
        # - In other cases, the service key is used by default.
        self.kmskey_id = kmskey_id
        # The performance level of the ESSD when it is used as the system cloud disk. Valid values:
        # - PL0: A single disk can deliver up to 10,000 random read/write IOPS.
        # - PL1: A single disk can deliver up to 50,000 random read/write IOPS.
        self.performance_level = performance_level
        # The size. Unit: GB.
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

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

