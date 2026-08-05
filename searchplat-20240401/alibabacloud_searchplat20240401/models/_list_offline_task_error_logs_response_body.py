# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class ListOfflineTaskErrorLogsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListOfflineTaskErrorLogsResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The collection of log request bodies, log responses, retry counts, and timestamps.
        self.result = result
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListOfflineTaskErrorLogsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListOfflineTaskErrorLogsResponseBodyResult(DaraModel):
    def __init__(
        self,
        request: str = None,
        response: str = None,
        retry: str = None,
        timestamp: str = None,
    ):
        # **The log request body.**
        self.request = request
        # **The log response.**
        self.response = response
        # **The number of retries.**
        self.retry = retry
        # **The timestamp.**
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request is not None:
            result['request'] = self.request

        if self.response is not None:
            result['response'] = self.response

        if self.retry is not None:
            result['retry'] = self.retry

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('request') is not None:
            self.request = m.get('request')

        if m.get('response') is not None:
            self.response = m.get('response')

        if m.get('retry') is not None:
            self.retry = m.get('retry')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

