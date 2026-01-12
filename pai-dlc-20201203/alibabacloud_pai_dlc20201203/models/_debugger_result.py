# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DebuggerResult(DaraModel):
    def __init__(
        self,
        debugger_config_content: str = None,
        debugger_job_issues: str = None,
        debugger_job_status: str = None,
        debugger_report_url: str = None,
        job_display_name: str = None,
        job_id: str = None,
        job_user_id: str = None,
    ):
        self.debugger_config_content = debugger_config_content
        self.debugger_job_issues = debugger_job_issues
        self.debugger_job_status = debugger_job_status
        self.debugger_report_url = debugger_report_url
        self.job_display_name = job_display_name
        self.job_id = job_id
        self.job_user_id = job_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debugger_config_content is not None:
            result['DebuggerConfigContent'] = self.debugger_config_content

        if self.debugger_job_issues is not None:
            result['DebuggerJobIssues'] = self.debugger_job_issues

        if self.debugger_job_status is not None:
            result['DebuggerJobStatus'] = self.debugger_job_status

        if self.debugger_report_url is not None:
            result['DebuggerReportURL'] = self.debugger_report_url

        if self.job_display_name is not None:
            result['JobDisplayName'] = self.job_display_name

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_user_id is not None:
            result['JobUserId'] = self.job_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebuggerConfigContent') is not None:
            self.debugger_config_content = m.get('DebuggerConfigContent')

        if m.get('DebuggerJobIssues') is not None:
            self.debugger_job_issues = m.get('DebuggerJobIssues')

        if m.get('DebuggerJobStatus') is not None:
            self.debugger_job_status = m.get('DebuggerJobStatus')

        if m.get('DebuggerReportURL') is not None:
            self.debugger_report_url = m.get('DebuggerReportURL')

        if m.get('JobDisplayName') is not None:
            self.job_display_name = m.get('JobDisplayName')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobUserId') is not None:
            self.job_user_id = m.get('JobUserId')

        return self

