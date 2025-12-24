# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReInitDiskRequest(DaraModel):
    def __init__(
        self,
        auto_start_instance: bool = None,
        disk_id: str = None,
        key_pair_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_enhancement_strategy: str = None,
    ):
        # Specifies whether to automatically start the instance after the disk is re-initialized. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.auto_start_instance = auto_start_instance
        # The ID of the disk.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The name of the key pair. This parameter is empty by default.
        # 
        # > The parameter is applicable only to Linux instances. You can bind an SSH key pair to an instance as the logon credential when you re-initialize the system disk of the instance. After the SSH key pair is bound, the username and password-based logon method is disabled for the instance.
        self.key_pair_name = key_pair_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to reset the password of the instance when you re-initialize its system disk. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include:
        # 
        #     ()`~!@#$%^&*-_+=|{}[]:;\\"<>,.?/
        # 
        # For Windows instances, passwords cannot start with a forward slash (/).
        # 
        # > If the `Password` parameter is specified, we recommend that you send requests over HTTPS to prevent password leaks.
        self.password = password
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to use Security Center free of charge after the system disk is re-initialized. Valid values:
        # 
        # *   Active: uses Security Center free of charge after the system disk is re-initialized. This value is applicable to only public images.
        # *   Deactive: does not use Security Center free of charge after the system disk is re-initialized. This value is applicable to all images.
        # 
        # Default value: Deactive.
        self.security_enhancement_strategy = security_enhancement_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_start_instance is not None:
            result['AutoStartInstance'] = self.auto_start_instance

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

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

        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoStartInstance') is not None:
            self.auto_start_instance = m.get('AutoStartInstance')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

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

        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')

        return self

