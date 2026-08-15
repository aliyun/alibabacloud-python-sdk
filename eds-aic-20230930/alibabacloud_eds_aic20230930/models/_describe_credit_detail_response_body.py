# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeCreditDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeCreditDetailResponseBodyData = None,
        request_id: str = None,
    ):
        # The response object.
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeCreditDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCreditDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        details: List[main_models.DescribeCreditDetailResponseBodyDataDetails] = None,
        next_token: str = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        total_credit_change: str = None,
    ):
        # The credit change details.
        self.details = details
        self.next_token = next_token
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The total number of detail records.
        self.total_count = total_count
        # The total credit change.
        self.total_credit_change = total_credit_change

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_credit_change is not None:
            result['TotalCreditChange'] = self.total_credit_change

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.DescribeCreditDetailResponseBodyDataDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalCreditChange') is not None:
            self.total_credit_change = m.get('TotalCreditChange')

        return self

class DescribeCreditDetailResponseBodyDataDetails(DaraModel):
    def __init__(
        self,
        api_key_name: str = None,
        cached_tokens: int = None,
        change_time: str = None,
        credit_change: str = None,
        description: str = None,
        duration_ms: int = None,
        input_tokens: int = None,
        instance_id: str = None,
        instance_name: str = None,
        model_id: str = None,
        output_tokens: int = None,
        package_id: str = None,
        request_id: str = None,
        task_id: str = None,
        total_tokens: int = None,
        ttft_ms: int = None,
    ):
        self.api_key_name = api_key_name
        self.cached_tokens = cached_tokens
        # The time when the change occurred.
        self.change_time = change_time
        # The credit change amount.
        self.credit_change = credit_change
        # The task description.
        self.description = description
        self.duration_ms = duration_ms
        self.input_tokens = input_tokens
        # The instance ID.
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.model_id = model_id
        self.output_tokens = output_tokens
        # The ID of the credit or plan package.
        self.package_id = package_id
        self.request_id = request_id
        # The task ID, which is globally unique.
        self.task_id = task_id
        self.total_tokens = total_tokens
        self.ttft_ms = ttft_ms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_name is not None:
            result['ApiKeyName'] = self.api_key_name

        if self.cached_tokens is not None:
            result['CachedTokens'] = self.cached_tokens

        if self.change_time is not None:
            result['ChangeTime'] = self.change_time

        if self.credit_change is not None:
            result['CreditChange'] = self.credit_change

        if self.description is not None:
            result['Description'] = self.description

        if self.duration_ms is not None:
            result['DurationMs'] = self.duration_ms

        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.package_id is not None:
            result['PackageId'] = self.package_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        if self.ttft_ms is not None:
            result['TtftMs'] = self.ttft_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyName') is not None:
            self.api_key_name = m.get('ApiKeyName')

        if m.get('CachedTokens') is not None:
            self.cached_tokens = m.get('CachedTokens')

        if m.get('ChangeTime') is not None:
            self.change_time = m.get('ChangeTime')

        if m.get('CreditChange') is not None:
            self.credit_change = m.get('CreditChange')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DurationMs') is not None:
            self.duration_ms = m.get('DurationMs')

        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        if m.get('TtftMs') is not None:
            self.ttft_ms = m.get('TtftMs')

        return self

