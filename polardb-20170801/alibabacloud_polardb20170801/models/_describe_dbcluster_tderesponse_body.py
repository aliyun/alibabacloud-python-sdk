# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBClusterTDEResponseBody(DaraModel):
    def __init__(
        self,
        automatic_rotation: str = None,
        dbcluster_id: str = None,
        encrypt_new_tables: str = None,
        encryption_key: str = None,
        encryption_key_status: str = None,
        request_id: str = None,
        rotation_interval: str = None,
        tderegion: str = None,
        tdestatus: str = None,
    ):
        # Indicates whether automatic key rotation is allowed. Valid values:
        # 
        # - **Enabled**: Automatic key rotation is allowed.
        # 
        # - **Disabled**: Automatic key rotation is not allowed.
        # 
        # > This parameter is returned only when the database engine is compatible with PostgreSQL or Oracle syntax.
        self.automatic_rotation = automatic_rotation
        # The unique ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # Indicates whether automatic encryption is enabled for all newly created tables. Valid values:
        # 
        # - **ON**: Automatic encryption is enabled.
        # 
        # - **OFF**: Automatic encryption is disabled.
        # 
        # > This parameter is returned only when the database engine is compatible with MySQL.
        self.encrypt_new_tables = encrypt_new_tables
        # The ID of the custom key.
        self.encryption_key = encryption_key
        # The status of the key. Valid values:
        # 
        # - **Enabled**: The key is enabled.
        # 
        # - **Disabled**: The key is disabled.
        self.encryption_key_status = encryption_key_status
        # The unique ID of the request.
        self.request_id = request_id
        # The automatic key rotation interval configured in KMS. If no automatic key rotation interval is set, 0 s is returned. Unit: s.
        # 
        # For example, if the rotation interval is 7 days, 604800 s is returned.
        # 
        # > This parameter is returned only when the database engine is compatible with PostgreSQL or Oracle syntax, and the value of `AutomaticRotation` is `Enabled`.
        self.rotation_interval = rotation_interval
        # The region where the TDE key is located.
        self.tderegion = tderegion
        # Indicates whether TDE encryption is enabled. Valid values:
        # 
        # - **Enabled**: TDE encryption is enabled.
        # 
        # - **Disabled**: TDE encryption is disabled.
        self.tdestatus = tdestatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.encrypt_new_tables is not None:
            result['EncryptNewTables'] = self.encrypt_new_tables

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_key_status is not None:
            result['EncryptionKeyStatus'] = self.encryption_key_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval

        if self.tderegion is not None:
            result['TDERegion'] = self.tderegion

        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EncryptNewTables') is not None:
            self.encrypt_new_tables = m.get('EncryptNewTables')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionKeyStatus') is not None:
            self.encryption_key_status = m.get('EncryptionKeyStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')

        if m.get('TDERegion') is not None:
            self.tderegion = m.get('TDERegion')

        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')

        return self

