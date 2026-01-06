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
        # The name of the role created in the RAM of the original account for cross-account backup managed by the current account.
        self.cross_account_role_name = cross_account_role_name
        # Cross-account backup type. Supported values:
        # - SELF_ACCOUNT: Backup within the same account
        # - CROSS_ACCOUNT: Cross-account backup
        self.cross_account_type = cross_account_type
        # The original account ID managed by the current account for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        self.edition = edition
        # The path not to be restored. All documents under this path will not be restored. Maximum length is 255 characters.
        self.exclude = exclude
        # Details of restoring to the local environment.
        self.failback_detail_shrink = failback_detail_shrink
        # The path to be restored. All documents under this path will be restored. Maximum length is 255 characters.
        self.include = include
        # Indicates whether it is called by the container service. Default is false.
        self.initiated_by_ack = initiated_by_ack
        # Parameters for the restore job.
        self.options = options
        # Details of the Table Store instance.
        self.ots_detail_shrink = ots_detail_shrink
        # The type of the restore destination data source. Possible values:
        #   - **ECS_FILE**: Restore to ECS file.
        #   - **OSS**: Restore to Alibaba Cloud OSS.
        #   - **NAS**: Restore to Alibaba Cloud NAS.
        #   - **OTS_TABLE**: Restore to Alibaba Cloud OTS.
        #   - **UDM_ECS_ROLLBACK**: Restore to Alibaba Cloud ECS whole machine.
        # 
        # This parameter is required.
        self.restore_type = restore_type
        # The HASH value of the backup snapshot.
        self.snapshot_hash = snapshot_hash
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id
        # The type of the data source. Possible values:
        #   - **ECS_FILE**: Restore ECS file.
        #   - **OSS**: Restore Alibaba Cloud OSS.
        #   - **NAS**: Restore Alibaba Cloud NAS.
        #   - **OTS_TABLE**: Restore to Alibaba Cloud OTS.
        #   - **UDM_ECS**: Restore to Alibaba Cloud ECS whole machine.
        # 
        # This parameter is required.
        self.source_type = source_type
        # Valid only when **RestoreType** is **OSS**. Indicates the name of the OSS bucket at the restore destination.
        self.target_bucket = target_bucket
        # Details of the target container.
        self.target_container = target_container
        # The ID of the target container cluster.
        self.target_container_cluster_id = target_container_cluster_id
        # Valid only when **RestoreType** is **NAS**. Indicates the creation time of the file system at the restore destination.
        self.target_create_time = target_create_time
        # Valid only when **RestoreType** is **NAS**. Indicates the ID of the file system at the restore destination.
        self.target_file_system_id = target_file_system_id
        # Valid only when **RestoreType** is **ECS_FILE**. Indicates the ECS instance ID at the restore destination.
        self.target_instance_id = target_instance_id
        # The name of the target Table Store instance.
        self.target_instance_name = target_instance_name
        # Valid only when **RestoreType** is **ECS_FILE**. Indicates the file path at the restore destination.
        self.target_path = target_path
        # Valid only when **RestoreType** is **OSS**. Indicates the object prefix at the restore destination.
        self.target_prefix = target_prefix
        # The name of the data table in the target Table Store.
        self.target_table_name = target_table_name
        # The time of the Table Store to be restored. UNIX timestamp, in seconds.
        self.target_time = target_time
        # The parameter is valid only when the SourceType is set to UDM_ECS. It represents the details of the entire machine backup and is a JSON string. Depending on the value of RestoreType, different details must be passed as follows:
        # - **UDM_ECS_DISK**: ECS disk cloning.
        #   - **targetInstanceId**: string (required). Specifies the target ECS instance ID to which the cloned disk will be attached.
        #   - **diskCategory**: string (required). Specifies the type of the target disk.
        #   - **diskPerformanceLevel**: string. When diskCategory is "essd", this indicates the disk performance level, supporting PL0, PL1, PL2, and PL3, with PL1 as the default.
        # - **UDM_ECS_DISK_ROLLBACK**: ECS disk rollback.
        #   - **sourceInstanceId**: string (required). Specifies the source ECS instance ID.
        #   - **forceRestore**: bool (default: false). Indicates whether to force restore. NOTE: If forceRestore is set to true, the disk restoration will proceed even if the backup disk has been unmounted from the original ECS instance or mounted to another instance. Exercise caution when using this option.
        #   - **bootAfterRestore**: bool (default: false). Indicates whether to start the ECS instance after restoration.
        # - **UDM_ECS**: Full ECS cloning.
        #   - **bootAfterRestore**: bool (default: false). Indicates whether to start the ECS instance after restoration.
        #   - **diskCategory**: string (required). Specifies the type of the target disk.
        #   - **diskPerformanceLevel**: string. When diskCategory is "essd", this indicates the disk performance level (PL0/PL1/PL2/PL3), defaulting to PL1.
        #   - **instanceType**: string (required). Specifies the specification of the target ECS instance.
        #   - **restoredNetwork**: string (required). Specifies the vSwitch ID for the target ECS instance.
        #   - **securityGroup**: string (required). Specifies the security group ID for the target ECS instance.
        #   - **restoredName:** string (required). Specifies the instance name of the target ECS instance.
        #   - **restoredHostName**: string (required). Specifies the host name of the target ECS instance.
        #   - **allocatePublicIp**: bool (default: false). Indicates whether to assign a public IP to the target ECS instance.
        #   - **privateIpAddress**: string. Specifies the internal IP address of the target ECS instance. If not specified, an IP will be assigned via DHCP.
        # - **UDM_ECS_ROLLBACK**: Full ECS rollback.
        #   - **sourceInstanceId**: string (required). Specifies the source ECS instance ID.
        #   - **forceRestore**: bool (default: false). Indicates whether to force restore. NOTE: If forceRestore is set to true, the disk restoration will proceed even if the backup disk has been unmounted from the original ECS instance or mounted to another instance. Exercise caution when using this option.
        #   - **bootAfterRestore**: bool (default: false). Indicates whether to start the ECS instance after restoration.
        self.udm_detail_shrink = udm_detail_shrink
        # Valid only when **SourceType** is **UDM_ECS**. Indicates the target region for the restore.
        self.udm_region_id = udm_region_id
        # The ID of the backup vault that the snapshot belongs to.
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

