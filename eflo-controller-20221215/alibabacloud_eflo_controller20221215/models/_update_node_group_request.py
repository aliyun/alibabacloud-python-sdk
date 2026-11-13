# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class UpdateNodeGroupRequest(DaraModel):
    def __init__(
        self,
        file_system_mount_enabled: bool = None,
        image_id: str = None,
        key_pair_name: str = None,
        login_password: str = None,
        new_node_group_name: str = None,
        node_group_id: str = None,
        ram_role_name: str = None,
        system_disk: main_models.UpdateNodeGroupRequestSystemDisk = None,
        user_data: str = None,
    ):
        # Specifies whether file storage mounting is supported.
        self.file_system_mount_enabled = file_system_mount_enabled
        # The default image ID of the node group. If this parameter is not specified, the image ID remains unchanged.
        self.image_id = image_id
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The logon password for the machines in the node group.
        self.login_password = login_password
        # The name of the node group.
        self.new_node_group_name = new_node_group_name
        # The ID of the node group.
        self.node_group_id = node_group_id
        # The name of the node RAM role. You can use the RAM API ListRoles to query the node RAM roles that you have created. The trusted entity of the configured role must be Lingjun AI Computing Service.
        # <warning>Submitting an empty string "" clears the RAM role of the node group.</warning>
        self.ram_role_name = ram_role_name
        # The system cloud disk configuration.
        self.system_disk = system_disk
        # The custom executable shell script. The script must be Base64-encoded. The maximum size of the raw data is 16 KB.
        self.user_data = user_data

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.login_password is not None:
            result['LoginPassword'] = self.login_password

        if self.new_node_group_name is not None:
            result['NewNodeGroupName'] = self.new_node_group_name

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemMountEnabled') is not None:
            self.file_system_mount_enabled = m.get('FileSystemMountEnabled')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')

        if m.get('NewNodeGroupName') is not None:
            self.new_node_group_name = m.get('NewNodeGroupName')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.UpdateNodeGroupRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class UpdateNodeGroupRequestSystemDisk(DaraModel):
    def __init__(
        self,
        encrypted: bool = None,
        kmskey_id: str = None,
        performance_level: str = None,
    ):
        # Specifies whether the system cloud disk is encrypted. Valid values:
        # - true: Encrypted.
        # - false: Not encrypted.
        # 
        # Default value: false.
        # 
        # 
        # >Notice: When you use a shared encrypted image to create a cloud disk based on an encrypted snapshot, you must specify the request parameter Encrypted=true for the cloud disk to ensure that the created cloud disk uses the key of the account that shares the image.
        # 
        # > System cloud disk encryption during instance creation is not active in Hong Kong (China) Zone D and Singapore Zone A.
        self.encrypted = encrypted
        # The KMS key ID for the system cloud disk.
        # 
        # If the Encrypted Settings is set to true and KMSKeyId is not specified, the default key is used for encryption, and the KMSKeyId value is returned after the instance is created.
        # - If the cloud disk is created from a non-shared encrypted snapshot: The encryption key used by the snapshot is used by default.
        # - If the cloud disk is created from a shared encrypted snapshot: The service key is used by default.
        # - If the cloud disk is created in a region where account-level default encryption for Block Storage is enabled: The specified account-level key is used by default.
        # - In other cases: The service key is used by default.
        self.kmskey_id = kmskey_id
        # The performance level.
        self.performance_level = performance_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        return self

