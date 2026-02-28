# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetInstanceTrendingReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetInstanceTrendingReportResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetInstanceTrendingReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceTrendingReportResponseBodyData(DaraModel):
    def __init__(
        self,
        inbound: List[main_models.GetInstanceTrendingReportResponseBodyDataInbound] = None,
        outbound: List[main_models.GetInstanceTrendingReportResponseBodyDataOutbound] = None,
        overall: List[main_models.GetInstanceTrendingReportResponseBodyDataOverall] = None,
    ):
        self.inbound = inbound
        self.outbound = outbound
        self.overall = overall

    def validate(self):
        if self.inbound:
            for v1 in self.inbound:
                 if v1:
                    v1.validate()
        if self.outbound:
            for v1 in self.outbound:
                 if v1:
                    v1.validate()
        if self.overall:
            for v1 in self.overall:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Inbound'] = []
        if self.inbound is not None:
            for k1 in self.inbound:
                result['Inbound'].append(k1.to_map() if k1 else None)

        result['Outbound'] = []
        if self.outbound is not None:
            for k1 in self.outbound:
                result['Outbound'].append(k1.to_map() if k1 else None)

        result['Overall'] = []
        if self.overall is not None:
            for k1 in self.overall:
                result['Overall'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inbound = []
        if m.get('Inbound') is not None:
            for k1 in m.get('Inbound'):
                temp_model = main_models.GetInstanceTrendingReportResponseBodyDataInbound()
                self.inbound.append(temp_model.from_map(k1))

        self.outbound = []
        if m.get('Outbound') is not None:
            for k1 in m.get('Outbound'):
                temp_model = main_models.GetInstanceTrendingReportResponseBodyDataOutbound()
                self.outbound.append(temp_model.from_map(k1))

        self.overall = []
        if m.get('Overall') is not None:
            for k1 in m.get('Overall'):
                temp_model = main_models.GetInstanceTrendingReportResponseBodyDataOverall()
                self.overall.append(temp_model.from_map(k1))

        return self

class GetInstanceTrendingReportResponseBodyDataOverall(DaraModel):
    def __init__(
        self,
        max_logged_in_agents: int = None,
        stats_time: int = None,
    ):
        self.max_logged_in_agents = max_logged_in_agents
        self.stats_time = stats_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_logged_in_agents is not None:
            result['MaxLoggedInAgents'] = self.max_logged_in_agents

        if self.stats_time is not None:
            result['StatsTime'] = self.stats_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxLoggedInAgents') is not None:
            self.max_logged_in_agents = m.get('MaxLoggedInAgents')

        if m.get('StatsTime') is not None:
            self.stats_time = m.get('StatsTime')

        return self

class GetInstanceTrendingReportResponseBodyDataOutbound(DaraModel):
    def __init__(
        self,
        calls_answered: int = None,
        stats_time: int = None,
        total_calls: int = None,
    ):
        self.calls_answered = calls_answered
        self.stats_time = stats_time
        self.total_calls = total_calls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calls_answered is not None:
            result['CallsAnswered'] = self.calls_answered

        if self.stats_time is not None:
            result['StatsTime'] = self.stats_time

        if self.total_calls is not None:
            result['TotalCalls'] = self.total_calls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallsAnswered') is not None:
            self.calls_answered = m.get('CallsAnswered')

        if m.get('StatsTime') is not None:
            self.stats_time = m.get('StatsTime')

        if m.get('TotalCalls') is not None:
            self.total_calls = m.get('TotalCalls')

        return self

class GetInstanceTrendingReportResponseBodyDataInbound(DaraModel):
    def __init__(
        self,
        calls_abandoned_in_ivr: int = None,
        calls_abandoned_in_queue: int = None,
        calls_abandoned_in_ring: int = None,
        calls_handled: int = None,
        calls_queued: int = None,
        stats_time: int = None,
        total_calls: int = None,
    ):
        self.calls_abandoned_in_ivr = calls_abandoned_in_ivr
        self.calls_abandoned_in_queue = calls_abandoned_in_queue
        self.calls_abandoned_in_ring = calls_abandoned_in_ring
        self.calls_handled = calls_handled
        self.calls_queued = calls_queued
        self.stats_time = stats_time
        self.total_calls = total_calls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calls_abandoned_in_ivr is not None:
            result['CallsAbandonedInIVR'] = self.calls_abandoned_in_ivr

        if self.calls_abandoned_in_queue is not None:
            result['CallsAbandonedInQueue'] = self.calls_abandoned_in_queue

        if self.calls_abandoned_in_ring is not None:
            result['CallsAbandonedInRing'] = self.calls_abandoned_in_ring

        if self.calls_handled is not None:
            result['CallsHandled'] = self.calls_handled

        if self.calls_queued is not None:
            result['CallsQueued'] = self.calls_queued

        if self.stats_time is not None:
            result['StatsTime'] = self.stats_time

        if self.total_calls is not None:
            result['TotalCalls'] = self.total_calls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallsAbandonedInIVR') is not None:
            self.calls_abandoned_in_ivr = m.get('CallsAbandonedInIVR')

        if m.get('CallsAbandonedInQueue') is not None:
            self.calls_abandoned_in_queue = m.get('CallsAbandonedInQueue')

        if m.get('CallsAbandonedInRing') is not None:
            self.calls_abandoned_in_ring = m.get('CallsAbandonedInRing')

        if m.get('CallsHandled') is not None:
            self.calls_handled = m.get('CallsHandled')

        if m.get('CallsQueued') is not None:
            self.calls_queued = m.get('CallsQueued')

        if m.get('StatsTime') is not None:
            self.stats_time = m.get('StatsTime')

        if m.get('TotalCalls') is not None:
            self.total_calls = m.get('TotalCalls')

        return self

