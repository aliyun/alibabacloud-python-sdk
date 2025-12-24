# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ReplaceSystemDiskRequest(DaraModel):
    def __init__(
        self,
        system_disk: main_models.ReplaceSystemDiskRequestSystemDisk = None,
        architecture: str = None,
        arn: List[main_models.ReplaceSystemDiskRequestArn] = None,
        client_token: str = None,
        disk_id: str = None,
        encrypt_algorithm: str = None,
        encrypted: bool = None,
        image_id: str = None,
        instance_id: str = None,
        kmskey_id: str = None,
        key_pair_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        password_inherit: bool = None,
        platform: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_enhancement_strategy: str = None,
        use_additional_service: bool = None,
    ):
        self.system_disk = system_disk
        # >  This parameter is deprecated.
        self.architecture = architecture
        # This parameter is not available for public use.
        self.arn = arn
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but make sure that the token is unique across requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # >  This parameter is deprecated. To improve compatibility, we recommend that you use `ImageId`.
        self.disk_id = disk_id
        # > This parameter is not available for public use.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt the disk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        # 
        # >  When you use a shared encrypted image to create the disk based on an encrypted snapshot, you must set Encrypted to true to ensure that the disk uses an encryption key of your own.
        self.encrypted = encrypted
        # The ID of the image used to replace the system disk. This parameter is required.
        self.image_id = image_id
        # The ID of the instance whose operating system you want to replace.
        # 
        # >  Make sure that the instance is in the `Stopped` (`Stopped`) state.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the KMS key to use for the system disk.
        self.kmskey_id = kmskey_id
        # The name of the key pair.
        # 
        # > This parameter is applicable only to Linux instances. You can bind an SSH key pair to the instance as a logon credential. After you bind the SSH key pair, the username and password logon method is disabled for the instance.
        self.key_pair_name = key_pair_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to reset the password for the instance. The password must be 8 to 30 characters in length and contain at least three of the following items: uppercase letters, lowercase letters, digits, and special characters. Special characters include:
        # 
        #     ()`~!@#$%^&*-_+=|{}[]:;\\"<>,.?/
        # 
        # The passwords of Windows instances cannot start with a forward slash (/).
        # 
        # This parameter is empty by default, which indicates that the current password remains unchanged.
        # 
        # > If you specify `Password`, we recommend that you send requests over HTTPS to prevent password leaks.
        self.password = password
        # Specifies whether to use the preset password of the image.
        # 
        # Default value: false
        # 
        # > If the PasswordInherit parameter is specified, you must leave the Password parameter empty. Before you use this parameter, make sure that a password is preset for the image.
        self.password_inherit = password_inherit
        # >  This parameter is deprecated.
        self.platform = platform
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to use Security Center Basic after the system disk is replaced. Valid values:
        # 
        # *   Active: uses Security Center Basic after the system disk is re-initialized. This value is applicable only to public images.
        # *   Deactive: does not use Security Center Basic after the system disk is re-initialized. This value is applicable to all images.
        # 
        # Default value: Deactive.
        self.security_enhancement_strategy = security_enhancement_strategy
        # Specifies whether to use the system configurations for virtual machines provided by Alibaba Cloud. System configurations for Windows: NTP and KMS. System configurations for Linux: NTP and YUM.
        # 
        # > This parameter takes effect only when you attach a system disk whose device name is /dev/xvda.
        self.use_additional_service = use_additional_service

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()
        if self.arn:
            for v1 in self.arn:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.architecture is not None:
            result['Architecture'] = self.architecture

        result['Arn'] = []
        if self.arn is not None:
            for k1 in self.arn:
                result['Arn'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy

        if self.use_additional_service is not None:
            result['UseAdditionalService'] = self.use_additional_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SystemDisk') is not None:
            temp_model = main_models.ReplaceSystemDiskRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        self.arn = []
        if m.get('Arn') is not None:
            for k1 in m.get('Arn'):
                temp_model = main_models.ReplaceSystemDiskRequestArn()
                self.arn.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')

        if m.get('UseAdditionalService') is not None:
            self.use_additional_service = m.get('UseAdditionalService')

        return self

class ReplaceSystemDiskRequestArn(DaraModel):
    def __init__(
        self,
        assume_role_for: int = None,
        role_type: str = None,
        rolearn: str = None,
    ):
        # > This parameter is unavailable.
        self.assume_role_for = assume_role_for
        # > This parameter is not available for public use.
        self.role_type = role_type
        # > This parameter is not available for public use.
        self.rolearn = rolearn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.rolearn is not None:
            result['Rolearn'] = self.rolearn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Rolearn') is not None:
            self.rolearn = m.get('Rolearn')

        return self

class ReplaceSystemDiskRequestSystemDisk(DaraModel):
    def __init__(
        self,
        size: int = None,
    ):
        # The capacity of the new system disk. Unit: GiB. Valid values:
        # 
        # *   Basic disk: Max{20, Size of the image specified by ImageId} to 500.
        # 
        # *   Enterprise SSD (ESSD):
        # 
        #     *   PL0 ESSD: Max{1, Size of the image specified by ImageId} to 2048.
        #     *   PL1 ESSD: Max{20, Size of the image specified by ImageId} to 2048.
        #     *   PL2 ESSD: Max{461, Size of the image specified by ImageId} to 2048.
        #     *   PL3 ESSD: Max{1261, Size of the image specified by ImageId} to 2048.
        # 
        # *   ESSD AutoPL disk: Max{1, Size of the image specified by ImageId} to 2048.
        # 
        # *   Other disk categories: Max{20, Size of the image specified by ImageId} to 2048.
        # 
        # Default value: Max{40, Size of the image specified by ImageId}.
        # 
        # >  If the capacity of the new system disk exceeds `Max{20, Capacity of the original system disk}`, you are charged for the excess capacity.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

