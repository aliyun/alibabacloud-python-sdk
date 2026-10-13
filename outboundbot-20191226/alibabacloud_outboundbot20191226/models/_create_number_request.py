# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class CreateNumberRequest(DaraModel):
    def __init__(
        self,
        numbers: List[main_models.CreateNumberRequestNumbers] = None,
        trunk_id: str = None,
    ):
        # The list of phone numbers to create and associate. A maximum of 100 phone numbers can be specified in a single request.
        # 
        # This parameter is required.
        self.numbers = numbers
        # The unique identifier of the SIP trunk.
        # 
        # This parameter is required.
        self.trunk_id = trunk_id

    def validate(self):
        if self.numbers:
            for v1 in self.numbers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Numbers'] = []
        if self.numbers is not None:
            for k1 in self.numbers:
                result['Numbers'].append(k1.to_map() if k1 else None)

        if self.trunk_id is not None:
            result['TrunkId'] = self.trunk_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.numbers = []
        if m.get('Numbers') is not None:
            for k1 in m.get('Numbers'):
                temp_model = main_models.CreateNumberRequestNumbers()
                self.numbers.append(temp_model.from_map(k1))

        if m.get('TrunkId') is not None:
            self.trunk_id = m.get('TrunkId')

        return self

class CreateNumberRequestNumbers(DaraModel):
    def __init__(
        self,
        number: str = None,
        rate_limit_count: int = None,
        rate_limit_period: int = None,
    ):
        # The phone number.
        self.number = number
        # The maximum number of requests allowed within the throttling period.
        self.rate_limit_count = rate_limit_count
        # The throttling period, in seconds.
        self.rate_limit_period = rate_limit_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.number is not None:
            result['Number'] = self.number

        if self.rate_limit_count is not None:
            result['RateLimitCount'] = self.rate_limit_count

        if self.rate_limit_period is not None:
            result['RateLimitPeriod'] = self.rate_limit_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('RateLimitCount') is not None:
            self.rate_limit_count = m.get('RateLimitCount')

        if m.get('RateLimitPeriod') is not None:
            self.rate_limit_period = m.get('RateLimitPeriod')

        return self

