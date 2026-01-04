# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainAttackEventsResponseBody(DaraModel):
    def __init__(
        self,
        domain_attack_events: List[main_models.DescribeDomainAttackEventsResponseBodyDomainAttackEvents] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the details of the DDoS attack event.
        self.domain_attack_events = domain_attack_events
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned DDoS attack events.
        self.total_count = total_count

    def validate(self):
        if self.domain_attack_events:
            for v1 in self.domain_attack_events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainAttackEvents'] = []
        if self.domain_attack_events is not None:
            for k1 in self.domain_attack_events:
                result['DomainAttackEvents'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_attack_events = []
        if m.get('DomainAttackEvents') is not None:
            for k1 in m.get('DomainAttackEvents'):
                temp_model = main_models.DescribeDomainAttackEventsResponseBodyDomainAttackEvents()
                self.domain_attack_events.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDomainAttackEventsResponseBodyDomainAttackEvents(DaraModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        max_qps: int = None,
        start_time: int = None,
    ):
        # The attacked domain name.
        self.domain = domain
        # The time when the DDoS attack stopped. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The peak attack QPS.
        self.max_qps = max_qps
        # The time when the DDoS attack started. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

