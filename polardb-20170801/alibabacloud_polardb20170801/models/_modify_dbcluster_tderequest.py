# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterTDERequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        enable_automatic_rotation: str = None,
        encrypt_new_tables: str = None,
        encryption_key: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role_arn: str = None,
        tdestatus: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to allow the TDE key of the cluster to be automatically rotated within the next maintenance window after a lapse of the rotation period when a change in the KMS key version is detected. This parameter is supported only for custom keys. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is supported only for a PolarDB for PostgreSQL or PolarDB for PostgreSQL (Compatible with Oracle) cluster.
        self.enable_automatic_rotation = enable_automatic_rotation
        # Specifies whether to enable automatic encryption for new tables. Valid values:
        # 
        # *   **ON**
        # *   **OFF**
        # 
        # >  This parameter takes effect only for a PolarDB for MySQL cluster.
        self.encrypt_new_tables = encrypt_new_tables
        # The ID of the custom key.
        self.encryption_key = encryption_key
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The Alibaba Cloud Resource Name (ARN) of the RAM role. A RAM role is a virtual identity that you can create within your Alibaba Cloud account. For more information, see [RAM role overview](https://help.aliyun.com/document_detail/93689.html).
        self.role_arn = role_arn
        # Modifies the TDE status. Set the value to **Enable**.
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation

        if self.encrypt_new_tables is not None:
            result['EncryptNewTables'] = self.encrypt_new_tables

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')

        if m.get('EncryptNewTables') is not None:
            self.encrypt_new_tables = m.get('EncryptNewTables')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')

        return self

