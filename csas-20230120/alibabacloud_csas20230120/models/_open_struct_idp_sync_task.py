# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenStructIdpSyncTask(DaraModel):
    def __init__(
        self,
        department_failed: int = None,
        department_total: int = None,
        end_time_unix: int = None,
        fail_type: str = None,
        idp_config_id: bytes = None,
        start_time_unix: int = None,
        status: str = None,
        sync_task_id: str = None,
        update_time_unix: int = None,
        user_failed: int = None,
        user_total: int = None,
    ):
        self.department_failed = department_failed
        self.department_total = department_total
        self.end_time_unix = end_time_unix
        self.fail_type = fail_type
        self.idp_config_id = idp_config_id
        self.start_time_unix = start_time_unix
        self.status = status
        self.sync_task_id = sync_task_id
        self.update_time_unix = update_time_unix
        self.user_failed = user_failed
        self.user_total = user_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_failed is not None:
            result['DepartmentFailed'] = self.department_failed

        if self.department_total is not None:
            result['DepartmentTotal'] = self.department_total

        if self.end_time_unix is not None:
            result['EndTimeUnix'] = self.end_time_unix

        if self.fail_type is not None:
            result['FailType'] = self.fail_type

        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id

        if self.start_time_unix is not None:
            result['StartTimeUnix'] = self.start_time_unix

        if self.status is not None:
            result['Status'] = self.status

        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id

        if self.update_time_unix is not None:
            result['UpdateTimeUnix'] = self.update_time_unix

        if self.user_failed is not None:
            result['UserFailed'] = self.user_failed

        if self.user_total is not None:
            result['UserTotal'] = self.user_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentFailed') is not None:
            self.department_failed = m.get('DepartmentFailed')

        if m.get('DepartmentTotal') is not None:
            self.department_total = m.get('DepartmentTotal')

        if m.get('EndTimeUnix') is not None:
            self.end_time_unix = m.get('EndTimeUnix')

        if m.get('FailType') is not None:
            self.fail_type = m.get('FailType')

        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')

        if m.get('StartTimeUnix') is not None:
            self.start_time_unix = m.get('StartTimeUnix')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')

        if m.get('UpdateTimeUnix') is not None:
            self.update_time_unix = m.get('UpdateTimeUnix')

        if m.get('UserFailed') is not None:
            self.user_failed = m.get('UserFailed')

        if m.get('UserTotal') is not None:
            self.user_total = m.get('UserTotal')

        return self

