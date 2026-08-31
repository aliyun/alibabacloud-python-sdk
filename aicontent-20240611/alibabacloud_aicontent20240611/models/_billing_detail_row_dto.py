# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BillingDetailRowDTO(DaraModel):
    def __init__(
        self,
        amount: float = None,
        api_key_id: int = None,
        api_key_name: str = None,
        cache_creation_tokens: float = None,
        cached_tokens: float = None,
        client_id: int = None,
        client_name: str = None,
        discount: float = None,
        input_tokens: float = None,
        member_user_id: int = None,
        member_user_name: str = None,
        metrics: str = None,
        model_code: str = None,
        model_id: int = None,
        model_name: str = None,
        model_symbol: str = None,
        model_type: str = None,
        model_version: int = None,
        output_tokens: float = None,
        reasoning_tokens: float = None,
        request_id: str = None,
        request_time: int = None,
        total_tokens: float = None,
        usage_detail: str = None,
    ):
        self.amount = amount
        self.api_key_id = api_key_id
        self.api_key_name = api_key_name
        self.cache_creation_tokens = cache_creation_tokens
        self.cached_tokens = cached_tokens
        self.client_id = client_id
        self.client_name = client_name
        self.discount = discount
        self.input_tokens = input_tokens
        self.member_user_id = member_user_id
        self.member_user_name = member_user_name
        self.metrics = metrics
        self.model_code = model_code
        self.model_id = model_id
        self.model_name = model_name
        self.model_symbol = model_symbol
        self.model_type = model_type
        self.model_version = model_version
        self.output_tokens = output_tokens
        self.reasoning_tokens = reasoning_tokens
        self.request_id = request_id
        self.request_time = request_time
        self.total_tokens = total_tokens
        self.usage_detail = usage_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.api_key_id is not None:
            result['apiKeyId'] = self.api_key_id

        if self.api_key_name is not None:
            result['apiKeyName'] = self.api_key_name

        if self.cache_creation_tokens is not None:
            result['cacheCreationTokens'] = self.cache_creation_tokens

        if self.cached_tokens is not None:
            result['cachedTokens'] = self.cached_tokens

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.client_name is not None:
            result['clientName'] = self.client_name

        if self.discount is not None:
            result['discount'] = self.discount

        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.member_user_id is not None:
            result['memberUserId'] = self.member_user_id

        if self.member_user_name is not None:
            result['memberUserName'] = self.member_user_name

        if self.metrics is not None:
            result['metrics'] = self.metrics

        if self.model_code is not None:
            result['modelCode'] = self.model_code

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_symbol is not None:
            result['modelSymbol'] = self.model_symbol

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.model_version is not None:
            result['modelVersion'] = self.model_version

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.reasoning_tokens is not None:
            result['reasoningTokens'] = self.reasoning_tokens

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.request_time is not None:
            result['requestTime'] = self.request_time

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        if self.usage_detail is not None:
            result['usageDetail'] = self.usage_detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('apiKeyId') is not None:
            self.api_key_id = m.get('apiKeyId')

        if m.get('apiKeyName') is not None:
            self.api_key_name = m.get('apiKeyName')

        if m.get('cacheCreationTokens') is not None:
            self.cache_creation_tokens = m.get('cacheCreationTokens')

        if m.get('cachedTokens') is not None:
            self.cached_tokens = m.get('cachedTokens')

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('clientName') is not None:
            self.client_name = m.get('clientName')

        if m.get('discount') is not None:
            self.discount = m.get('discount')

        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('memberUserId') is not None:
            self.member_user_id = m.get('memberUserId')

        if m.get('memberUserName') is not None:
            self.member_user_name = m.get('memberUserName')

        if m.get('metrics') is not None:
            self.metrics = m.get('metrics')

        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelSymbol') is not None:
            self.model_symbol = m.get('modelSymbol')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('modelVersion') is not None:
            self.model_version = m.get('modelVersion')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('reasoningTokens') is not None:
            self.reasoning_tokens = m.get('reasoningTokens')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('requestTime') is not None:
            self.request_time = m.get('requestTime')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        if m.get('usageDetail') is not None:
            self.usage_detail = m.get('usageDetail')

        return self

