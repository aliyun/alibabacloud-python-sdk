# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Rule(DaraModel):
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
        # * COMPLETE：Full backup.
        # * INCREMENTAL：Incremental backup.
        self.backup_type = backup_type
        # The replication region id.
        self.destination_region_id = destination_region_id
        # The retention period of remote backups. Minimum value: 1. Unit: days.
        self.destination_retention = destination_retention
        # Whether the plan is disbaled for this data source.
        # - **true**: disabled
        # - **false**: Not disabled
        self.disabled = disabled
        # Whether do copy.
        self.do_copy = do_copy
        # This parameter indicates the retention period of the backup data. Minimum value: 1. Unit: days.
        self.retention = retention
        # The rule name.
        self.rule_name = rule_name
        # This parameter is returned only if the value of the **RuleType** parameter is **BACKUP**. This parameter indicates the backup schedule settings. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified in the {startTime} parameter and the subsequent backup jobs at an interval that is specified in the {interval} parameter. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   startTime: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   interval: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
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

