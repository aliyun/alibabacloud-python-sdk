# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgenticDmsInstanceSyncTask(DaraModel):
    def __init__(
        self,
        actor_id: str = None,
        actor_name: str = None,
        actor_type: str = None,
        error_code: str = None,
        error_summary: str = None,
        failed_count: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        skipped_count: int = None,
        status: str = None,
        success_count: int = None,
        sync_user_data_permission: bool = None,
        task_id: str = None,
        total_count: int = None,
    ):
        self.actor_id = actor_id
        self.actor_name = actor_name
        self.actor_type = actor_type
        self.error_code = error_code
        self.error_summary = error_summary
        self.failed_count = failed_count
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.skipped_count = skipped_count
        self.status = status
        self.success_count = success_count
        self.sync_user_data_permission = sync_user_data_permission
        self.task_id = task_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actor_id is not None:
            result['ActorId'] = self.actor_id

        if self.actor_name is not None:
            result['ActorName'] = self.actor_name

        if self.actor_type is not None:
            result['ActorType'] = self.actor_type

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_summary is not None:
            result['ErrorSummary'] = self.error_summary

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.skipped_count is not None:
            result['SkippedCount'] = self.skipped_count

        if self.status is not None:
            result['Status'] = self.status

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.sync_user_data_permission is not None:
            result['SyncUserDataPermission'] = self.sync_user_data_permission

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActorId') is not None:
            self.actor_id = m.get('ActorId')

        if m.get('ActorName') is not None:
            self.actor_name = m.get('ActorName')

        if m.get('ActorType') is not None:
            self.actor_type = m.get('ActorType')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorSummary') is not None:
            self.error_summary = m.get('ErrorSummary')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('SkippedCount') is not None:
            self.skipped_count = m.get('SkippedCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('SyncUserDataPermission') is not None:
            self.sync_user_data_permission = m.get('SyncUserDataPermission')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

