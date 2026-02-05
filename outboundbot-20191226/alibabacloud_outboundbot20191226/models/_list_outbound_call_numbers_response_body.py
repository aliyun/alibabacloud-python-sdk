# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListOutboundCallNumbersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        outbound_call_numbers: main_models.ListOutboundCallNumbersResponseBodyOutboundCallNumbers = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.outbound_call_numbers = outbound_call_numbers
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.outbound_call_numbers:
            self.outbound_call_numbers.validate()

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

        if self.outbound_call_numbers is not None:
            result['OutboundCallNumbers'] = self.outbound_call_numbers.to_map()

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

        if m.get('OutboundCallNumbers') is not None:
            temp_model = main_models.ListOutboundCallNumbersResponseBodyOutboundCallNumbers()
            self.outbound_call_numbers = temp_model.from_map(m.get('OutboundCallNumbers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListOutboundCallNumbersResponseBodyOutboundCallNumbers(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListOutboundCallNumbersResponseBodyOutboundCallNumbersList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListOutboundCallNumbersResponseBodyOutboundCallNumbersList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOutboundCallNumbersResponseBodyOutboundCallNumbersList(DaraModel):
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

