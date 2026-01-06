# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class UpdateBackupPlanRequest(DaraModel):
    def __init__(
        self,
        change_list_path: str = None,
        detail: Dict[str, Any] = None,
        edition: str = None,
        exclude: str = None,
        include: str = None,
        keep_latest_snapshots: int = None,
        options: str = None,
        ots_detail: main_models.OtsDetail = None,
        path: List[str] = None,
        plan_id: str = None,
        plan_name: str = None,
        prefix: str = None,
        retention: int = None,
        rule: List[main_models.UpdateBackupPlanRequestRule] = None,
        schedule: str = None,
        source_type: str = None,
        speed_limit: str = None,
        update_paths: bool = None,
        vault_id: str = None,
    ):
        # The configurations of the incremental file synchronization. This parameter is required for data synchronization only.
        self.change_list_path = change_list_path
        # The details about ECS instance backup. The value is a JSON string.
        # 
        # *   snapshotGroup: specifies whether to use a snapshot-consistent group. This parameter is valid only if all disks of the ECS instance are enhanced SSDs (ESSDs).
        # *   appConsistent: specifies whether to enable application consistency. If you set this parameter to true, you must also specify the preScriptPath and postScriptPath parameters.
        # *   preScriptPath: the path to the pre-freeze scripts.
        # *   postScriptPath: the path to the post-thaw scripts.
        self.detail = detail
        self.edition = edition
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that are excluded from the backup job. The value must be 1 to 255 characters in length.
        self.exclude = exclude
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the paths to the files that you want to back up. The value must be 1 to 255 characters in length.
        self.include = include
        # Specifies whether to enable the feature of keeping at least one backup version. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies whether to use Windows Volume Shadow Copy Service (VSS) to define a source path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before you can set this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot back up data from multiple directories.
        self.options = options
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail
        # The source paths.
        self.path = path
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The name of the backup plan.
        self.plan_name = plan_name
        # This parameter is required only if the **SourceType** parameter is set to **OSS**. This parameter specifies the prefix of objects that you want to back up. After a prefix is specified, only objects whose names start with the prefix are backed up.
        self.prefix = prefix
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention
        # The rule of the backup plan.
        self.rule = rule
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the `{startTime}` parameter and the subsequent backup jobs at an interval that is specified in the `{interval}` parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   **startTime**: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds.
        # *   **interval**: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
        self.schedule = schedule
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type
        # This parameter is required only if the **SourceType** parameter is set to **ECS_FILE**. This parameter specifies the throttling rules. To ensure business continuity, you can limit the bandwidth that is used for file backup during peak hours. Format: `{start}|{end}|{bandwidth}`. Separate multiple throttling rules with vertical bars (|). A specified time range cannot overlap with another time range.
        # 
        # *   **start**: the start hour
        # *   **end**: the end hour.
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit
        # Specifies whether to update the source path if the backup source is empty. Valid values:
        # 
        # *   true: The system replaces the original source path with the specified source path.
        # *   false: The system does not update the original source path. The system backs up data based on the source path that you specified when you created the backup plan.
        self.update_paths = update_paths
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.ots_detail:
            self.ots_detail.validate()
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

        if self.detail is not None:
            result['Detail'] = self.detail

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

        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()

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
            self.detail = m.get('Detail')

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
            temp_model = main_models.OtsDetail()
            self.ots_detail = temp_model.from_map(m.get('OtsDetail'))

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
                temp_model = main_models.UpdateBackupPlanRequestRule()
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

class UpdateBackupPlanRequestRule(DaraModel):
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
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # The ID of the region where the remote backup vault resides.
        self.destination_region_id = destination_region_id
        # The retention period of the backup data. Unit: days.
        self.destination_retention = destination_retention
        # Specifies whether to disable the policy.
        self.disabled = disabled
        # Specifies whether to enable remote replication.
        self.do_copy = do_copy
        # The retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention
        # The name of the backup policy.
        self.rule_name = rule_name
        # The backup policy. Format: I|{startTime}|{interval}. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, I|1631685600|P1D specifies that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # startTime: the time at which the system starts to run a backup job. The time must follow the UNIX time format. Unit: seconds. interval: the interval at which the system runs a backup job. The interval must follow the ISO 8601 standard. For example, PT1H specifies an interval of one hour. P1D specifies an interval of one day.
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

