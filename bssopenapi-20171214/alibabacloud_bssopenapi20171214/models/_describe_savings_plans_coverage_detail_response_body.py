# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeSavingsPlansCoverageDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSavingsPlansCoverageDetailResponseBodyData = None,
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
            temp_model = main_models.DescribeSavingsPlansCoverageDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSavingsPlansCoverageDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeSavingsPlansCoverageDetailResponseBodyDataItems] = None,
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
                temp_model = main_models.DescribeSavingsPlansCoverageDetailResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSavingsPlansCoverageDetailResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        coverage_percentage: float = None,
        currency: str = None,
        deduct_amount: float = None,
        end_period: str = None,
        instance_id: str = None,
        instance_spec: str = None,
        owner_id: int = None,
        postpaid_cost: float = None,
        region: str = None,
        start_period: str = None,
        total_amount: float = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # The coverage.
        self.coverage_percentage = coverage_percentage
        # The currency.
        self.currency = currency
        # The deducted amount.
        self.deduct_amount = deduct_amount
        # The end time.
        self.end_period = end_period
        # The ID of the instance.
        self.instance_id = instance_id
        # The specifications.
        self.instance_spec = instance_spec
        self.owner_id = owner_id
        # The pay-as-you-go cost.
        self.postpaid_cost = postpaid_cost
        # The region.
        self.region = region
        # The start time.
        self.start_period = start_period
        # The total expenditure.
        self.total_amount = total_amount
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
        if self.coverage_percentage is not None:
            result['CoveragePercentage'] = self.coverage_percentage

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.deduct_amount is not None:
            result['DeductAmount'] = self.deduct_amount

        if self.end_period is not None:
            result['EndPeriod'] = self.end_period

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.postpaid_cost is not None:
            result['PostpaidCost'] = self.postpaid_cost

        if self.region is not None:
            result['Region'] = self.region

        if self.start_period is not None:
            result['StartPeriod'] = self.start_period

        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoveragePercentage') is not None:
            self.coverage_percentage = m.get('CoveragePercentage')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DeductAmount') is not None:
            self.deduct_amount = m.get('DeductAmount')

        if m.get('EndPeriod') is not None:
            self.end_period = m.get('EndPeriod')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PostpaidCost') is not None:
            self.postpaid_cost = m.get('PostpaidCost')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartPeriod') is not None:
            self.start_period = m.get('StartPeriod')

        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

