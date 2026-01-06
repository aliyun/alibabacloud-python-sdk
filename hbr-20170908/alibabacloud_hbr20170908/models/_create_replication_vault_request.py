# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateReplicationVaultRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        encrypt_type: str = None,
        kms_key_id: str = None,
        redundancy_type: str = None,
        replication_source_region_id: str = None,
        replication_source_vault_id: str = None,
        vault_name: str = None,
        vault_region_id: str = None,
        vault_storage_class: str = None,
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
        # The data redundancy type of the backup vault. Valid values:
        # 
        # *   LRS: standard locally redundant storage (LRS). Cloud Backup stores the copies of each object on multiple devices of different facilities in the same zone. This way, Cloud Backup ensures data durability and availability even if hardware failures occur.
        # *   ZRS: standard zone-redundant storage (ZRS). Cloud Backup uses the multi-zone mechanism to distribute data across three zones within the same region. If a zone fails, the data that is stored in the other two zones is still accessible.
        self.redundancy_type = redundancy_type
        # The ID of the region where the source vault resides.
        # 
        # This parameter is required.
        self.replication_source_region_id = replication_source_region_id
        # The ID of the source vault.
        # 
        # This parameter is required.
        self.replication_source_vault_id = replication_source_vault_id
        # The name of the backup vault. The name must be 1 to 64 characters in length.
        # 
        # This parameter is required.
        self.vault_name = vault_name
        # The ID of the region where the backup vault resides.
        # 
        # This parameter is required.
        self.vault_region_id = vault_region_id
        # The storage type of the backup vault. Valid value: **STANDARD**, which indicates standard storage.
        self.vault_storage_class = vault_storage_class

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

        if self.redundancy_type is not None:
            result['RedundancyType'] = self.redundancy_type

        if self.replication_source_region_id is not None:
            result['ReplicationSourceRegionId'] = self.replication_source_region_id

        if self.replication_source_vault_id is not None:
            result['ReplicationSourceVaultId'] = self.replication_source_vault_id

        if self.vault_name is not None:
            result['VaultName'] = self.vault_name

        if self.vault_region_id is not None:
            result['VaultRegionId'] = self.vault_region_id

        if self.vault_storage_class is not None:
            result['VaultStorageClass'] = self.vault_storage_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('RedundancyType') is not None:
            self.redundancy_type = m.get('RedundancyType')

        if m.get('ReplicationSourceRegionId') is not None:
            self.replication_source_region_id = m.get('ReplicationSourceRegionId')

        if m.get('ReplicationSourceVaultId') is not None:
            self.replication_source_vault_id = m.get('ReplicationSourceVaultId')

        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')

        if m.get('VaultRegionId') is not None:
            self.vault_region_id = m.get('VaultRegionId')

        if m.get('VaultStorageClass') is not None:
            self.vault_storage_class = m.get('VaultStorageClass')

        return self

