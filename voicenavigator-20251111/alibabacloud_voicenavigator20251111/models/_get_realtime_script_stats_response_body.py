# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class GetRealtimeScriptStatsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRealtimeScriptStatsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        # The error code.
        self.code = code
        # The real-time script statistics.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # A list of error parameters.
        self.params = params
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetRealtimeScriptStatsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetRealtimeScriptStatsResponseBodyData(DaraModel):
    def __init__(
        self,
        configured_concurrency: int = None,
        stats_time: int = None,
        used_concurrency: int = None,
    ):
        # The configured concurrency.
        self.configured_concurrency = configured_concurrency
        # The time the statistics were collected, expressed as a Unix timestamp in milliseconds.
        self.stats_time = stats_time
        # The current concurrency.
        self.used_concurrency = used_concurrency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configured_concurrency is not None:
            result['ConfiguredConcurrency'] = self.configured_concurrency

        if self.stats_time is not None:
            result['StatsTime'] = self.stats_time

        if self.used_concurrency is not None:
            result['UsedConcurrency'] = self.used_concurrency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfiguredConcurrency') is not None:
            self.configured_concurrency = m.get('ConfiguredConcurrency')

        if m.get('StatsTime') is not None:
            self.stats_time = m.get('StatsTime')

        if m.get('UsedConcurrency') is not None:
            self.used_concurrency = m.get('UsedConcurrency')

        return self

