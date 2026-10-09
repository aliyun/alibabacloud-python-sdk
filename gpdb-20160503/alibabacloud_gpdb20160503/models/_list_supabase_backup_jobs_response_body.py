# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListSupabaseBackupJobsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListSupabaseBackupJobsResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of backup tasks.
        self.items = items
        # The maximum number of entries to return for this request.
        self.max_results = max_results
        # The pagination token for the next page, which can be used as the NextToken parameter in the next request.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListSupabaseBackupJobsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSupabaseBackupJobsResponseBodyItems(DaraModel):
    def __init__(
        self,
        backup_job_id: str = None,
        backup_mode: str = None,
        backup_status: str = None,
        process: str = None,
        start_time: str = None,
    ):
        # The ID of the backup task.
        self.backup_job_id = backup_job_id
        # The backup mode. Valid values:
        # * **Automated**: automatic backup
        # * **Manual**: manual backup
        self.backup_mode = backup_mode
        # The status of the backup task. Valid statuses include: schedule (waiting to be scheduled) and backup (in progress).
        self.backup_status = backup_status
        # The progress percentage of the backup task, such as 0%. This value may be an empty string when the task is in the schedule (waiting to be scheduled) state.
        self.process = process
        # The start time of the backup task. The time is displayed in UTC in the yyyy-MM-ddTHH:mm:ssZ format. This value may be an empty string when the task is in the schedule (waiting to be scheduled) state.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_job_id is not None:
            result['BackupJobId'] = self.backup_job_id

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.process is not None:
            result['Process'] = self.process

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupJobId') is not None:
            self.backup_job_id = m.get('BackupJobId')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

