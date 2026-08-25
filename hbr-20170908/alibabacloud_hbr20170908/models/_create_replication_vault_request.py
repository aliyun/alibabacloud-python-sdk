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
        # The encryption type of the replication target vault. This parameter is valid only when VaultType is set to STANDARD. The encryption type must be the same as that of the source backup repository. Valid values:
        # - **HBR_PRIVATE**: fully managed by Cloud Backup. The built-in secret key encryption method of the backup service is used.
        # - **KMS**: uses a custom key from Alibaba Cloud Key Management Service (KMS) for encryption.
        self.encrypt_type = encrypt_type
        # The custom key or alias from Alibaba Cloud KMS. This parameter is required only when EncryptType is set to KMS.
        self.kms_key_id = kms_key_id
        # The data redundancy storage method of the backup vault. Valid values:
        # 
        # - LRS: locally redundant storage (LRS). The data redundancy storage mechanism is used to store redundant copies of each object on multiple devices across multiple facilities within the same zone, ensuring data durability and availability in the event of hardware failure.
        # - ZRS: zone-redundant storage (ZRS). The multi-zone mechanism is used to distribute user data across three zones in the same region. If one zone becomes unavailable, the data can still be accessed normally.
        self.redundancy_type = redundancy_type
        # The region ID of the source vault.
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
        # The region ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_region_id = vault_region_id
        # The storage class of the backup vault. The value can only be **STANDARD**, which indicates standard storage.
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

