# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ModifyOutboundCallNumberResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        outbound_call_number: main_models.ModifyOutboundCallNumberResponseBodyOutboundCallNumber = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.outbound_call_number = outbound_call_number
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.outbound_call_number:
            self.outbound_call_number.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.outbound_call_number is not None:
            result['OutboundCallNumber'] = self.outbound_call_number.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OutboundCallNumber') is not None:
            temp_model = main_models.ModifyOutboundCallNumberResponseBodyOutboundCallNumber()
            self.outbound_call_number = temp_model.from_map(m.get('OutboundCallNumber'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ModifyOutboundCallNumberResponseBodyOutboundCallNumber(DaraModel):
    def __init__(
        self,
        number: str = None,
        outbound_call_number_id: str = None,
        rate_limit_count: str = None,
        rate_limit_period: str = None,
    ):
        self.number = number
        self.outbound_call_number_id = outbound_call_number_id
        self.rate_limit_count = rate_limit_count
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

        if self.outbound_call_number_id is not None:
            result['OutboundCallNumberId'] = self.outbound_call_number_id

        if self.rate_limit_count is not None:
            result['RateLimitCount'] = self.rate_limit_count

        if self.rate_limit_period is not None:
            result['RateLimitPeriod'] = self.rate_limit_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('OutboundCallNumberId') is not None:
            self.outbound_call_number_id = m.get('OutboundCallNumberId')

        if m.get('RateLimitCount') is not None:
            self.rate_limit_count = m.get('RateLimitCount')

        if m.get('RateLimitPeriod') is not None:
            self.rate_limit_period = m.get('RateLimitPeriod')

        return self

