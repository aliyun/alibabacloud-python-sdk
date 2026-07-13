# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class GetModelInvocationSummaryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetModelInvocationSummaryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetModelInvocationSummaryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetModelInvocationSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        call_frequency: float = None,
        provider_distribution: List[main_models.GetModelInvocationSummaryResponseBodyDataProviderDistribution] = None,
        today_call_count: int = None,
        today_change_rate: float = None,
        week_call_count: int = None,
        week_change_rate: float = None,
    ):
        self.call_frequency = call_frequency
        self.provider_distribution = provider_distribution
        self.today_call_count = today_call_count
        self.today_change_rate = today_change_rate
        self.week_call_count = week_call_count
        self.week_change_rate = week_change_rate

    def validate(self):
        if self.provider_distribution:
            for v1 in self.provider_distribution:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_frequency is not None:
            result['CallFrequency'] = self.call_frequency

        result['ProviderDistribution'] = []
        if self.provider_distribution is not None:
            for k1 in self.provider_distribution:
                result['ProviderDistribution'].append(k1.to_map() if k1 else None)

        if self.today_call_count is not None:
            result['TodayCallCount'] = self.today_call_count

        if self.today_change_rate is not None:
            result['TodayChangeRate'] = self.today_change_rate

        if self.week_call_count is not None:
            result['WeekCallCount'] = self.week_call_count

        if self.week_change_rate is not None:
            result['WeekChangeRate'] = self.week_change_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallFrequency') is not None:
            self.call_frequency = m.get('CallFrequency')

        self.provider_distribution = []
        if m.get('ProviderDistribution') is not None:
            for k1 in m.get('ProviderDistribution'):
                temp_model = main_models.GetModelInvocationSummaryResponseBodyDataProviderDistribution()
                self.provider_distribution.append(temp_model.from_map(k1))

        if m.get('TodayCallCount') is not None:
            self.today_call_count = m.get('TodayCallCount')

        if m.get('TodayChangeRate') is not None:
            self.today_change_rate = m.get('TodayChangeRate')

        if m.get('WeekCallCount') is not None:
            self.week_call_count = m.get('WeekCallCount')

        if m.get('WeekChangeRate') is not None:
            self.week_change_rate = m.get('WeekChangeRate')

        return self

class GetModelInvocationSummaryResponseBodyDataProviderDistribution(DaraModel):
    def __init__(
        self,
        count: int = None,
        percentage: float = None,
        provider_name: str = None,
    ):
        self.count = count
        self.percentage = percentage
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        return self

