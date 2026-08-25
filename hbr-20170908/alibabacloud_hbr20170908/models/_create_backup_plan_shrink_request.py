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
        edition: str = None,
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
        # The backup type. Set the value to **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # This parameter is required only when **SourceType** is set to **OSS**. The name of the OSS bucket.
        self.bucket = bucket
        # The configuration of the incremental file synchronization list. This parameter is required only for data synchronization.
        self.change_list_path = change_list_path
        # The ID of the client group that executes the data synchronization plan. This parameter is required only for data synchronization.
        self.cluster_id = cluster_id
        # This parameter is required only when **SourceType** is set to **NAS**. The time when the file system was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The name of the RAM role created in the source account for cross-account backup.
        self.cross_account_role_name = cross_account_role_name
        # The cross-account backup type. Valid values: 
        # - SELF_ACCOUNT: backup within the same account.
        # - CROSS_ACCOUNT: cross-account backup.
        self.cross_account_type = cross_account_type
        # The ID of the source account for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        # The ID of the source data source. This parameter is required only for data synchronization.
        self.data_source_id = data_source_id
        # The details of the destination data source. This parameter is required only for data synchronization.
        self.dest_data_source_detail_shrink = dest_data_source_detail_shrink
        # The ID of the destination data source. This parameter is required only for data synchronization.
        self.dest_data_source_id = dest_data_source_id
        # The type of the destination data source. This parameter is required only for data synchronization.
        self.dest_source_type = dest_source_type
        # The details of the full-copy backup. The value is a JSON string.
        # 
        # * snapshotGroup: specifies whether to use a consistent snapshot group. This parameter is valid only when all cloud disks of the instance are ESSDs.
        # * appConsistent: specifies whether to use application consistency. This parameter must be used together with the preScriptPath and postScriptPath parameters.
        # * preScriptPath: the path of the pre-freeze script.
        # * postScriptPath: the path of the post-thaw script.
        self.detail_shrink = detail_shrink
        # Specifies whether the plan is disabled by default.
        self.disabled = disabled
        # The edition type. Valid values: BASIC and STANDARD. Default value: STANDARD.
        self.edition = edition
        # This parameter is required only when **SourceType** is set to **ECS_FILE**. The path to exclude from the backup. All files in this path are not backed up. The value can be up to 255 characters in length.
        self.exclude = exclude
        # This parameter is required only when **SourceType** is set to **NAS**. The file system ID.
        self.file_system_id = file_system_id
        # This parameter is required only when **SourceType** is set to **ECS_FILE**. The path to include in the backup. All files in this path are backed up. The value can be up to 255 characters in length.
        self.include = include
        # This parameter is required only when **SourceType** is set to **ECS_FILE**. The ECS instance ID.
        self.instance_id = instance_id
        # The name of the Tablestore instance.
        self.instance_name = instance_name
        # Specifies whether to retain at least one backup version. Valid values:
        # - 0: does not retain.
        # - 1: retains.
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is required only when **SourceType** is set to **ECS_FILE**. Specifies whether to use Windows Volume Shadow Copy Service (VSS) to define the source path.
        # 
        # - This feature is supported only for Windows ECS instances.
        # - If the backup source contains data changes and you need to ensure consistency between the backup data and the source data, set this parameter to `["UseVSS":true]`.
        # - After VSS is enabled, multiple file folders cannot be backed up simultaneously.
        self.options = options
        # The details of the Tablestore instance.
        self.ots_detail_shrink = ots_detail_shrink
        # The source paths.
        self.path = path
        # The name of the backup plan. The name must be 1 to 64 characters in length. The backup plan name must be unique for each data source type within a single vault.
        self.plan_name = plan_name
        # This parameter is required only when **SourceType** is set to **OSS**. The backup prefix. If specified, only objects that match the prefix are backed up.
        self.prefix = prefix
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention
        # The backup plan rules.
        self.rule = rule
        # The backup policy. Format: `I|{startTime}|{interval}`. This indicates that a backup job is executed at every `{interval}` starting from `{startTime}`. Backup jobs for past time periods are not compensated. If the previous backup job is not completed, the next backup job is not triggered. Example: `I|1631685600|P1D` indicates that a backup is performed once a day starting from 2021-09-15 14:00:00.
        # 
        # - **startTime**: the start time of the backup. The value is a UNIX timestamp. Unit: seconds.
        # - **interval**: the ISO 8601 time interval. Example: PT1H indicates an interval of one hour. P1D indicates an interval of one day.
        self.schedule = schedule
        # The type of the data source. Valid values:
        # 
        # - **ECS_FILE**: backs up ECS files.
        # - **OSS**: backs up Alibaba Cloud OSS.
        # - **NAS**: backs up Alibaba Cloud NAS.
        # - **OTS**: backs up Alibaba Cloud OTS.
        # - **UDM_ECS**: backs up an entire ECS instance.
        # - **SYNC**: data synchronization.
        # 
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required only when **SourceType** is set to **ECS_FILE**. The backup traffic control. Format: `{start}:{end}:{bandwidth}`. Separate multiple traffic control configurations with vertical bars (|). The time ranges of the configurations cannot overlap.
        # 
        # - **start**: the start hour.
        # - **end**: the end hour.
        # - **bandwidth**: the rate limit. Unit: KB/s.
        self.speed_limit = speed_limit
        # The region where the ECS instance for full-copy backup resides.
        self.udm_region_id = udm_region_id
        # The vault ID.
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

        if self.edition is not None:
            result['Edition'] = self.edition

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

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

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
        # The backup type.
        self.backup_type = backup_type
        # The ID of the destination region for cross-region replication.
        self.destination_region_id = destination_region_id
        # The retention period of the geo-redundancy backup. Unit: days.
        self.destination_retention = destination_retention
        # Specifies whether the rule is disabled.
        self.disabled = disabled
        # Specifies whether to enable cross-region replication.
        self.do_copy = do_copy
        # The retention period of the backup.
        self.retention = retention
        # The rule name.
        self.rule_name = rule_name
        # The backup policy. Format: I|{startTime}|{interval}. This indicates that a backup job is executed at every {interval} starting from {startTime}. Backup jobs for past time periods are not executed. If the previous backup job is not completed, the next backup job is not triggered. Example: I|1631685600|P1D indicates that a backup is performed once a day starting from 2021-09-15 14:00:00.
        # 
        # startTime: the start time of the backup. The value is a UNIX timestamp. Unit: seconds.
        # interval: the ISO 8601 time interval. Example: PT1H indicates an interval of one hour. P1D indicates an interval of one day.
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

