# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceTDERequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        encryption_key: str = None,
        encryptor_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role_arn: str = None,
        switch_mode: str = None,
        tdestatus: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The ID of the custom key.
        # Custom keys are supported only in the following regions. In other regions, the default key is used for encryption.
        # - Singapore (ap-southeast-1)
        # - Hangzhou (cn-hangzhou)
        # - Shanghai (cn-shanghai)
        # - Beijing (cn-beijing)
        # - Shenzhen (cn-shenzhen)
        # - Hong Kong (China) (cn-hongkong)
        # - Malaysia (ap-southeast-3)
        self.encryption_key = encryption_key
        # The encryption method. Valid values: **aes-256-cbc**.
        # 
        # > This parameter is available only when the **TDEStatus** parameter is set to **enabled**.
        self.encryptor_name = encryptor_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ARN of the specified role. Format: `acs:ram::$accountID:role/$roleName`.
        # > - `$accountID`: the ID of the Alibaba Cloud account. You can view the ID by logging on to the Alibaba Cloud Management Console, moving the pointer over the profile picture in the upper-right corner, and clicking Security Settings.
        # > - `$roleName`: the name of the RAM role. You can view the name by logging on to the Resource Access Management (RAM) console, clicking RAM Roles in the left-side navigation pane, and viewing the RAM role name list.
        self.role_arn = role_arn
        # The time to modify the Transparent Data Encryption (TDE) status of the MongoDB instance. Valid values:
        # 
        # - 0: immediately.
        # 
        # - 1: within the O&M window.
        self.switch_mode = switch_mode
        # The TDE status. Valid values: **enabled**, which indicates that TDE is enabled.
        # > You cannot disable TDE after it is enabled. Proceed with caution.
        # 
        # This parameter is required.
        self.tdestatus = tdestatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryptor_name is not None:
            result['EncryptorName'] = self.encryptor_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptorName') is not None:
            self.encryptor_name = m.get('EncryptorName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')

        return self

