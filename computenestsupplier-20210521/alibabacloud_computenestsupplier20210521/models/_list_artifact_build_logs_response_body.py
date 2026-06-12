# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListArtifactBuildLogsResponseBody(DaraModel):
    def __init__(
        self,
        build_logs: List[main_models.ListArtifactBuildLogsResponseBodyBuildLogs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The log array.
        self.build_logs = build_logs
        # The number of entries returned per page. The maximum value is 100 and the default value is 20.
        self.max_results = max_results
        # The token to start the next paged query.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

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
                temp_model = main_models.ListArtifactBuildLogsResponseBodyBuildLogs()
                self.build_logs.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListArtifactBuildLogsResponseBodyBuildLogs(DaraModel):
    def __init__(
        self,
        content: str = None,
        timestamp: str = None,
    ):
        # The log content.
        self.content = content
        # The timestamp.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

