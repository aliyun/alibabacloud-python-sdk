# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVaultRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        encrypt_type: str = None,
        kms_key_id: str = None,
        replication: bool = None,
        vault_name: str = None,
        vault_region_id: str = None,
        vault_storage_class: str = None,
        vault_type: str = None,
        worm_enabled: bool = None,
    ):
        # The description of the backup vault. The description must be 0 to 255 characters in length.
        self.description = description
        # The method that is used to encrypt the source data. This parameter is valid only if you set the VaultType parameter to STANDARD or OTS_BACKUP. Valid values:
        # 
        # *   **HBR_PRIVATE**: The source data is encrypted by using the built-in encryption method of Hybrid Backup Recovery (HBR).
        # *   **KMS**: The source data is encrypted by using Key Management Service (KMS).
        self.encrypt_type = encrypt_type
        # The customer master key (CMK) created in KMS or the alias of the key. This parameter is required only if you set the EncryptType parameter to KMS.
        self.kms_key_id = kms_key_id
        self.replication = replication
        # The name of the backup vault. The name must be 1 to 64 characters in length.
        # 
        # This parameter is required.
        self.vault_name = vault_name
        # The ID of the region where the backup vault resides.
        # 
        # This parameter is required.
        self.vault_region_id = vault_region_id
        # The storage type of the backup vault.
        # 
        # *   **STANDARD**: standard storage.
        # *   **ARCHIVE**: This parameter is deprecated.
        # *   **COLD_ARCHIVE**: This parameter is deprecated.
        # *   **IA**: This parameter is deprecated.
        self.vault_storage_class = vault_storage_class
        # The type of the backup vault. Valid values:
        # 
        # *   **STANDARD**: standard backup vault
        # *   **OTS_BACKUP**: backup vault for Tablestore
        self.vault_type = vault_type
        # Specifies whether to enable the immutable backup feature.
        self.worm_enabled = worm_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.replication is not None:
            result['Replication'] = self.replication

        if self.vault_name is not None:
            result['VaultName'] = self.vault_name

        if self.vault_region_id is not None:
            result['VaultRegionId'] = self.vault_region_id

        if self.vault_storage_class is not None:
            result['VaultStorageClass'] = self.vault_storage_class

        if self.vault_type is not None:
            result['VaultType'] = self.vault_type

        if self.worm_enabled is not None:
            result['WormEnabled'] = self.worm_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('Replication') is not None:
            self.replication = m.get('Replication')

        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')

        if m.get('VaultRegionId') is not None:
            self.vault_region_id = m.get('VaultRegionId')

        if m.get('VaultStorageClass') is not None:
            self.vault_storage_class = m.get('VaultStorageClass')

        if m.get('VaultType') is not None:
            self.vault_type = m.get('VaultType')

        if m.get('WormEnabled') is not None:
            self.worm_enabled = m.get('WormEnabled')

        return self

