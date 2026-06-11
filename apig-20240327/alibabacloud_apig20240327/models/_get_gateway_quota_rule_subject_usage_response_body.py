# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetGatewayQuotaRuleSubjectUsageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetGatewayQuotaRuleSubjectUsageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetGatewayQuotaRuleSubjectUsageResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGatewayQuotaRuleSubjectUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        cached_amount: int = None,
        details: main_models.GetGatewayQuotaRuleSubjectUsageResponseBodyDataDetails = None,
        input_amount: int = None,
        output_amount: int = None,
        over_limit: bool = None,
        total_quota: int = None,
        used_amount: int = None,
    ):
        self.cached_amount = cached_amount
        self.details = details
        self.input_amount = input_amount
        self.output_amount = output_amount
        self.over_limit = over_limit
        self.total_quota = total_quota
        self.used_amount = used_amount

    def validate(self):
        if self.details:
            self.details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cached_amount is not None:
            result['cachedAmount'] = self.cached_amount

        if self.details is not None:
            result['details'] = self.details.to_map()

        if self.input_amount is not None:
            result['inputAmount'] = self.input_amount

        if self.output_amount is not None:
            result['outputAmount'] = self.output_amount

        if self.over_limit is not None:
            result['overLimit'] = self.over_limit

        if self.total_quota is not None:
            result['totalQuota'] = self.total_quota

        if self.used_amount is not None:
            result['usedAmount'] = self.used_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cachedAmount') is not None:
            self.cached_amount = m.get('cachedAmount')

        if m.get('details') is not None:
            temp_model = main_models.GetGatewayQuotaRuleSubjectUsageResponseBodyDataDetails()
            self.details = temp_model.from_map(m.get('details'))

        if m.get('inputAmount') is not None:
            self.input_amount = m.get('inputAmount')

        if m.get('outputAmount') is not None:
            self.output_amount = m.get('outputAmount')

        if m.get('overLimit') is not None:
            self.over_limit = m.get('overLimit')

        if m.get('totalQuota') is not None:
            self.total_quota = m.get('totalQuota')

        if m.get('usedAmount') is not None:
            self.used_amount = m.get('usedAmount')

        return self

class GetGatewayQuotaRuleSubjectUsageResponseBodyDataDetails(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetGatewayQuotaRuleSubjectUsageResponseBodyDataDetailsItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_size is not None:
            result['totalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetGatewayQuotaRuleSubjectUsageResponseBodyDataDetailsItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class GetGatewayQuotaRuleSubjectUsageResponseBodyDataDetailsItems(DaraModel):
    def __init__(
        self,
        cached_amount: int = None,
        input_amount: int = None,
        model: str = None,
        output_amount: int = None,
        start_time: str = None,
        used_amount: int = None,
    ):
        self.cached_amount = cached_amount
        self.input_amount = input_amount
        self.model = model
        self.output_amount = output_amount
        self.start_time = start_time
        self.used_amount = used_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cached_amount is not None:
            result['cachedAmount'] = self.cached_amount

        if self.input_amount is not None:
            result['inputAmount'] = self.input_amount

        if self.model is not None:
            result['model'] = self.model

        if self.output_amount is not None:
            result['outputAmount'] = self.output_amount

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.used_amount is not None:
            result['usedAmount'] = self.used_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cachedAmount') is not None:
            self.cached_amount = m.get('cachedAmount')

        if m.get('inputAmount') is not None:
            self.input_amount = m.get('inputAmount')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('outputAmount') is not None:
            self.output_amount = m.get('outputAmount')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('usedAmount') is not None:
            self.used_amount = m.get('usedAmount')

        return self

