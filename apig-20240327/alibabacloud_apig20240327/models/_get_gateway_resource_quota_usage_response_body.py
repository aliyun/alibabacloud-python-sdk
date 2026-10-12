# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetGatewayResourceQuotaUsageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetGatewayResourceQuotaUsageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The quota query result.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
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
            temp_model = main_models.GetGatewayResourceQuotaUsageResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGatewayResourceQuotaUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        items: List[main_models.GetGatewayResourceQuotaUsageResponseBodyDataItems] = None,
        observed_at: str = None,
    ):
        # The gateway ID.
        self.gateway_id = gateway_id
        # The resource quota items.
        self.items = items
        # The time when the statistics collection was completed.
        self.observed_at = observed_at

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
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.observed_at is not None:
            result['observedAt'] = self.observed_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetGatewayResourceQuotaUsageResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('observedAt') is not None:
            self.observed_at = m.get('observedAt')

        return self

class GetGatewayResourceQuotaUsageResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        applicable: bool = None,
        limit: int = None,
        limit_scope: str = None,
        quota_key: str = None,
        used: int = None,
        used_scope: str = None,
    ):
        # Indicates whether quota numerical values are provided.
        self.applicable = applicable
        # The effective limit.
        self.limit = limit
        # The scope to which the limit applies.
        self.limit_scope = limit_scope
        # The quota metric.
        self.quota_key = quota_key
        # The current usage.
        self.used = used
        # The scope for usage statistics.
        self.used_scope = used_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicable is not None:
            result['applicable'] = self.applicable

        if self.limit is not None:
            result['limit'] = self.limit

        if self.limit_scope is not None:
            result['limitScope'] = self.limit_scope

        if self.quota_key is not None:
            result['quotaKey'] = self.quota_key

        if self.used is not None:
            result['used'] = self.used

        if self.used_scope is not None:
            result['usedScope'] = self.used_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicable') is not None:
            self.applicable = m.get('applicable')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('limitScope') is not None:
            self.limit_scope = m.get('limitScope')

        if m.get('quotaKey') is not None:
            self.quota_key = m.get('quotaKey')

        if m.get('used') is not None:
            self.used = m.get('used')

        if m.get('usedScope') is not None:
            self.used_scope = m.get('usedScope')

        return self

