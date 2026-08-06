# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeMOTokenUsageSummaryResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        records: List[main_models.DescribeMOTokenUsageSummaryResponseBodyRecords] = None,
        request_id: str = None,
        success: bool = None,
        summary: main_models.DescribeMOTokenUsageSummaryResponseBodySummary = None,
        usage_type: str = None,
    ):
        self.message = message
        self.records = records
        self.request_id = request_id
        self.success = success
        self.summary = summary
        self.usage_type = usage_type

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.summary is not None:
            result['Summary'] = self.summary.to_map()

        if self.usage_type is not None:
            result['UsageType'] = self.usage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.DescribeMOTokenUsageSummaryResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Summary') is not None:
            temp_model = main_models.DescribeMOTokenUsageSummaryResponseBodySummary()
            self.summary = temp_model.from_map(m.get('Summary'))

        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')

        return self

class DescribeMOTokenUsageSummaryResponseBodySummary(DaraModel):
    def __init__(
        self,
        cache_tokens: float = None,
        input_tokens: float = None,
        output_tokens: float = None,
        total_tokens: float = None,
    ):
        self.cache_tokens = cache_tokens
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_tokens is not None:
            result['CacheTokens'] = self.cache_tokens

        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheTokens') is not None:
            self.cache_tokens = m.get('CacheTokens')

        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

class DescribeMOTokenUsageSummaryResponseBodyRecords(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        cache_tokens: float = None,
        date: str = None,
        input_tokens: float = None,
        key_name: str = None,
        model: str = None,
        output_tokens: float = None,
        request_count: int = None,
        total_tokens: float = None,
        usage_type: str = None,
    ):
        self.api_key = api_key
        self.cache_tokens = cache_tokens
        self.date = date
        self.input_tokens = input_tokens
        self.key_name = key_name
        self.model = model
        self.output_tokens = output_tokens
        self.request_count = request_count
        self.total_tokens = total_tokens
        self.usage_type = usage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.cache_tokens is not None:
            result['CacheTokens'] = self.cache_tokens

        if self.date is not None:
            result['Date'] = self.date

        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.model is not None:
            result['Model'] = self.model

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.request_count is not None:
            result['RequestCount'] = self.request_count

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        if self.usage_type is not None:
            result['UsageType'] = self.usage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('CacheTokens') is not None:
            self.cache_tokens = m.get('CacheTokens')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')

        return self

