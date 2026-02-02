# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JobHistory(DaraModel):
    def __init__(
        self,
        commit_id: str = None,
        copied_count: int = None,
        copied_size: int = None,
        end_time: str = None,
        failed_count: int = None,
        job_version: str = None,
        list_status: str = None,
        message: str = None,
        name: str = None,
        operator: str = None,
        runtime_id: str = None,
        runtime_state: str = None,
        skipped_count: int = None,
        skipped_size: int = None,
        start_time: str = None,
        status: str = None,
        total_count: int = None,
        total_size: int = None,
    ):
        self.commit_id = commit_id
        self.copied_count = copied_count
        self.copied_size = copied_size
        self.end_time = end_time
        self.failed_count = failed_count
        self.job_version = job_version
        self.list_status = list_status
        self.message = message
        self.name = name
        self.operator = operator
        self.runtime_id = runtime_id
        self.runtime_state = runtime_state
        self.skipped_count = skipped_count
        self.skipped_size = skipped_size
        self.start_time = start_time
        self.status = status
        self.total_count = total_count
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id

        if self.copied_count is not None:
            result['CopiedCount'] = self.copied_count

        if self.copied_size is not None:
            result['CopiedSize'] = self.copied_size

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.job_version is not None:
            result['JobVersion'] = self.job_version

        if self.list_status is not None:
            result['ListStatus'] = self.list_status

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        if self.runtime_state is not None:
            result['RuntimeState'] = self.runtime_state

        if self.skipped_count is not None:
            result['SkippedCount'] = self.skipped_count

        if self.skipped_size is not None:
            result['SkippedSize'] = self.skipped_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')

        if m.get('CopiedCount') is not None:
            self.copied_count = m.get('CopiedCount')

        if m.get('CopiedSize') is not None:
            self.copied_size = m.get('CopiedSize')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('JobVersion') is not None:
            self.job_version = m.get('JobVersion')

        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('RuntimeState') is not None:
            self.runtime_state = m.get('RuntimeState')

        if m.get('SkippedCount') is not None:
            self.skipped_count = m.get('SkippedCount')

        if m.get('SkippedSize') is not None:
            self.skipped_size = m.get('SkippedSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

