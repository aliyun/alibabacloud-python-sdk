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
        # Specifies whether to attach the disk as the system disk. Valid values:
        # 
        # *   true: attaches the disk as the system disk.
        # *   false: does not attach the disk as the system disk.
        # 
        # Default value: false.
        # 
        # >  You can set `Bootable` to true only if the instance does not have a system disk.
        self.bootable = bootable
        # Specifies whether to release the disk when the instance is released. Valid values:
        # 
        # *   true: releases the disk when the instance is released.
        # *   false: does not release the disk when the instance is released. The disk is retained as a pay-as-you-go data disk.
        # 
        # Default value: false.
        # 
        # When you specify this parameter, take note of the following items:
        # 
        # *   If `OperationLocks` in the DescribeInstances response contains `"LockReason" : "security"` for the instance to which the disk is attached, the instance is locked for security reasons. Regardless of whether you set `DeleteWithInstance` to `false`, the DeleteWithInstance setting is ignored, and the disk is released when the instance is released.
        # *   If you want to attach an `elastic ephemeral disk`, you must set `DeleteWithInstance` to `true`.
        # *   You cannot specify DeleteWithInstance for disks for which the multi-attach feature is enabled.
        self.delete_with_instance = delete_with_instance
        # The device name of the disk.
        # 
        # >  This parameter will be removed in the future. We recommend that you use other parameters to ensure future compatibility.
        self.device = device
        # The ID of the disk. The disk specified by `DiskId` and the instance specified by `InstanceId` must reside in the same zone.
        # 
        # >  For information about the limits on attaching a data disk and a system disk, see the "Usage notes" section of this topic.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # Specifies whether to force attach the disk to the instance. Valid values:
        # 
        # *   true: force attaches the disk to the instance.
        # *   false: does not force attach the disk to the instance.
        # 
        # Default value: false.
        # 
        # >  You can set this parameter to true only for Regional Enterprise SSDs (ESSDs) (cloud_regional_disk_auto).
        self.force = force
        # The ID of the instance to which you want to attach the disk.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the SSH key pair that you bind to the Linux instance when you attach the system disk.
        # 
        # *   Windows instances do not support logons based on SSH key pairs. The `Password` parameter takes effect even if the KeyPairName parameter is specified.
        # *   For Linux instances, the username and password-based logon method is disabled by default.
        self.key_pair_name = key_pair_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password that is set when you attach the system disk. The password is applicable only to the administrator and root users. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported:
        # 
        #     ()`~!@#$%^&*-_+=|{}[]:;\\"<>,.?/
        # 
        # For Windows instances, passwords cannot start with a forward slash (/).
        # 
        # > If `Password` is configured, we recommend that you send requests over HTTPS to prevent password leaks.
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

