# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class GetRealtimeInstanceStatsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRealtimeInstanceStatsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
        # Id of the request
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
            temp_model = main_models.GetRealtimeInstanceStatsResponseBodyData()
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

class GetRealtimeInstanceStatsResponseBodyData(DaraModel):
    def __init__(
        self,
        configured_concurrency: int = None,
        realtime_script_stats_list: List[main_models.GetRealtimeInstanceStatsResponseBodyDataRealtimeScriptStatsList] = None,
        stats_time: int = None,
        used_concurrency: int = None,
    ):
        self.configured_concurrency = configured_concurrency
        self.realtime_script_stats_list = realtime_script_stats_list
        self.stats_time = stats_time
        self.used_concurrency = used_concurrency

    def validate(self):
        if self.realtime_script_stats_list:
            for v1 in self.realtime_script_stats_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configured_concurrency is not None:
            result['ConfiguredConcurrency'] = self.configured_concurrency

        result['RealtimeScriptStatsList'] = []
        if self.realtime_script_stats_list is not None:
            for k1 in self.realtime_script_stats_list:
                result['RealtimeScriptStatsList'].append(k1.to_map() if k1 else None)

        if self.stats_time is not None:
            result['StatsTime'] = self.stats_time

        if self.used_concurrency is not None:
            result['UsedConcurrency'] = self.used_concurrency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfiguredConcurrency') is not None:
            self.configured_concurrency = m.get('ConfiguredConcurrency')

        self.realtime_script_stats_list = []
        if m.get('RealtimeScriptStatsList') is not None:
            for k1 in m.get('RealtimeScriptStatsList'):
                temp_model = main_models.GetRealtimeInstanceStatsResponseBodyDataRealtimeScriptStatsList()
                self.realtime_script_stats_list.append(temp_model.from_map(k1))

        if m.get('StatsTime') is not None:
            self.stats_time = m.get('StatsTime')

        if m.get('UsedConcurrency') is not None:
            self.used_concurrency = m.get('UsedConcurrency')

        return self

class GetRealtimeInstanceStatsResponseBodyDataRealtimeScriptStatsList(DaraModel):
    def __init__(
        self,
        configured_concurrency: int = None,
        script_id: str = None,
        script_name: str = None,
        stats_time: int = None,
        used_concurrency: int = None,
    ):
        self.configured_concurrency = configured_concurrency
        self.script_id = script_id
        self.script_name = script_name
        self.stats_time = stats_time
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

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.stats_time is not None:
            result['StatsTime'] = self.stats_time

        if self.used_concurrency is not None:
            result['UsedConcurrency'] = self.used_concurrency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfiguredConcurrency') is not None:
            self.configured_concurrency = m.get('ConfiguredConcurrency')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('StatsTime') is not None:
            self.stats_time = m.get('StatsTime')

        if m.get('UsedConcurrency') is not None:
            self.used_concurrency = m.get('UsedConcurrency')

        return self

