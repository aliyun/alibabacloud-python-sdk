# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class SparkAnalyzeLogTask(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        result: main_models.LogAnalyzeResult = None,
        rule_matched: bool = None,
        started_time_in_millis: int = None,
        submitted_time_in_millis: int = None,
        task_err_msg: str = None,
        task_id: int = None,
        task_state: str = None,
        terminated_time_in_millis: int = None,
        user_id: int = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.result = result
        self.rule_matched = rule_matched
        self.started_time_in_millis = started_time_in_millis
        self.submitted_time_in_millis = submitted_time_in_millis
        self.task_err_msg = task_err_msg
        self.task_id = task_id
        self.task_state = task_state
        self.terminated_time_in_millis = terminated_time_in_millis
        self.user_id = user_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.rule_matched is not None:
            result['RuleMatched'] = self.rule_matched

        if self.started_time_in_millis is not None:
            result['StartedTimeInMillis'] = self.started_time_in_millis

        if self.submitted_time_in_millis is not None:
            result['SubmittedTimeInMillis'] = self.submitted_time_in_millis

        if self.task_err_msg is not None:
            result['TaskErrMsg'] = self.task_err_msg

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_state is not None:
            result['TaskState'] = self.task_state

        if self.terminated_time_in_millis is not None:
            result['TerminatedTimeInMillis'] = self.terminated_time_in_millis

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Result') is not None:
            temp_model = main_models.LogAnalyzeResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('RuleMatched') is not None:
            self.rule_matched = m.get('RuleMatched')

        if m.get('StartedTimeInMillis') is not None:
            self.started_time_in_millis = m.get('StartedTimeInMillis')

        if m.get('SubmittedTimeInMillis') is not None:
            self.submitted_time_in_millis = m.get('SubmittedTimeInMillis')

        if m.get('TaskErrMsg') is not None:
            self.task_err_msg = m.get('TaskErrMsg')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')

        if m.get('TerminatedTimeInMillis') is not None:
            self.terminated_time_in_millis = m.get('TerminatedTimeInMillis')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

