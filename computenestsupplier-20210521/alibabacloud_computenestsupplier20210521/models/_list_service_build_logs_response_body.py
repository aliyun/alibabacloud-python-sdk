# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListServiceBuildLogsResponseBody(DaraModel):
    def __init__(
        self,
        build_logs: List[main_models.ListServiceBuildLogsResponseBodyBuildLogs] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # An array of build logs.
        self.build_logs = build_logs
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.build_logs:
            for v1 in self.build_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BuildLogs'] = []
        if self.build_logs is not None:
            for k1 in self.build_logs:
                result['BuildLogs'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.build_logs = []
        if m.get('BuildLogs') is not None:
            for k1 in m.get('BuildLogs'):
                temp_model = main_models.ListServiceBuildLogsResponseBodyBuildLogs()
                self.build_logs.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListServiceBuildLogsResponseBodyBuildLogs(DaraModel):
    def __init__(
        self,
        build_step: str = None,
        content: str = None,
        timestamp: str = None,
    ):
        # The name of the build step.
        self.build_step = build_step
        # The content of the log.
        self.content = content
        # The timestamp of the log entry.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_step is not None:
            result['BuildStep'] = self.build_step

        if self.content is not None:
            result['Content'] = self.content

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildStep') is not None:
            self.build_step = m.get('BuildStep')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

