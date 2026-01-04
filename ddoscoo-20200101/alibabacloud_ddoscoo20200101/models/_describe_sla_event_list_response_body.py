# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeSlaEventListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sla_event: List[main_models.DescribeSlaEventListResponseBodySlaEvent] = None,
        total: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The destination rate limit events.
        self.sla_event = sla_event
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.sla_event:
            for v1 in self.sla_event:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SlaEvent'] = []
        if self.sla_event is not None:
            for k1 in self.sla_event:
                result['SlaEvent'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sla_event = []
        if m.get('SlaEvent') is not None:
            for k1 in m.get('SlaEvent'):
                temp_model = main_models.DescribeSlaEventListResponseBodySlaEvent()
                self.sla_event.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeSlaEventListResponseBodySlaEvent(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        ip: str = None,
        region: str = None,
        start_time: int = None,
    ):
        # The end of the time range. Unit: seconds.
        self.end_time = end_time
        # The IP address of the instance.
        self.ip = ip
        # The region to which the destination IP address belongs. Valid values:
        # 
        # *   **cn**: a region in the Chinese mainland
        # *   **cn-hongkong**: China (Hong Kong)
        self.region = region
        # The beginning of the time range. Unit: seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.region is not None:
            result['Region'] = self.region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

