# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupsRequest(DaraModel):
    def __init__(
        self,
        backup_task_id: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        statuses: str = None,
        time_period_end_time: int = None,
        time_period_start_time: int = None,
    ):
        self.backup_task_id = backup_task_id
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.statuses = statuses
        self.time_period_end_time = time_period_end_time
        self.time_period_start_time = time_period_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_task_id is not None:
            result['BackupTaskId'] = self.backup_task_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        if self.time_period_end_time is not None:
            result['TimePeriodEndTime'] = self.time_period_end_time

        if self.time_period_start_time is not None:
            result['TimePeriodStartTime'] = self.time_period_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupTaskId') is not None:
            self.backup_task_id = m.get('BackupTaskId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        if m.get('TimePeriodEndTime') is not None:
            self.time_period_end_time = m.get('TimePeriodEndTime')

        if m.get('TimePeriodStartTime') is not None:
            self.time_period_start_time = m.get('TimePeriodStartTime')

        return self

