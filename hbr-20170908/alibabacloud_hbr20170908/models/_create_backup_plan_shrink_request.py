# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class CreateBackupPlanShrinkRequest(DaraModel):
    def __init__(
        self,
        backup_type: str = None,
        bucket: str = None,
        change_list_path: str = None,
        cluster_id: str = None,
        create_time: int = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        data_source_id: str = None,
        dest_data_source_detail_shrink: str = None,
        dest_data_source_id: str = None,
        dest_source_type: str = None,
        detail_shrink: str = None,
        disabled: bool = None,
        exclude: str = None,
        file_system_id: str = None,
        include: str = None,
        instance_id: str = None,
        instance_name: str = None,
        keep_latest_snapshots: int = None,
        options: str = None,
        ots_detail_shrink: str = None,
        path: List[str] = None,
        plan_name: str = None,
        prefix: str = None,
        retention: int = None,
        rule: List[main_models.CreateBackupPlanShrinkRequestRule] = None,
        schedule: str = None,
        source_type: str = None,
        speed_limit: str = None,
        udm_region_id: str = None,
        vault_id: str = None,
    ):
        # Backup type. Value: **COMPLETE**, indicating a full backup.
        self.backup_type = backup_type
        # This parameter is required when **SourceType** is set to **OSS**. It represents the OSS bucket name.
        self.bucket = bucket
        # Configuration for the incremental file synchronization list. (Required only for synchronization)
        self.change_list_path = change_list_path
        # The ID of the client group that executes the data synchronization plan. This parameter is required only for data synchronization.
        self.cluster_id = cluster_id
        # This parameter is required when **SourceType** is set to **NAS**. It represents the creation time of the file system, in UNIX timestamp, in seconds.
        self.create_time = create_time
        # The role name created in the RAM of the original account for cross-account backup.
        self.cross_account_role_name = cross_account_role_name
        # Cross-account backup type. Supported values:
        # - SELF_ACCOUNT: Backup within the same account
        # - CROSS_ACCOUNT: Cross-account backup
        self.cross_account_type = cross_account_type
        # The original account ID used for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        # The ID of the data source. This parameter is required only for data synchronization.
        self.data_source_id = data_source_id
        # Destination data source details. (Required only for synchronization)
        self.dest_data_source_detail_shrink = dest_data_source_detail_shrink
        # Destination data source ID. (Required only for synchronization)
        self.dest_data_source_id = dest_data_source_id
        # Destination data source type. (Required only for synchronization)
        self.dest_source_type = dest_source_type
        # Details of the whole machine backup, in JSON string format.
        # 
        # * snapshotGroup: Whether to use a consistent snapshot group (only valid if all instance disks are ESSD).
        # * appConsistent: Whether to use application consistency (requires the use of preScriptPath and postScriptPath parameters).
        # * preScriptPath: Path to the freeze script.
        # * postScriptPath: Path to the thaw script.
        self.detail_shrink = detail_shrink
        # Is the plan disabled by default
        self.disabled = disabled
        # This parameter is required only when **SourceType** is set to **ECS_FILE**. It specifies the path that should not be backed up, meaning all files under this path will not be included in the backup. The maximum length is 255 characters.
        self.exclude = exclude
        # This parameter is required when **SourceType** is set to **NAS**. It represents the file system ID.
        self.file_system_id = file_system_id
        # This parameter is required when **SourceType** is set to **ECS_FILE**. It represents the path to be backed up, and all files under this path will be backed up. Supports up to 255 characters.
        self.include = include
        # This parameter is required when **SourceType** is set to **ECS_FILE**. It represents the ECS instance ID.
        self.instance_id = instance_id
        # Table store instance name.
        self.instance_name = instance_name
        # Whether to enable retaining at least one backup version.
        # - 0 - Do not retain
        # - 1 - Retain
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is required when **SourceType** is set to **ECS_FILE**. It indicates whether to use the Windows system VSS to define the backup path.
        # 
        # - This feature only supports Windows type ECS instances.
        # - If there are data changes in the backup source and you need to ensure consistency between the backup data and the source data, you can configure it as `["UseVSS":true]`.
        # - After choosing to use VSS, multiple file directories cannot be backed up simultaneously.
        self.options = options
        # The details about the Tablestore instance.
        self.ots_detail_shrink = ots_detail_shrink
        # Backup paths.
        self.path = path
        # Name of the backup plan. 1 to 64 characters. The name must be unique for each data source type within a single backup vault.
        self.plan_name = plan_name
        # This parameter is required when **SourceType** is set to **OSS**. It represents the backup prefix. When specified, only objects matching the prefix are backed up.
        self.prefix = prefix
        # Number of days to retain the backup, with a minimum value of 1, in days.
        self.retention = retention
        # Backup plan rules.
        self.rule = rule
        # Backup policy. Optional format: `I|{startTime}|{interval}`. This indicates that a backup task will be executed every `{interval}` starting from `{startTime}`. It does not compensate for missed backup tasks due to past time. If the previous backup task has not been completed, the next backup task will not be triggered. For example, `I|1631685600|P1D` means a backup is performed every day starting from 2021-09-15 14:00:00.
        # 
        # - **startTime**: Start time of the backup, in UNIX timestamp, in seconds.
        # - **interval**: ISO8601 time interval. For example, PT1H indicates an interval of one hour, and P1D indicates an interval of one day.
        self.schedule = schedule
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: File Storage NAS (NAS) file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        # *   **SYNC**: data synchronization
        # 
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required when **SourceType** is set to **ECS_FILE**. It represents the backup traffic control. Format: `{start}:{end}:{bandwidth}`. Multiple traffic control configurations are separated by |, and the configured times should not overlap.
        # 
        # - **start**: Start hour.
        # - **end**: End hour.
        # - **bandwidth**: Limit rate, in KB/s.
        self.speed_limit = speed_limit
        # Region where the whole machine backup instance is located.
        self.udm_region_id = udm_region_id
        # Backup vault ID.
        self.vault_id = vault_id

    def validate(self):
        if self.rule:
            for v1 in self.rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.dest_data_source_detail_shrink is not None:
            result['DestDataSourceDetail'] = self.dest_data_source_detail_shrink

        if self.dest_data_source_id is not None:
            result['DestDataSourceId'] = self.dest_data_source_id

        if self.dest_source_type is not None:
            result['DestSourceType'] = self.dest_source_type

        if self.detail_shrink is not None:
            result['Detail'] = self.detail_shrink

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.include is not None:
            result['Include'] = self.include

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots

        if self.options is not None:
            result['Options'] = self.options

        if self.ots_detail_shrink is not None:
            result['OtsDetail'] = self.ots_detail_shrink

        if self.path is not None:
            result['Path'] = self.path

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.retention is not None:
            result['Retention'] = self.retention

        result['Rule'] = []
        if self.rule is not None:
            for k1 in self.rule:
                result['Rule'].append(k1.to_map() if k1 else None)

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit

        if self.udm_region_id is not None:
            result['UdmRegionId'] = self.udm_region_id

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DestDataSourceDetail') is not None:
            self.dest_data_source_detail_shrink = m.get('DestDataSourceDetail')

        if m.get('DestDataSourceId') is not None:
            self.dest_data_source_id = m.get('DestDataSourceId')

        if m.get('DestSourceType') is not None:
            self.dest_source_type = m.get('DestSourceType')

        if m.get('Detail') is not None:
            self.detail_shrink = m.get('Detail')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('OtsDetail') is not None:
            self.ots_detail_shrink = m.get('OtsDetail')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        self.rule = []
        if m.get('Rule') is not None:
            for k1 in m.get('Rule'):
                temp_model = main_models.CreateBackupPlanShrinkRequestRule()
                self.rule.append(temp_model.from_map(k1))

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')

        if m.get('UdmRegionId') is not None:
            self.udm_region_id = m.get('UdmRegionId')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

class CreateBackupPlanShrinkRequestRule(DaraModel):
    def __init__(
        self,
        backup_type: str = None,
        destination_region_id: str = None,
        destination_retention: int = None,
        disabled: bool = None,
        do_copy: bool = None,
        retention: int = None,
        rule_name: str = None,
        schedule: str = None,
    ):
        # Backup type.
        self.backup_type = backup_type
        # ID of the region for offsite replication.
        self.destination_region_id = destination_region_id
        # Number of days to retain offsite backups.
        self.destination_retention = destination_retention
        # Whether the rule is enabled.
        self.disabled = disabled
        # Whether to enable offsite replication.
        self.do_copy = do_copy
        # Backup retention period.
        self.retention = retention
        # Rule name.
        self.rule_name = rule_name
        # Backup strategy. Optional format: I|{startTime}|{interval}. This means that a backup task is executed every {interval} starting from {startTime}. Backup tasks for past times will not be executed. If the previous backup task has not been completed, the next backup task will not be triggered. For example, I|1631685600|P1D means a backup is performed every day starting from 2021-09-15 14:00:00.
        # 
        # - startTime: The start time of the backup, in UNIX time, in seconds.
        # - interval: ISO8601 time interval. For example, PT1H means an interval of one hour. P1D means an interval of one day.
        self.schedule = schedule

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id

        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')

        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        return self

