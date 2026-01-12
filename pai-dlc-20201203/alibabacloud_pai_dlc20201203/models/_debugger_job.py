# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DebuggerJob(DaraModel):
    def __init__(
        self,
        debugger_job_id: str = None,
        display_name: str = None,
        duration: str = None,
        gmt_create_time: str = None,
        gmt_failed_time: str = None,
        gmt_finish_time: str = None,
        gmt_running_time: str = None,
        gmt_stopped_time: str = None,
        gmt_submitted_time: str = None,
        gmt_succeed_time: str = None,
        status: str = None,
        user_id: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.debugger_job_id = debugger_job_id
        self.display_name = display_name
        self.duration = duration
        self.gmt_create_time = gmt_create_time
        self.gmt_failed_time = gmt_failed_time
        self.gmt_finish_time = gmt_finish_time
        self.gmt_running_time = gmt_running_time
        self.gmt_stopped_time = gmt_stopped_time
        self.gmt_submitted_time = gmt_submitted_time
        self.gmt_succeed_time = gmt_succeed_time
        self.status = status
        self.user_id = user_id
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debugger_job_id is not None:
            result['DebuggerJobId'] = self.debugger_job_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_failed_time is not None:
            result['GmtFailedTime'] = self.gmt_failed_time

        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time

        if self.gmt_running_time is not None:
            result['GmtRunningTime'] = self.gmt_running_time

        if self.gmt_stopped_time is not None:
            result['GmtStoppedTime'] = self.gmt_stopped_time

        if self.gmt_submitted_time is not None:
            result['GmtSubmittedTime'] = self.gmt_submitted_time

        if self.gmt_succeed_time is not None:
            result['GmtSucceedTime'] = self.gmt_succeed_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebuggerJobId') is not None:
            self.debugger_job_id = m.get('DebuggerJobId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtFailedTime') is not None:
            self.gmt_failed_time = m.get('GmtFailedTime')

        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')

        if m.get('GmtRunningTime') is not None:
            self.gmt_running_time = m.get('GmtRunningTime')

        if m.get('GmtStoppedTime') is not None:
            self.gmt_stopped_time = m.get('GmtStoppedTime')

        if m.get('GmtSubmittedTime') is not None:
            self.gmt_submitted_time = m.get('GmtSubmittedTime')

        if m.get('GmtSucceedTime') is not None:
            self.gmt_succeed_time = m.get('GmtSucceedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

