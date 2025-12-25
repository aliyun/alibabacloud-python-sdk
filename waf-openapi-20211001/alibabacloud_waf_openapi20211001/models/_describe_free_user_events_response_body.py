# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeFreeUserEventsResponseBody(DaraModel):
    def __init__(
        self,
        event: List[main_models.DescribeFreeUserEventsResponseBodyEvent] = None,
        request_id: str = None,
    ):
        # The security events on which basic detection is performed.
        self.event = event
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.event:
            for v1 in self.event:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Event'] = []
        if self.event is not None:
            for k1 in self.event:
                result['Event'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event = []
        if m.get('Event') is not None:
            for k1 in m.get('Event'):
                temp_model = main_models.DescribeFreeUserEventsResponseBodyEvent()
                self.event.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFreeUserEventsResponseBodyEvent(DaraModel):
    def __init__(
        self,
        api_format: str = None,
        attack_ip: str = None,
        attack_time: int = None,
        domain: str = None,
        event_level: str = None,
        event_tag: str = None,
    ):
        # The API.
        self.api_format = api_format
        # The attacker IP address.
        self.attack_ip = attack_ip
        # The time at which the attack was launched. The value is a UNIX timestamp displayed in UTC. Unit: seconds.
        self.attack_time = attack_time
        # The domain name of the API.
        self.domain = domain
        # The severity level of the security event. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.event_level = event_level
        # The type of the security event.
        # 
        # >  You can call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to query the supported types of security events.
        self.event_tag = event_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_format is not None:
            result['ApiFormat'] = self.api_format

        if self.attack_ip is not None:
            result['AttackIP'] = self.attack_ip

        if self.attack_time is not None:
            result['AttackTime'] = self.attack_time

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_tag is not None:
            result['EventTag'] = self.event_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiFormat') is not None:
            self.api_format = m.get('ApiFormat')

        if m.get('AttackIP') is not None:
            self.attack_ip = m.get('AttackIP')

        if m.get('AttackTime') is not None:
            self.attack_time = m.get('AttackTime')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventTag') is not None:
            self.event_tag = m.get('EventTag')

        return self

