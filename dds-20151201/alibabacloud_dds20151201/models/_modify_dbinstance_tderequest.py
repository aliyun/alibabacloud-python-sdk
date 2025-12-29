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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The ID of the custom key.
        self.encryption_key = encryption_key
        # The encryption method. Set the value to **aes-256-cbc**.
        # 
        # > This parameter is valid only when the **TEDStatus** parameter is set to **enabled**.
        self.encryptor_name = encryptor_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The Alibaba Cloud Resource Name (ARN) of the specified Resource Access Management (RAM) role. The ARN is displayed in the `acs:ram::$accountID:role/$roleName` format.
        # 
        # > *   `$accountID`: specifies the ID of the Alibaba Cloud account. To view the account ID, log on to the Alibaba Cloud Management Console, move your pointer over your profile picture in the upper-right corner, and then click Security Settings.
        # 
        # > *   `$roleName`: specifies the name of the RAM role. To view the RAM role name, log on to the RAM console. In the left-side navigation pane, choose Identities > Roles. On the Roles page, view the name of the RAM role.
        self.role_arn = role_arn
        self.switch_mode = switch_mode
        # The TDE status. When the value of this parameter is set to **Enabled**, TDE is enabled.
        # 
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

