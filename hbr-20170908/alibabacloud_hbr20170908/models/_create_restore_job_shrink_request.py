# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRestoreJobShrinkRequest(DaraModel):
    def __init__(
        self,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        edition: str = None,
        exclude: str = None,
        failback_detail_shrink: str = None,
        include: str = None,
        initiated_by_ack: bool = None,
        options: str = None,
        ots_detail_shrink: str = None,
        restore_type: str = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        source_type: str = None,
        target_bucket: str = None,
        target_container: str = None,
        target_container_cluster_id: str = None,
        target_create_time: int = None,
        target_file_system_id: str = None,
        target_instance_id: str = None,
        target_instance_name: str = None,
        target_path: str = None,
        target_prefix: str = None,
        target_table_name: str = None,
        target_time: int = None,
        udm_detail_shrink: str = None,
        udm_region_id: str = None,
        vault_id: str = None,
    ):
        # The name of the RAM role created in the source account for cross-account backup managed by the current account.
        self.cross_account_role_name = cross_account_role_name
        # The cross-account backup type. Valid values: 
        # - SELF_ACCOUNT: backup within the current account.
        # - CROSS_ACCOUNT: cross-account backup.
        self.cross_account_type = cross_account_type
        # The ID of the source account for cross-account backup managed by the current account.
        self.cross_account_user_id = cross_account_user_id
        # The Cloud Backup feature edition. Valid values:
        # - **STANDARD**: Standard Edition. This is the default value.
        # - **BASIC**: Essential Edition. Currently, only ECS File Backup Essential Edition is supported.
        self.edition = edition
        # The path to exclude from restoration. All files under this path are not restored. Maximum length: 255 characters.
        self.exclude = exclude
        # The details of the restoration to the local host.
        self.failback_detail_shrink = failback_detail_shrink
        # The path to restore. All files under this path are restored. Maximum length: 255 characters.
        self.include = include
        # Specifies whether the operation is invoked by Container Service. Default value: false.
        self.initiated_by_ack = initiated_by_ack
        # The restore job parameters.
        self.options = options
        # The details of the Tablestore instance.
        self.ots_detail_shrink = ots_detail_shrink
        # The data source type of the restore destination. Valid values:
        #   - **ECS_FILE**: restores to an ECS file.
        #   - **OSS**: restores to Alibaba Cloud OSS.
        #   - **NAS**: restores to Alibaba Cloud NAS.
        #   - **COMMON_FILE_SYSTEM**: restores to CPFS.
        #   - **OTS_TABLE**: restores to Alibaba Cloud OTS.
        #   - **UDM_ECS_ROLLBACK**: restores to an Alibaba Cloud ECS instance (full-copy migration).
        # 
        # This parameter is required.
        self.restore_type = restore_type
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id
        # The data source type. Valid values:
        #   - **ECS_FILE**: restores ECS files.
        #   - **OSS**: restores Alibaba Cloud OSS.
        #   - **NAS**: restores Alibaba Cloud NAS.
        #   - **COMMON_FILE_SYSTEM**: restores to CPFS.
        #   - **OTS_TABLE**: restores to Alibaba Cloud OTS.
        #   - **UDM_ECS**: restores to an Alibaba Cloud ECS instance (full-copy migration).
        # 
        # This parameter is required.
        self.source_type = source_type
        # This parameter is valid only when **RestoreType** is set to **OSS**. The name of the destination OSS bucket.
        self.target_bucket = target_bucket
        # The details of the target container for restoration.
        self.target_container = target_container
        # The ID of the target container cluster for restoration.
        self.target_container_cluster_id = target_container_cluster_id
        # This parameter is valid only when **RestoreType** is set to **NAS**. The creation time of the destination file system. This value is a UNIX timestamp. Unit: seconds.
        self.target_create_time = target_create_time
        # This parameter is valid only when **RestoreType** is set to **NAS**. The file system ID of the restore destination.
        self.target_file_system_id = target_file_system_id
        # This parameter is valid only when **RestoreType** is set to **ECS_FILE**. The ECS instance ID of the restore destination.
        self.target_instance_id = target_instance_id
        # The name of the target Tablestore instance for restoration.
        self.target_instance_name = target_instance_name
        # This parameter is valid only when **RestoreType** is set to **ECS_FILE**. The file path of the restore destination.
        self.target_path = target_path
        # This parameter is valid only when **RestoreType** is set to **OSS**. The object prefix of the restore destination.
        self.target_prefix = target_prefix
        # The name of the target data table in Tablestore for restoration.
        self.target_table_name = target_table_name
        # The point in time to which the Tablestore data is restored. This value is a UNIX timestamp. Unit: seconds.
        self.target_time = target_time
        # This parameter is valid only when SourceType is set to UDM_ECS. The details of the full-copy migration backup. This parameter is a JSON string. The details vary depending on the value of RestoreType:
        # - **UDM_ECS_DISK**: ECS cloud disk clone.
        #   - **targetInstanceId**: string type, required. Instance ID of the target ECS instance to which the cloned cloud disk is attached.
        #   - **diskCategory**: string type, required. The type of the target cloud disk.
        #   - **diskPerformanceLevel**: string type. If diskCategory is set to essd, this parameter specifies the performance level (PL) of the cloud disk. Valid values: PL0, PL1, PL2, and PL3. Default value: PL1.
        # - **UDM_ECS_DISK_ROLLBACK**: ECS cloud disk restoration.
        #   - **sourceInstanceId**: string type, required. Instance ID of the source ECS instance.
        #   - **foreceRestore**: bool type. Default value: false. Specifies whether to forcibly restore. If foreceRestore is set to true, the restore job still restores the cloud disk even if the backed-up cloud disk has been unmounted from the original ECS instance or attached to a new ECS instance. Proceed with caution.
        #   - **bootAfterRestore**: bool type. Default value: false. Specifies whether to start the ECS instance after restoration.
        # - **UDM_ECS**: ECS full-copy clone.
        #   - **bootAfterRestore**: bool type. Default value: false. Specifies whether to start the ECS instance after restoration.
        #   - **diskCategory**: string type, required. The type of the target cloud disk.
        #   - **diskPerformanceLevel**: string type. If diskCategory is set to essd, this parameter specifies the performance level (PL) of the cloud disk. Valid values: PL0, PL1, PL2, and PL3. Default value: PL1.
        #   - **instanceType**: string type, required. The instance type of the target ECS instance.
        #   - **restoredNetwork**: string type, required. The vSwitch ID of the target ECS instance.
        #   - **securityGroup**: string type, required. The security group ID of the target ECS instance.
        #   - **restoredName**: string type, required. The instance name of the target ECS instance.
        #   - **restoredHostName**: string type, required. The hostname of the target ECS instance.
        #   - **allocatePublicIp**: bool type. Default value: false. Specifies whether to assign a public IP address to the target ECS instance.
        #   - **privateIpAddress**: string type. The internal IP address of the target ECS instance. If this parameter is not specified, DHCP is used to randomly assign an IP address.
        # - **UDM_ECS_ROLLBACK**: ECS full-copy restoration.
        #   - **sourceInstanceId**: string type, required. Instance ID of the source ECS instance.
        #   - **forceRestore**: bool type. Default value: false. Specifies whether to forcibly restore. If foreceRestore is set to true, the restore job still restores the cloud disk even if the backed-up cloud disk has been unmounted from the original ECS instance or attached to a new ECS instance. Proceed with caution.
        #   - **bootAfterRestore**: bool type. Default value: false. Specifies whether to start the ECS instance after restoration.
        self.udm_detail_shrink = udm_detail_shrink
        # This parameter is valid only when **SourceType** is set to **UDM_ECS**. The destination region for restoration.
        self.udm_region_id = udm_region_id
        # The ID of the backup vault to which the backup snapshot belongs.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.failback_detail_shrink is not None:
            result['FailbackDetail'] = self.failback_detail_shrink

        if self.include is not None:
            result['Include'] = self.include

        if self.initiated_by_ack is not None:
            result['InitiatedByAck'] = self.initiated_by_ack

        if self.options is not None:
            result['Options'] = self.options

        if self.ots_detail_shrink is not None:
            result['OtsDetail'] = self.ots_detail_shrink

        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type

        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.target_bucket is not None:
            result['TargetBucket'] = self.target_bucket

        if self.target_container is not None:
            result['TargetContainer'] = self.target_container

        if self.target_container_cluster_id is not None:
            result['TargetContainerClusterId'] = self.target_container_cluster_id

        if self.target_create_time is not None:
            result['TargetCreateTime'] = self.target_create_time

        if self.target_file_system_id is not None:
            result['TargetFileSystemId'] = self.target_file_system_id

        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id

        if self.target_instance_name is not None:
            result['TargetInstanceName'] = self.target_instance_name

        if self.target_path is not None:
            result['TargetPath'] = self.target_path

        if self.target_prefix is not None:
            result['TargetPrefix'] = self.target_prefix

        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name

        if self.target_time is not None:
            result['TargetTime'] = self.target_time

        if self.udm_detail_shrink is not None:
            result['UdmDetail'] = self.udm_detail_shrink

        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('FailbackDetail') is not None:
            self.failback_detail_shrink = m.get('FailbackDetail')

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('InitiatedByAck') is not None:
            self.initiated_by_ack = m.get('InitiatedByAck')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('OtsDetail') is not None:
            self.ots_detail_shrink = m.get('OtsDetail')

        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')

        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('TargetBucket') is not None:
            self.target_bucket = m.get('TargetBucket')

        if m.get('TargetContainer') is not None:
            self.target_container = m.get('TargetContainer')

        if m.get('TargetContainerClusterId') is not None:
            self.target_container_cluster_id = m.get('TargetContainerClusterId')

        if m.get('TargetCreateTime') is not None:
            self.target_create_time = m.get('TargetCreateTime')

        if m.get('TargetFileSystemId') is not None:
            self.target_file_system_id = m.get('TargetFileSystemId')

        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')

        if m.get('TargetInstanceName') is not None:
            self.target_instance_name = m.get('TargetInstanceName')

        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')

        if m.get('TargetPrefix') is not None:
            self.target_prefix = m.get('TargetPrefix')

        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')

        if m.get('TargetTime') is not None:
            self.target_time = m.get('TargetTime')

        if m.get('UdmDetail') is not None:
            self.udm_detail_shrink = m.get('UdmDetail')

        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

