# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyOutboundCallNumberRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        number: str = None,
        outbound_call_number_id: str = None,
        rate_limit_count: int = None,
        rate_limit_period: int = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.number = number
        # This parameter is required.
        self.outbound_call_number_id = outbound_call_number_id
        # This parameter is required.
        self.rate_limit_count = rate_limit_count
        # This parameter is required.
        self.rate_limit_period = rate_limit_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.number is not None:
            result['Number'] = self.number

        if self.outbound_call_number_id is not None:
            result['OutboundCallNumberId'] = self.outbound_call_number_id

        if self.rate_limit_count is not None:
            result['RateLimitCount'] = self.rate_limit_count

        if self.rate_limit_period is not None:
            result['RateLimitPeriod'] = self.rate_limit_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('OutboundCallNumberId') is not None:
            self.outbound_call_number_id = m.get('OutboundCallNumberId')

        if m.get('RateLimitCount') is not None:
            self.rate_limit_count = m.get('RateLimitCount')

        if m.get('RateLimitPeriod') is not None:
            self.rate_limit_period = m.get('RateLimitPeriod')

        return self

