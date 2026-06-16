# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_antiddos_public20170518 import models as main_models
from darabonba.model import DaraModel

class DescribeDdosEventListResponseBody(DaraModel):
    def __init__(
        self,
        ddos_event_list: main_models.DescribeDdosEventListResponseBodyDdosEventList = None,
        request_id: str = None,
        total: int = None,
    ):
        self.ddos_event_list = ddos_event_list
        # The ID of the request. Alibaba Cloud generates a unique ID for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The total number of DDoS attack events found.
        self.total = total

    def validate(self):
        if self.ddos_event_list:
            self.ddos_event_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddos_event_list is not None:
            result['DdosEventList'] = self.ddos_event_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosEventList') is not None:
            temp_model = main_models.DescribeDdosEventListResponseBodyDdosEventList()
            self.ddos_event_list = temp_model.from_map(m.get('DdosEventList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeDdosEventListResponseBodyDdosEventList(DaraModel):
    def __init__(
        self,
        ddos_event: List[main_models.DescribeDdosEventListResponseBodyDdosEventListDdosEvent] = None,
    ):
        self.ddos_event = ddos_event

    def validate(self):
        if self.ddos_event:
            for v1 in self.ddos_event:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DdosEvent'] = []
        if self.ddos_event is not None:
            for k1 in self.ddos_event:
                result['DdosEvent'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ddos_event = []
        if m.get('DdosEvent') is not None:
            for k1 in m.get('DdosEvent'):
                temp_model = main_models.DescribeDdosEventListResponseBodyDdosEventListDdosEvent()
                self.ddos_event.append(temp_model.from_map(k1))

        return self

class DescribeDdosEventListResponseBodyDdosEventListDdosEvent(DaraModel):
    def __init__(
        self,
        ddos_status: str = None,
        ddos_type: str = None,
        delay_time: int = None,
        end_time: int = None,
        start_time: int = None,
        un_blackhole_time: int = None,
    ):
        self.ddos_status = ddos_status
        self.ddos_type = ddos_type
        self.delay_time = delay_time
        self.end_time = end_time
        self.start_time = start_time
        self.un_blackhole_time = un_blackhole_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status

        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.un_blackhole_time is not None:
            result['UnBlackholeTime'] = self.un_blackhole_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')

        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UnBlackholeTime') is not None:
            self.un_blackhole_time = m.get('UnBlackholeTime')

        return self

