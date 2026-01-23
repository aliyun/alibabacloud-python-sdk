# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListArtifactBuildTaskLogResponseBody(DaraModel):
    def __init__(
        self,
        build_task_logs: List[main_models.ListArtifactBuildTaskLogResponseBodyBuildTaskLogs] = None,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The log entries of the artifact build task.
        self.build_task_logs = build_task_logs
        # The response code.
        self.code = code
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: successful
        # *   `false`: failed
        self.is_success = is_success
        # The request ID.
        self.request_id = request_id
        # The total number of log entries.
        self.total_count = total_count

    def validate(self):
        if self.build_task_logs:
            for v1 in self.build_task_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BuildTaskLogs'] = []
        if self.build_task_logs is not None:
            for k1 in self.build_task_logs:
                result['BuildTaskLogs'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.build_task_logs = []
        if m.get('BuildTaskLogs') is not None:
            for k1 in m.get('BuildTaskLogs'):
                temp_model = main_models.ListArtifactBuildTaskLogResponseBodyBuildTaskLogs()
                self.build_task_logs.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListArtifactBuildTaskLogResponseBodyBuildTaskLogs(DaraModel):
    def __init__(
        self,
        line_number: int = None,
        message: str = None,
    ):
        # The row number of the log entry.
        self.line_number = line_number
        # The log data.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line_number is not None:
            result['LineNumber'] = self.line_number

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineNumber') is not None:
            self.line_number = m.get('LineNumber')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

