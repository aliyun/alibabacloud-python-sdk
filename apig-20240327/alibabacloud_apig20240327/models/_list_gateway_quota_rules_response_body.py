# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListGatewayQuotaRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListGatewayQuotaRulesResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
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

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListGatewayQuotaRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListGatewayQuotaRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListGatewayQuotaRulesResponseBodyDataItems] = None,
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
                temp_model = main_models.ListGatewayQuotaRulesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class ListGatewayQuotaRulesResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        period_type: str = None,
        quota_dimension: str = None,
        quota_limit: int = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_status: str = None,
        timezone: str = None,
        window_alignment: str = None,
    ):
        self.period_type = period_type
        self.quota_dimension = quota_dimension
        self.quota_limit = quota_limit
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_status = rule_status
        self.timezone = timezone
        self.window_alignment = window_alignment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period_type is not None:
            result['periodType'] = self.period_type

        if self.quota_dimension is not None:
            result['quotaDimension'] = self.quota_dimension

        if self.quota_limit is not None:
            result['quotaLimit'] = self.quota_limit

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.rule_status is not None:
            result['ruleStatus'] = self.rule_status

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.window_alignment is not None:
            result['windowAlignment'] = self.window_alignment

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')

        if m.get('quotaDimension') is not None:
            self.quota_dimension = m.get('quotaDimension')

        if m.get('quotaLimit') is not None:
            self.quota_limit = m.get('quotaLimit')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('ruleStatus') is not None:
            self.rule_status = m.get('ruleStatus')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('windowAlignment') is not None:
            self.window_alignment = m.get('windowAlignment')

        return self

