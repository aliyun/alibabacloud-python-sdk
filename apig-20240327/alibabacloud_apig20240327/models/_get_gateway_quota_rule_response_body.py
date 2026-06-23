# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetGatewayQuotaRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetGatewayQuotaRuleResponseBodyData = None,
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
            temp_model = main_models.GetGatewayQuotaRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGatewayQuotaRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        base_timestamp: int = None,
        consumer_count: int = None,
        consumers: List[main_models.GetGatewayQuotaRuleResponseBodyDataConsumers] = None,
        period_type: str = None,
        quota_dimension: str = None,
        quota_limit: int = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_status: str = None,
        timezone: str = None,
        window_alignment: str = None,
    ):
        self.base_timestamp = base_timestamp
        self.consumer_count = consumer_count
        self.consumers = consumers
        self.period_type = period_type
        self.quota_dimension = quota_dimension
        self.quota_limit = quota_limit
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_status = rule_status
        self.timezone = timezone
        self.window_alignment = window_alignment

    def validate(self):
        if self.consumers:
            for v1 in self.consumers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_timestamp is not None:
            result['baseTimestamp'] = self.base_timestamp

        if self.consumer_count is not None:
            result['consumerCount'] = self.consumer_count

        result['consumers'] = []
        if self.consumers is not None:
            for k1 in self.consumers:
                result['consumers'].append(k1.to_map() if k1 else None)

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
        if m.get('baseTimestamp') is not None:
            self.base_timestamp = m.get('baseTimestamp')

        if m.get('consumerCount') is not None:
            self.consumer_count = m.get('consumerCount')

        self.consumers = []
        if m.get('consumers') is not None:
            for k1 in m.get('consumers'):
                temp_model = main_models.GetGatewayQuotaRuleResponseBodyDataConsumers()
                self.consumers.append(temp_model.from_map(k1))

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

class GetGatewayQuotaRuleResponseBodyDataConsumers(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

