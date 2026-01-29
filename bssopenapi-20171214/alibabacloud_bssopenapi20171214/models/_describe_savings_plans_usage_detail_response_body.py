# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeSavingsPlansUsageDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSavingsPlansUsageDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The return data.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation was successful.
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
            temp_model = main_models.DescribeSavingsPlansUsageDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSavingsPlansUsageDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeSavingsPlansUsageDetailResponseBodyDataItems] = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The data entries.
        self.items = items
        # The token of the next page.
        self.next_token = next_token
        # The total number of entries.
        self.total_count = total_count

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
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeSavingsPlansUsageDetailResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSavingsPlansUsageDetailResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        currency: str = None,
        deduct_value: float = None,
        end_period: str = None,
        instance_id: str = None,
        pool_value: float = None,
        postpaid_cost: float = None,
        saved_cost: float = None,
        start_period: str = None,
        status: str = None,
        type: str = None,
        usage_percentage: float = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # The currency.
        self.currency = currency
        # The used amount of the savings plan.
        self.deduct_value = deduct_value
        # The end time.
        self.end_period = end_period
        # The ID of the instance.
        self.instance_id = instance_id
        # The total amount of the savings plan.
        self.pool_value = pool_value
        # The pay-as-you-go cost.
        self.postpaid_cost = postpaid_cost
        # The amount that is saved.
        self.saved_cost = saved_cost
        # The start time.
        self.start_period = start_period
        # The status of the instance.
        # 
        # A value of -1 indicates that the payment is overdue. A value of 1 indicates that the instance is active.
        self.status = status
        # The type of the savings plan. Valid values: universal and ECS compute.
        self.type = type
        # The usage.
        self.usage_percentage = usage_percentage
        # The ID of the account.
        self.user_id = user_id
        # The username of the account.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.deduct_value is not None:
            result['DeductValue'] = self.deduct_value

        if self.end_period is not None:
            result['EndPeriod'] = self.end_period

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.pool_value is not None:
            result['PoolValue'] = self.pool_value

        if self.postpaid_cost is not None:
            result['PostpaidCost'] = self.postpaid_cost

        if self.saved_cost is not None:
            result['SavedCost'] = self.saved_cost

        if self.start_period is not None:
            result['StartPeriod'] = self.start_period

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.usage_percentage is not None:
            result['UsagePercentage'] = self.usage_percentage

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DeductValue') is not None:
            self.deduct_value = m.get('DeductValue')

        if m.get('EndPeriod') is not None:
            self.end_period = m.get('EndPeriod')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PoolValue') is not None:
            self.pool_value = m.get('PoolValue')

        if m.get('PostpaidCost') is not None:
            self.postpaid_cost = m.get('PostpaidCost')

        if m.get('SavedCost') is not None:
            self.saved_cost = m.get('SavedCost')

        if m.get('StartPeriod') is not None:
            self.start_period = m.get('StartPeriod')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UsagePercentage') is not None:
            self.usage_percentage = m.get('UsagePercentage')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

