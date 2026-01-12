# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DebuggerJobIssue(DaraModel):
    def __init__(
        self,
        debugger_job_issue: str = None,
        gmt_create_time: str = None,
        job_debugger_issue_id: str = None,
        job_id: str = None,
        reason_code: str = None,
        reason_message: str = None,
        rule_name: str = None,
    ):
        self.debugger_job_issue = debugger_job_issue
        self.gmt_create_time = gmt_create_time
        self.job_debugger_issue_id = job_debugger_issue_id
        self.job_id = job_id
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debugger_job_issue is not None:
            result['DebuggerJobIssue'] = self.debugger_job_issue

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.job_debugger_issue_id is not None:
            result['JobDebuggerIssueId'] = self.job_debugger_issue_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebuggerJobIssue') is not None:
            self.debugger_job_issue = m.get('DebuggerJobIssue')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('JobDebuggerIssueId') is not None:
            self.job_debugger_issue_id = m.get('JobDebuggerIssueId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

