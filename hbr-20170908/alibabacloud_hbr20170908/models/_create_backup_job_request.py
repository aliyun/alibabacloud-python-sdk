# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateBackupJobRequest(DaraModel):
    def __init__(
        self,
        backup_type: str = None,
        cluster_id: str = None,
        container_cluster_id: str = None,
        container_resources: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        detail: Dict[str, Any] = None,
        exclude: str = None,
        include: str = None,
        initiated_by_ack: bool = None,
        instance_id: str = None,
        job_name: str = None,
        options: str = None,
        retention: int = None,
        source_type: str = None,
        speed_limit: str = None,
        vault_id: str = None,
    ):
        # The backup type. This parameter is required only if you set the SourceType parameter to UDM_ECS.
        # 
        # *   **COMPLETE**: full backup
        self.backup_type = backup_type
        # You do not need to specify this parameter.
        self.cluster_id = cluster_id
        # You do not need to specify this parameter.
        self.container_cluster_id = container_cluster_id
        # You do not need to specify this parameter.
        self.container_resources = container_resources
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # This parameter is required only if you set the **SourceType** parameter to **UDM_ECS**. The value is a JSON string. Valid values:
        # 
        # *   doCopy: specifies whether to enable remote replication.
        # 
        # *   destinationRegionId: the destination region for remote replication.
        # 
        # *   destinationRetention: the retention period of the backup point for remote replication.
        # 
        # *   diskIdList: the IDs of the disks that are to be backed up. If this parameter is left empty, all disks are backed up.
        # 
        # *   snapshotGroup: specifies whether to use a snapshot-consistent group. This parameter is valid only if all disks of the ECS instance are Enterprise SSDs (ESSDs).
        # 
        # *   appConsistent: specifies whether to use the application-consistent backup feature. This parameter must be used with the preScriptPath and postScriptPath parameters.
        # 
        # *   preScriptPath: the path to the pre-freeze scripts.
        # 
        # *   postScriptPath: the path to the post-thaw scripts.
        # 
        # *   enableWriters: This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies whether to create application-consistent snapshots.
        # 
        #     *   true: creates application-consistent snapshots.
        #     *   false: creates file system-consistent snapshots.
        # 
        # *   enableFsFreeze: This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies whether to enable Linux fsfreeze to put file systems into the read-only state before application-consistent snapshots are created. Default value: true.
        # 
        # *   timeoutSeconds: This parameter is required only if you set the **AppConsistent** parameter to **true**. This parameter specifies the I/O freeze timeout period. Default value: 30. Unit: seconds.
        self.detail = detail
        # This parameter does not take effect if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the paths to the files that are excluded from the backup job. The value can be up to 255 characters in length.
        self.exclude = exclude
        # This parameter does not take effect if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the paths to the files that are backed up. The value can be up to 255 characters in length.
        self.include = include
        # false or left empty
        self.initiated_by_ack = initiated_by_ack
        # This parameter is required only if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the ID of the ECS instance.
        self.instance_id = instance_id
        # The name of the backup job.
        self.job_name = job_name
        # You do not need to specify this parameter.
        self.options = options
        # The retention period of the backup data. Unit: days.
        self.retention = retention
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: Elastic Compute Service (ECS) instance
        # 
        # This parameter is required.
        self.source_type = source_type
        # This parameter does not take effect if you set the **SourceType** parameter to **UDM_ECS**. This parameter specifies the throttling rules. Format: `{start}|{end}|{bandwidth}`. Separate multiple throttling rules with vertical bars (|). A specified time range cannot overlap with another time range.
        # 
        # *   **start**: the start hour.
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit
        # The ID of the backup vault. This parameter is not required if you set the SourceType parameter to UDM_ECS.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.container_cluster_id is not None:
            result['ContainerClusterId'] = self.container_cluster_id

        if self.container_resources is not None:
            result['ContainerResources'] = self.container_resources

        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.include is not None:
            result['Include'] = self.include

        if self.initiated_by_ack is not None:
            result['InitiatedByAck'] = self.initiated_by_ack

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.options is not None:
            result['Options'] = self.options

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ContainerClusterId') is not None:
            self.container_cluster_id = m.get('ContainerClusterId')

        if m.get('ContainerResources') is not None:
            self.container_resources = m.get('ContainerResources')

        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('InitiatedByAck') is not None:
            self.initiated_by_ack = m.get('InitiatedByAck')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

