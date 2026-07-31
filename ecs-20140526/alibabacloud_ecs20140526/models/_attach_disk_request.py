# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachDiskRequest(DaraModel):
    def __init__(
        self,
        bootable: bool = None,
        delete_with_instance: bool = None,
        device: str = None,
        disk_id: str = None,
        force: bool = None,
        instance_id: str = None,
        key_pair_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to attach the disk as a system disk. Valid values:
        # 
        # - true: The disk is attached as a system disk.
        # 
        # - false: The disk is not attached as a system disk.
        # 
        # Default value: false.
        # 
        # > If you set `Bootable=true`, the destination ECS instance must have no system disk attached.
        self.bootable = bootable
        # Specifies whether to release the disk when the instance is released. Valid values:
        # 
        # - true: The disk is released together with the instance.
        # - false: The disk is not released together with the instance. The disk is retained as a pay-as-you-go data disk.
        # 
        # Default value: false.
        # 
        # Take note of the following items when you set this parameter:
        # 
        # - If you set `DeleteWithInstance` to `false` and the ECS instance is locked for security reasons, meaning that `OperationLocks` contains `"LockReason" : "security"`, this attribute is ignored when the ECS instance is released, and the disk is released together with the instance.
        # 
        # - If the destination disk is an `elastic ephemeral disk`, you must set `DeleteWithInstance` to `true`.
        # 
        # - Disks with the multi-attach feature enabled do not support this parameter.
        self.delete_with_instance = delete_with_instance
        # The device name of the disk.
        # 
        # > This parameter will be deprecated soon. To improve compatibility, use other parameters to identify the disk.
        self.device = device
        # The ID of the disk to be attached. The disk (`DiskId`) and the instance (`InstanceId`) must be in the same zone.
        # 
        # > You can attach data disks and system disks. For related constraints, see the operation description section above.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # Specifies whether to forcefully attach the disk. Valid values:
        # 
        # - true: Forcefully attaches the disk.
        # - false: Does not forcefully attach the disk.
        # 
        # Default value: false.
        # 
        # 
        # > Currently, only regional ESSDs (cloud_regional_disk_auto) support setting this parameter to true.
        self.force = force
        # The ID of the ECS instance to which you want to attach the disk.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the SSH key pair that is bound to the Linux ECS instance when you attach a system disk.
        # 
        # - Windows Server instances: SSH key pairs are not supported. Even if this parameter is specified, only the `Password` configuration takes effect.
        # 
        # - Linux instances: The password logon method is disabled by default.
        self.key_pair_name = key_pair_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password that is set for the instance when you attach a system disk. The password is effective only for the administrator and root usernames and is not effective for other usernames. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported:
        # 
        # ```
        # ()`~!@#$%^&*-_+=|{}[]:;\\"<>,.?/
        # ```
        # For Windows instances, the password cannot start with a forward slash (/).
        # 
        # > If you specify the `Password` parameter, send the request over HTTPS to prevent password leaks.
        self.password = password
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bootable is not None:
            result['Bootable'] = self.bootable

        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.device is not None:
            result['Device'] = self.device

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.force is not None:
            result['Force'] = self.force

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bootable') is not None:
            self.bootable = m.get('Bootable')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

