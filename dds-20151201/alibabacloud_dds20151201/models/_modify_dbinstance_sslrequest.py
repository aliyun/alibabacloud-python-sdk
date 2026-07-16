# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceSSLRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        force_encryption: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sslaction: str = None,
        switch_mode: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to forcibly enable SSL encryption for connections. Valid values:
        # 
        # - **1**: Forcibly enable SSL encryption.
        # 
        # - **0**: Do not forcibly enable SSL encryption.
        # 
        # > * Forced SSL encryption is supported only for MongoDB 7.0 and 8.0 instances that use cloud disks and meet the following minor engine version requirements:
        # >
        # > * - For version 7.0, the minor engine version must be 8.0.13 or later.
        # >
        # > * - For version 8.0, the minor engine version must be 9.0.5 or later.
        # 
        # >Warning: 
        # 
        # After you enable forced SSL encryption, only SSL connections to the instance are allowed.
        self.force_encryption = force_encryption
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The operation to perform on the SSL feature. Valid values:
        # 
        # - **Open**: Enable SSL encryption.
        # 
        # - **Close**: Disable SSL encryption.
        # 
        # - **Update**: Update the SSL certificate.
        # 
        # This parameter is required.
        self.sslaction = sslaction
        # The time to modify the SSL configuration of the MongoDB instance. Valid values:
        # 
        # - 0: Modify immediately.
        # 
        # - 1: Modify within the maintenance window.
        self.switch_mode = switch_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.force_encryption is not None:
            result['ForceEncryption'] = self.force_encryption

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sslaction is not None:
            result['SSLAction'] = self.sslaction

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ForceEncryption') is not None:
            self.force_encryption = m.get('ForceEncryption')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SSLAction') is not None:
            self.sslaction = m.get('SSLAction')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        return self

