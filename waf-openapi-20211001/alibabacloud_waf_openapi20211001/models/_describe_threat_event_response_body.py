# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeThreatEventResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        threat_events: List[main_models.DescribeThreatEventResponseBodyThreatEvents] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The list of noteworthy security events.
        self.threat_events = threat_events
        # The total number of queried events.
        self.total_count = total_count

    def validate(self):
        if self.threat_events:
            for v1 in self.threat_events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ThreatEvents'] = []
        if self.threat_events is not None:
            for k1 in self.threat_events:
                result['ThreatEvents'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.threat_events = []
        if m.get('ThreatEvents') is not None:
            for k1 in m.get('ThreatEvents'):
                temp_model = main_models.DescribeThreatEventResponseBodyThreatEvents()
                self.threat_events.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeThreatEventResponseBodyThreatEvents(DaraModel):
    def __init__(
        self,
        block_rate: str = None,
        end_time: int = None,
        event_id: str = None,
        event_level: str = None,
        event_src: str = None,
        event_tag: str = None,
        event_target: str = None,
    ):
        # The percentage of blocked requests.
        self.block_rate = block_rate
        # The most recent Attack Time. The format is a UNIX timestamp in UTC. Unit: seconds.
        self.end_time = end_time
        # The ID of the security event.
        self.event_id = event_id
        # The severity level of the event. Valid values:
        # 
        # - **critical**: critical.
        # - **high**: high.
        # - **medium**: medium.
        # - **low**: low.
        self.event_level = event_level
        # The Attack Source IP Addresses.
        # > A security event may involve multiple source IP addresses. This operation returns only one source IP address.
        self.event_src = event_src
        # The name of the event. Valid values:
        # 
        # - **MultipleDomainDirscan**: folder and file scanning targeting multiple domain names.
        # - **SingleDomainDirscan**: folder and file scanning targeting a single domain name.
        # - **MultipleDomainWebscan**: web vulnerability scanning targeting multiple domain names.
        # - **SingleDomainWebscan**: web vulnerability scanning targeting a single domain name.
        # - **MultipleDomainWebattack**: web vulnerability attacks targeting multiple domain names.
        # - **SingleDomainWebattack**: web vulnerability attacks targeting a single domain name.
        # - **SingleURLWebattack**: web vulnerability attacks targeting a specific URL.
        # - **SingleURLSqlattack**: SQL injection attacks targeting a specific URL.
        # - **SingleURLXssattack**: XSS attacks targeting a specific URL.
        # - **WebshellUpload**: attempts to upload backdoor trojans.
        # - **RandomVulnTest**: random web vulnerability probing.
        self.event_tag = event_tag
        # The protected object of the Attack Target.
        # > A security event may involve multiple protected objects targeted by the attack. This operation returns only one protected object.
        self.event_target = event_target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_rate is not None:
            result['BlockRate'] = self.block_rate

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_src is not None:
            result['EventSrc'] = self.event_src

        if self.event_tag is not None:
            result['EventTag'] = self.event_tag

        if self.event_target is not None:
            result['EventTarget'] = self.event_target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockRate') is not None:
            self.block_rate = m.get('BlockRate')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventSrc') is not None:
            self.event_src = m.get('EventSrc')

        if m.get('EventTag') is not None:
            self.event_tag = m.get('EventTag')

        if m.get('EventTarget') is not None:
            self.event_target = m.get('EventTarget')

        return self

