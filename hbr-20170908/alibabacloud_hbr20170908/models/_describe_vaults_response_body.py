# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeVaultsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        vaults: main_models.DescribeVaultsResponseBodyVaults = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # Page number for pagination, starting from 1. The default value is 1.
        self.page_number = page_number
        # Page size, with a minimum value of 1, a maximum value of 99, and a default value of 10.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Whether the request was successful.
        # - true: Success - false: Failure
        self.success = success
        # Returns the total number of backup repositories.
        self.total_count = total_count
        # The backup vaults.
        self.vaults = vaults

    def validate(self):
        if self.vaults:
            self.vaults.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vaults is not None:
            result['Vaults'] = self.vaults.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Vaults') is not None:
            temp_model = main_models.DescribeVaultsResponseBodyVaults()
            self.vaults = temp_model.from_map(m.get('Vaults'))

        return self

class DescribeVaultsResponseBodyVaults(DaraModel):
    def __init__(
        self,
        vault: List[main_models.DescribeVaultsResponseBodyVaultsVault] = None,
    ):
        self.vault = vault

    def validate(self):
        if self.vault:
            for v1 in self.vault:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Vault'] = []
        if self.vault is not None:
            for k1 in self.vault:
                result['Vault'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vault = []
        if m.get('Vault') is not None:
            for k1 in m.get('Vault'):
                temp_model = main_models.DescribeVaultsResponseBodyVaultsVault()
                self.vault.append(temp_model.from_map(k1))

        return self

class DescribeVaultsResponseBodyVaultsVault(DaraModel):
    def __init__(
        self,
        archive_bytes_done: int = None,
        archive_storage_size: int = None,
        backup_plan_statistics: main_models.DescribeVaultsResponseBodyVaultsVaultBackupPlanStatistics = None,
        bucket_name: str = None,
        bytes_done: int = None,
        charge_type: str = None,
        charged_storage_size: int = None,
        compression_algorithm: str = None,
        created_time: int = None,
        dedup: bool = None,
        description: str = None,
        encrypt_type: str = None,
        index_available: bool = None,
        index_level: str = None,
        index_update_time: int = None,
        kms_key_id: str = None,
        latest_replication_time: int = None,
        redundancy_type: str = None,
        replication: bool = None,
        replication_progress: main_models.DescribeVaultsResponseBodyVaultsVaultReplicationProgress = None,
        replication_source_owner_id: int = None,
        replication_source_region_id: str = None,
        replication_source_vault: bool = None,
        replication_source_vault_id: str = None,
        replication_status: str = None,
        replication_target_owner_id: int = None,
        replication_target_region_id: str = None,
        replication_target_vault_id: str = None,
        resource_group_id: str = None,
        retention: int = None,
        rs_target_account_ids: main_models.DescribeVaultsResponseBodyVaultsVaultRsTargetAccountIds = None,
        search_enabled: bool = None,
        snapshot_count: int = None,
        source_types: main_models.DescribeVaultsResponseBodyVaultsVaultSourceTypes = None,
        status: str = None,
        storage_size: int = None,
        tags: main_models.DescribeVaultsResponseBodyVaultsVaultTags = None,
        trial_info: main_models.DescribeVaultsResponseBodyVaultsVaultTrialInfo = None,
        updated_time: int = None,
        vault_id: str = None,
        vault_name: str = None,
        vault_owner_id: int = None,
        vault_region_id: str = None,
        vault_status_message: str = None,
        vault_storage_class: str = None,
        vault_type: str = None,
        worm_enabled: bool = None,
    ):
        # Archival tier backup data volume. Unit: bytes.
        self.archive_bytes_done = archive_bytes_done
        # The billable storage usage of the Archive tier. Unit: bytes.
        self.archive_storage_size = archive_storage_size
        # The statistics of backup plans that use the backup vault.
        self.backup_plan_statistics = backup_plan_statistics
        # The name of the OSS bucket used by the backup vault.
        self.bucket_name = bucket_name
        # The amount of data that is backed up. Unit: bytes.
        self.bytes_done = bytes_done
        # The billing method of the backup vault.
        self.charge_type = charge_type
        # The billable storage usage of the archive vault. Unit: bytes.
        self.charged_storage_size = charged_storage_size
        # The encryption algorithm used to compress the backup vault. Valid values:
        # 
        # *   DISABLED: The backup vault is not compressed.
        # *   SNAPPY: The backup vault is compressed by using the SNAPPY encryption algorithm.
        # *   ZSTD: The backup vault is compressed by using Zstandard, a fast lossless compression algorithm.
        self.compression_algorithm = compression_algorithm
        # The time when the backup vault was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # Indicates whether the deduplication feature is enabled.
        self.dedup = dedup
        # The description of the backup vault.
        self.description = description
        # The encryption type of the backup vault. Valid values:
        # 
        # *   NONE: The backup vault is not encrypted.
        # *   HBR_PRIVATE (default): The backup vault is encrypted by using a key provided by Cloud Backup.
        # *   KMS: The backup vault is encrypted by using a custom master key (CMK) created in Key Management Service (KMS).
        self.encrypt_type = encrypt_type
        # Indicates whether indexes are available. Indexes are available when they are not being updated.
        self.index_available = index_available
        # The index level.
        # 
        # *   OFF: No indexes are created.
        # *   META: Metadata indexes are created.
        # *   ALL: Full-text indexes are created.
        self.index_level = index_level
        # The time when the index was updated.
        self.index_update_time = index_update_time
        # The ID or alias of the CMK created in KMS. This parameter is returned only when EncryptType is set to KMS.
        self.kms_key_id = kms_key_id
        # The time when the last remote backup was synchronized. The value is a UNIX timestamp. Unit: seconds.
        self.latest_replication_time = latest_replication_time
        # The data redundancy type of the backup vault. Valid values:
        # 
        # *   LRS: Locally redundant storage (LRS) is enabled for the backup vault. Cloud Backup stores the copies of each object on multiple devices of different facilities in the same zone. This way, Cloud Backup ensures data durability and availability even if hardware failures occur.
        # *   ZRS: Zone-redundant storage (ZRS) is enabled for the backup vault. Cloud Backup uses the multi-zone mechanism to distribute data across three zones within the same region. If a zone fails, the data that is stored in the other two zones is still accessible.
        self.redundancy_type = redundancy_type
        # Indicates whether the backup vault is a remote backup vault. Valid values:
        # 
        # *   true: The backup vault is a remote backup vault.
        # *   false: The backup vault is a local backup vault.
        self.replication = replication
        # The progress of data synchronization from the backup vault to the mirror vault.
        self.replication_progress = replication_progress
        self.replication_source_owner_id = replication_source_owner_id
        # The ID of the region in which the source vault resides. This parameter is valid only for remote backup vaults.
        self.replication_source_region_id = replication_source_region_id
        # Indicate whether the backup vault is the source vault that corresponds to the remote backup vault. Valid values:
        # 
        # *   true
        # *   false
        self.replication_source_vault = replication_source_vault
        # The ID of the source vault that corresponds to the remote backup vault.
        self.replication_source_vault_id = replication_source_vault_id
        self.replication_status = replication_status
        self.replication_target_owner_id = replication_target_owner_id
        # Target region for remote backup repository.
        self.replication_target_region_id = replication_target_region_id
        self.replication_target_vault_id = replication_target_vault_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The retention period of the backup vault. Unit: days.
        self.retention = retention
        self.rs_target_account_ids = rs_target_account_ids
        # Indicates whether the backup search feature is enabled.
        self.search_enabled = search_enabled
        # The number of snapshots in the backup vault.
        self.snapshot_count = snapshot_count
        # The data source types of the backup vault.
        self.source_types = source_types
        # The status of the backup vault. Valid values:
        # 
        # *   **UNKNOWN**: The backup vault is in an unknown state.
        # *   **INITIALIZING**: The backup vault is being initialized.
        # *   **CREATED**: The backup vault is created.
        # *   **ERROR**: An error occurs on the backup vault.
        self.status = status
        # The usage of the backup vault. Unit: bytes.
        self.storage_size = storage_size
        # The tags of the backup vault.
        self.tags = tags
        # The free trial information.
        self.trial_info = trial_info
        # The time when the backup vault was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # The ID of the backup vault.
        self.vault_id = vault_id
        # The name of the backup vault.
        self.vault_name = vault_name
        self.vault_owner_id = vault_owner_id
        # The ID of the region in which the backup vault resides.
        self.vault_region_id = vault_region_id
        # The status message that is returned when the backup vault is in the ERROR state. This parameter is valid only for remote backup vaults. Valid values:
        # 
        # *   **UNKNOWN_ERROR**: An unknown error occurs.
        # *   **SOURCE_VAULT_ALREADY_HAS_REPLICATION**: A mirror vault is configured for the source vault.
        self.vault_status_message = vault_status_message
        # The storage class of the backup vault. Valid value: **STANDARD**, which indicates standard storage.
        self.vault_storage_class = vault_storage_class
        # The type of the backup vault. Valid value: **STANDARD**, which indicates a standard backup vault.
        self.vault_type = vault_type
        # Indicates whether the immutable backup feature is enabled.
        self.worm_enabled = worm_enabled

    def validate(self):
        if self.backup_plan_statistics:
            self.backup_plan_statistics.validate()
        if self.replication_progress:
            self.replication_progress.validate()
        if self.rs_target_account_ids:
            self.rs_target_account_ids.validate()
        if self.source_types:
            self.source_types.validate()
        if self.tags:
            self.tags.validate()
        if self.trial_info:
            self.trial_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_bytes_done is not None:
            result['ArchiveBytesDone'] = self.archive_bytes_done

        if self.archive_storage_size is not None:
            result['ArchiveStorageSize'] = self.archive_storage_size

        if self.backup_plan_statistics is not None:
            result['BackupPlanStatistics'] = self.backup_plan_statistics.to_map()

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.charged_storage_size is not None:
            result['ChargedStorageSize'] = self.charged_storage_size

        if self.compression_algorithm is not None:
            result['CompressionAlgorithm'] = self.compression_algorithm

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.dedup is not None:
            result['Dedup'] = self.dedup

        if self.description is not None:
            result['Description'] = self.description

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.index_available is not None:
            result['IndexAvailable'] = self.index_available

        if self.index_level is not None:
            result['IndexLevel'] = self.index_level

        if self.index_update_time is not None:
            result['IndexUpdateTime'] = self.index_update_time

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.latest_replication_time is not None:
            result['LatestReplicationTime'] = self.latest_replication_time

        if self.redundancy_type is not None:
            result['RedundancyType'] = self.redundancy_type

        if self.replication is not None:
            result['Replication'] = self.replication

        if self.replication_progress is not None:
            result['ReplicationProgress'] = self.replication_progress.to_map()

        if self.replication_source_owner_id is not None:
            result['ReplicationSourceOwnerId'] = self.replication_source_owner_id

        if self.replication_source_region_id is not None:
            result['ReplicationSourceRegionId'] = self.replication_source_region_id

        if self.replication_source_vault is not None:
            result['ReplicationSourceVault'] = self.replication_source_vault

        if self.replication_source_vault_id is not None:
            result['ReplicationSourceVaultId'] = self.replication_source_vault_id

        if self.replication_status is not None:
            result['ReplicationStatus'] = self.replication_status

        if self.replication_target_owner_id is not None:
            result['ReplicationTargetOwnerId'] = self.replication_target_owner_id

        if self.replication_target_region_id is not None:
            result['ReplicationTargetRegionId'] = self.replication_target_region_id

        if self.replication_target_vault_id is not None:
            result['ReplicationTargetVaultId'] = self.replication_target_vault_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.rs_target_account_ids is not None:
            result['RsTargetAccountIds'] = self.rs_target_account_ids.to_map()

        if self.search_enabled is not None:
            result['SearchEnabled'] = self.search_enabled

        if self.snapshot_count is not None:
            result['SnapshotCount'] = self.snapshot_count

        if self.source_types is not None:
            result['SourceTypes'] = self.source_types.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.trial_info is not None:
            result['TrialInfo'] = self.trial_info.to_map()

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        if self.vault_name is not None:
            result['VaultName'] = self.vault_name

        if self.vault_owner_id is not None:
            result['VaultOwnerId'] = self.vault_owner_id

        if self.vault_region_id is not None:
            result['VaultRegionId'] = self.vault_region_id

        if self.vault_status_message is not None:
            result['VaultStatusMessage'] = self.vault_status_message

        if self.vault_storage_class is not None:
            result['VaultStorageClass'] = self.vault_storage_class

        if self.vault_type is not None:
            result['VaultType'] = self.vault_type

        if self.worm_enabled is not None:
            result['WormEnabled'] = self.worm_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveBytesDone') is not None:
            self.archive_bytes_done = m.get('ArchiveBytesDone')

        if m.get('ArchiveStorageSize') is not None:
            self.archive_storage_size = m.get('ArchiveStorageSize')

        if m.get('BackupPlanStatistics') is not None:
            temp_model = main_models.DescribeVaultsResponseBodyVaultsVaultBackupPlanStatistics()
            self.backup_plan_statistics = temp_model.from_map(m.get('BackupPlanStatistics'))

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ChargedStorageSize') is not None:
            self.charged_storage_size = m.get('ChargedStorageSize')

        if m.get('CompressionAlgorithm') is not None:
            self.compression_algorithm = m.get('CompressionAlgorithm')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Dedup') is not None:
            self.dedup = m.get('Dedup')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('IndexAvailable') is not None:
            self.index_available = m.get('IndexAvailable')

        if m.get('IndexLevel') is not None:
            self.index_level = m.get('IndexLevel')

        if m.get('IndexUpdateTime') is not None:
            self.index_update_time = m.get('IndexUpdateTime')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('LatestReplicationTime') is not None:
            self.latest_replication_time = m.get('LatestReplicationTime')

        if m.get('RedundancyType') is not None:
            self.redundancy_type = m.get('RedundancyType')

        if m.get('Replication') is not None:
            self.replication = m.get('Replication')

        if m.get('ReplicationProgress') is not None:
            temp_model = main_models.DescribeVaultsResponseBodyVaultsVaultReplicationProgress()
            self.replication_progress = temp_model.from_map(m.get('ReplicationProgress'))

        if m.get('ReplicationSourceOwnerId') is not None:
            self.replication_source_owner_id = m.get('ReplicationSourceOwnerId')

        if m.get('ReplicationSourceRegionId') is not None:
            self.replication_source_region_id = m.get('ReplicationSourceRegionId')

        if m.get('ReplicationSourceVault') is not None:
            self.replication_source_vault = m.get('ReplicationSourceVault')

        if m.get('ReplicationSourceVaultId') is not None:
            self.replication_source_vault_id = m.get('ReplicationSourceVaultId')

        if m.get('ReplicationStatus') is not None:
            self.replication_status = m.get('ReplicationStatus')

        if m.get('ReplicationTargetOwnerId') is not None:
            self.replication_target_owner_id = m.get('ReplicationTargetOwnerId')

        if m.get('ReplicationTargetRegionId') is not None:
            self.replication_target_region_id = m.get('ReplicationTargetRegionId')

        if m.get('ReplicationTargetVaultId') is not None:
            self.replication_target_vault_id = m.get('ReplicationTargetVaultId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('RsTargetAccountIds') is not None:
            temp_model = main_models.DescribeVaultsResponseBodyVaultsVaultRsTargetAccountIds()
            self.rs_target_account_ids = temp_model.from_map(m.get('RsTargetAccountIds'))

        if m.get('SearchEnabled') is not None:
            self.search_enabled = m.get('SearchEnabled')

        if m.get('SnapshotCount') is not None:
            self.snapshot_count = m.get('SnapshotCount')

        if m.get('SourceTypes') is not None:
            temp_model = main_models.DescribeVaultsResponseBodyVaultsVaultSourceTypes()
            self.source_types = temp_model.from_map(m.get('SourceTypes'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeVaultsResponseBodyVaultsVaultTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TrialInfo') is not None:
            temp_model = main_models.DescribeVaultsResponseBodyVaultsVaultTrialInfo()
            self.trial_info = temp_model.from_map(m.get('TrialInfo'))

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')

        if m.get('VaultOwnerId') is not None:
            self.vault_owner_id = m.get('VaultOwnerId')

        if m.get('VaultRegionId') is not None:
            self.vault_region_id = m.get('VaultRegionId')

        if m.get('VaultStatusMessage') is not None:
            self.vault_status_message = m.get('VaultStatusMessage')

        if m.get('VaultStorageClass') is not None:
            self.vault_storage_class = m.get('VaultStorageClass')

        if m.get('VaultType') is not None:
            self.vault_type = m.get('VaultType')

        if m.get('WormEnabled') is not None:
            self.worm_enabled = m.get('WormEnabled')

        return self

class DescribeVaultsResponseBodyVaultsVaultTrialInfo(DaraModel):
    def __init__(
        self,
        keep_after_trial_expiration: bool = None,
        trial_expire_time: int = None,
        trial_start_time: int = None,
        trial_vault_release_time: int = None,
    ):
        # Indicates whether you are billed based on the pay-as-you-go method after the free trial ends.
        self.keep_after_trial_expiration = keep_after_trial_expiration
        # The expiration time of the free trial.
        self.trial_expire_time = trial_expire_time
        # The start time of the free trial.
        self.trial_start_time = trial_start_time
        # The time when the free-trial backup vault is released.
        self.trial_vault_release_time = trial_vault_release_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keep_after_trial_expiration is not None:
            result['KeepAfterTrialExpiration'] = self.keep_after_trial_expiration

        if self.trial_expire_time is not None:
            result['TrialExpireTime'] = self.trial_expire_time

        if self.trial_start_time is not None:
            result['TrialStartTime'] = self.trial_start_time

        if self.trial_vault_release_time is not None:
            result['TrialVaultReleaseTime'] = self.trial_vault_release_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeepAfterTrialExpiration') is not None:
            self.keep_after_trial_expiration = m.get('KeepAfterTrialExpiration')

        if m.get('TrialExpireTime') is not None:
            self.trial_expire_time = m.get('TrialExpireTime')

        if m.get('TrialStartTime') is not None:
            self.trial_start_time = m.get('TrialStartTime')

        if m.get('TrialVaultReleaseTime') is not None:
            self.trial_vault_release_time = m.get('TrialVaultReleaseTime')

        return self

class DescribeVaultsResponseBodyVaultsVaultTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeVaultsResponseBodyVaultsVaultTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeVaultsResponseBodyVaultsVaultTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeVaultsResponseBodyVaultsVaultTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        # *   The tag key cannot be an empty string.
        self.key = key
        # The tag value of the backup vault. Valid values of N: 1 to 20.
        # 
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
        # *   The tag value cannot be an empty string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeVaultsResponseBodyVaultsVaultSourceTypes(DaraModel):
    def __init__(
        self,
        source_type: List[str] = None,
    ):
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

class DescribeVaultsResponseBodyVaultsVaultRsTargetAccountIds(DaraModel):
    def __init__(
        self,
        rs_target_account_id: List[int] = None,
    ):
        self.rs_target_account_id = rs_target_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rs_target_account_id is not None:
            result['RsTargetAccountId'] = self.rs_target_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RsTargetAccountId') is not None:
            self.rs_target_account_id = m.get('RsTargetAccountId')

        return self

class DescribeVaultsResponseBodyVaultsVaultReplicationProgress(DaraModel):
    def __init__(
        self,
        historical_replication_progress: int = None,
        new_replication_progress: int = None,
    ):
        # The progress of historical data synchronization from the backup vault to the mirror vault. Valid values: 0 to 100.
        self.historical_replication_progress = historical_replication_progress
        # The latest synchronization time of incremental data in the mirror vault.
        self.new_replication_progress = new_replication_progress

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.historical_replication_progress is not None:
            result['HistoricalReplicationProgress'] = self.historical_replication_progress

        if self.new_replication_progress is not None:
            result['NewReplicationProgress'] = self.new_replication_progress

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoricalReplicationProgress') is not None:
            self.historical_replication_progress = m.get('HistoricalReplicationProgress')

        if m.get('NewReplicationProgress') is not None:
            self.new_replication_progress = m.get('NewReplicationProgress')

        return self

class DescribeVaultsResponseBodyVaultsVaultBackupPlanStatistics(DaraModel):
    def __init__(
        self,
        archive: int = None,
        common_file_system: int = None,
        common_nas: int = None,
        csg: int = None,
        ecs_file: int = None,
        ecs_hana: int = None,
        isilon: int = None,
        local_file: int = None,
        local_vm: int = None,
        my_sql: int = None,
        nas: int = None,
        oracle: int = None,
        oss: int = None,
        ots: int = None,
        sql_server: int = None,
    ):
        # The number of archive plans.
        self.archive = archive
        # The number of Cloud Parallel File Storage (CPFS) backup plans.
        self.common_file_system = common_file_system
        # The number of backup plans for General-purpose NAS file systems.
        self.common_nas = common_nas
        # The number of backup plans for Cloud Storage Gateway (CSG) gateways.
        self.csg = csg
        # The number of backup plans for ECS files.
        self.ecs_file = ecs_file
        # The number of backup plans for SAP HANA instances.
        self.ecs_hana = ecs_hana
        # The number of backup plans for Isilon storage systems.
        self.isilon = isilon
        # The number of backup plans for on-premises servers.
        self.local_file = local_file
        # The number of backup plans for on-premises virtual machines (VMs).
        self.local_vm = local_vm
        # The number of backup plans for MySQL databases.
        self.my_sql = my_sql
        # The number of backup plans for NAS file systems.
        self.nas = nas
        # The number of backup plans for Oracle databases.
        self.oracle = oracle
        # The number of backup plans for OSS buckets.
        self.oss = oss
        # The number of backup plans for Tablestore instances.
        self.ots = ots
        # The number of backup plans for SQL Server databases.
        self.sql_server = sql_server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive is not None:
            result['Archive'] = self.archive

        if self.common_file_system is not None:
            result['CommonFileSystem'] = self.common_file_system

        if self.common_nas is not None:
            result['CommonNas'] = self.common_nas

        if self.csg is not None:
            result['Csg'] = self.csg

        if self.ecs_file is not None:
            result['EcsFile'] = self.ecs_file

        if self.ecs_hana is not None:
            result['EcsHana'] = self.ecs_hana

        if self.isilon is not None:
            result['Isilon'] = self.isilon

        if self.local_file is not None:
            result['LocalFile'] = self.local_file

        if self.local_vm is not None:
            result['LocalVm'] = self.local_vm

        if self.my_sql is not None:
            result['MySql'] = self.my_sql

        if self.nas is not None:
            result['Nas'] = self.nas

        if self.oracle is not None:
            result['Oracle'] = self.oracle

        if self.oss is not None:
            result['Oss'] = self.oss

        if self.ots is not None:
            result['Ots'] = self.ots

        if self.sql_server is not None:
            result['SqlServer'] = self.sql_server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')

        if m.get('CommonFileSystem') is not None:
            self.common_file_system = m.get('CommonFileSystem')

        if m.get('CommonNas') is not None:
            self.common_nas = m.get('CommonNas')

        if m.get('Csg') is not None:
            self.csg = m.get('Csg')

        if m.get('EcsFile') is not None:
            self.ecs_file = m.get('EcsFile')

        if m.get('EcsHana') is not None:
            self.ecs_hana = m.get('EcsHana')

        if m.get('Isilon') is not None:
            self.isilon = m.get('Isilon')

        if m.get('LocalFile') is not None:
            self.local_file = m.get('LocalFile')

        if m.get('LocalVm') is not None:
            self.local_vm = m.get('LocalVm')

        if m.get('MySql') is not None:
            self.my_sql = m.get('MySql')

        if m.get('Nas') is not None:
            self.nas = m.get('Nas')

        if m.get('Oracle') is not None:
            self.oracle = m.get('Oracle')

        if m.get('Oss') is not None:
            self.oss = m.get('Oss')

        if m.get('Ots') is not None:
            self.ots = m.get('Ots')

        if m.get('SqlServer') is not None:
            self.sql_server = m.get('SqlServer')

        return self

