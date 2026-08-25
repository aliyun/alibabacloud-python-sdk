# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class UpdateBackupPlanShrinkRequest(DaraModel):
    def __init__(
        self,
        change_list_path: str = None,
        detail_shrink: str = None,
        edition: str = None,
        exclude: str = None,
        include: str = None,
        keep_latest_snapshots: int = None,
        options: str = None,
        ots_detail_shrink: str = None,
        path: List[str] = None,
        plan_id: str = None,
        plan_name: str = None,
        prefix: str = None,
        retention: int = None,
        rule: List[main_models.UpdateBackupPlanShrinkRequestRule] = None,
        schedule: str = None,
        source_type: str = None,
        speed_limit: str = None,
        update_paths: bool = None,
        vault_id: str = None,
    ):
        # The configuration for the incremental file synchronization list. (This parameter is required only for file synchronization.)
        self.change_list_path = change_list_path
        # The details of the ECS instance backup. This is a JSON string.
        # 
        # - snapshotGroup: Specifies whether to use a snapshot-consistent group. This feature is available only when all disks of the instance are Enhanced Solid-State Drives (ESSDs).
        # 
        # - appConsistent: Specifies whether to enable application consistency. You must also configure the preScriptPath and postScriptPath parameters.
        # 
        # - preScriptPath: The path to the pre-freeze script.
        # 
        # - postScriptPath: The path to the post-thaw script.
        self.detail_shrink = detail_shrink
        # The edition. Valid values are BASIC and STANDARD. The default value is STANDARD.
        self.edition = edition
        # This parameter is required only when **SourceType** is set to **ECS_FILE**. This parameter specifies the paths to the files to exclude from the backup. All files in the specified paths are not backed up. The value can be up to 255 characters in length.
        self.exclude = exclude
        # This parameter is required only when **SourceType** is set to **ECS_FILE**. This parameter specifies the paths to the files to back up. All files in the specified paths are backed up. The value can be up to 255 characters in length.
        self.include = include
        # Specifies whether to permanently retain the latest backup version.
        # 
        # - 0: No
        # 
        # - 1: Yes
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is required only when **SourceType** is set to **ECS_FILE**. This parameter specifies whether to use Volume Shadow Copy Service (VSS) to define the backup path.
        # 
        # - This feature is available only for Windows ECS instances.
        # 
        # - If data changes occur in the backup source, set this parameter to `["UseVSS":true]` to ensure data consistency.
        # 
        # - If you enable VSS, you cannot back up multiple file directories at the same time.
        self.options = options
        # The details of the Tablestore instance.
        self.ots_detail_shrink = ots_detail_shrink
        # The backup paths.
        self.path = path
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The name of the backup plan.
        self.plan_name = plan_name
        # This parameter is required only when **SourceType** is set to **OSS**. This parameter specifies the prefix of objects to back up. After you specify a prefix, only objects that match the prefix are backed up.
        self.prefix = prefix
        # The number of days to retain backups. The minimum value is 1.
        self.retention = retention
        # The rules of the backup plan.
        self.rule = rule
        # The backup policy. Use the `I|{startTime}|{interval}` format. This specifies that a backup job runs at a recurring interval. The `{startTime}` is when the backup starts. The `{interval}` is the time between jobs. HBR does not run overdue backup jobs. If the previous backup job is not finished, the next one does not start. For example, `I|1631685600|P1D` means the backup runs once a day, starting at 14:00:00 on September 15, 2021.
        # 
        # - **startTime**: The start time of the backup. This is a UNIX timestamp in seconds.
        # 
        # - **interval**: The time interval. Use the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule
        # The type of the data source. Valid values:
        # 
        # - **ECS_FILE**: Backs up ECS files.
        # 
        # - **OSS**: Backs up Alibaba Cloud OSS.
        # 
        # - **NAS**: Backs up Alibaba Cloud NAS.
        # 
        # - **OTS**: Backs up Alibaba Cloud Tablestore.
        # 
        # - **UDM_ECS**: Backs up an entire ECS instance.
        self.source_type = source_type
        # This parameter is required only when **SourceType** is set to **ECS_FILE**. This parameter specifies traffic shaping for backups. Traffic shaping helps you control backup traffic during peak business hours to avoid affecting your services. The format is `{start}|{end}|{bandwidth}`. You can specify multiple traffic shaping rules. Separate them with vertical bars (|). The time ranges of the rules cannot overlap.
        # 
        # - **start**: The start hour.
        # 
        # - **end**: The end hour.
        # 
        # - **bandwidth**: The maximum speed. Unit: KB/s.
        self.speed_limit = speed_limit
        # Specifies whether to update the backup paths if the Path parameter is empty.
        # 
        # - true: Updates the backup paths based on the paths specified in this call.
        # 
        # - false: Does not update the backup paths. The backup paths that were configured when the backup plan was created are used.
        self.update_paths = update_paths
        # The ID of the backup repository.
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
        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path

        if self.detail_shrink is not None:
            result['Detail'] = self.detail_shrink

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.include is not None:
            result['Include'] = self.include

        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots

        if self.options is not None:
            result['Options'] = self.options

        if self.ots_detail_shrink is not None:
            result['OtsDetail'] = self.ots_detail_shrink

        if self.path is not None:
            result['Path'] = self.path

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

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

        if self.update_paths is not None:
            result['UpdatePaths'] = self.update_paths

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')

        if m.get('Detail') is not None:
            self.detail_shrink = m.get('Detail')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('OtsDetail') is not None:
            self.ots_detail_shrink = m.get('OtsDetail')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        self.rule = []
        if m.get('Rule') is not None:
            for k1 in m.get('Rule'):
                temp_model = main_models.UpdateBackupPlanShrinkRequestRule()
                self.rule.append(temp_model.from_map(k1))

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')

        if m.get('UpdatePaths') is not None:
            self.update_paths = m.get('UpdatePaths')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

class UpdateBackupPlanShrinkRequestRule(DaraModel):
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
        # The backup type. Set the value to **COMPLETE**. This indicates a full backup.
        self.backup_type = backup_type
        # The ID of the destination region for the geo-redundant backup.
        self.destination_region_id = destination_region_id
        # The number of days to retain the geo-redundant backup.
        self.destination_retention = destination_retention
        # Specifies whether to disable the policy.
        self.disabled = disabled
        # Specifies whether to enable geo-redundant replication.
        self.do_copy = do_copy
        # The number of days to retain backups. The minimum value is 1.
        self.retention = retention
        # The name of the policy.
        self.rule_name = rule_name
        # The backup policy. Use the I|{startTime}|{interval} format. This specifies that a backup job runs at a recurring interval. The {startTime} is when the backup starts. The {interval} is the time between jobs. HBR does not run overdue backup jobs. If the previous backup job is not finished, the next one does not start. For example, I|1631685600|P1D means the backup runs once a day, starting at 14:00:00 on September 15, 2021.
        # 
        # startTime: The start time of the backup. This is a UNIX timestamp in seconds. interval: The time interval. Use the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
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

