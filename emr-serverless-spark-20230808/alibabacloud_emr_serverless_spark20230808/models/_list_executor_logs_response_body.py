# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListExecutorLogsResponseBody(DaraModel):
    def __init__(
        self,
        logs: List[main_models.ListExecutorLogsResponseBodyLogs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.logs = logs
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['logs'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logs = []
        if m.get('logs') is not None:
            for k1 in m.get('logs'):
                temp_model = main_models.ListExecutorLogsResponseBodyLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListExecutorLogsResponseBodyLogs(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_size: int = None,
        log_name: str = None,
        log_type: str = None,
        update_time: int = None,
    ):
        self.file_name = file_name
        self.file_size = file_size
        self.log_name = log_name
        self.log_type = log_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.log_name is not None:
            result['logName'] = self.log_name

        if self.log_type is not None:
            result['logType'] = self.log_type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('logName') is not None:
            self.log_name = m.get('logName')

        if m.get('logType') is not None:
            self.log_type = m.get('logType')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

