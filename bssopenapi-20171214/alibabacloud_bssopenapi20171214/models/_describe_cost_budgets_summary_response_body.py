# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeCostBudgetsSummaryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeCostBudgetsSummaryResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The data that is returned.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.DescribeCostBudgetsSummaryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCostBudgetsSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        host_id: str = None,
        items: List[main_models.DescribeCostBudgetsSummaryResponseBodyDataItems] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The website.
        self.host_id = host_id
        # The list of items.
        self.items = items
        # The maximum number of entries returned on the current page.
        self.max_results = max_results
        # The token for the next page of results.
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
        if self.host_id is not None:
            result['HostId'] = self.host_id

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeCostBudgetsSummaryResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCostBudgetsSummaryResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        budget: Dict[str, Any] = None,
        budget_name: str = None,
        budget_status: str = None,
        budget_type: str = None,
        calculated_values: Dict[str, Any] = None,
        consume_period: Dict[str, Any] = None,
    ):
        # Information about the budget.
        # 
        # - BudgetCycleType: The budget period. Valid values: daily, monthly, quarterly, and yearly.
        # 
        # - TotalBudgetAmount: The total budget amount.
        # 
        # - BudgetMemo: The notes for the budget.
        self.budget = budget
        # The name of the budget.
        self.budget_name = budget_name
        # The status of the budget.
        self.budget_status = budget_status
        # The type of the budget.
        self.budget_type = budget_type
        # Information about the estimate-to-actual comparison.
        # 
        # - ActualConsumeSum: The accumulated actual consumption.
        # 
        # - ActualAddForecastedAmount: The sum of the accumulated actual value and the predicted value. For a cost budget, this value represents the actual spending to date plus the forecasted spending until the budget period ends.
        # 
        # - ActualAndBudgetComparison: The comparison of the actual consumption to the budget. This value is calculated using the following formula: (Accumulated actual value / Total budget amount) × 100%.
        self.calculated_values = calculated_values
        # Information about the billing cycle.
        # 
        # - ConsumePeriodBegin: The start date of the budget.
        # 
        # - ConsumePeriodEnd: The end date of the budget.
        self.consume_period = consume_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.budget is not None:
            result['Budget'] = self.budget

        if self.budget_name is not None:
            result['BudgetName'] = self.budget_name

        if self.budget_status is not None:
            result['BudgetStatus'] = self.budget_status

        if self.budget_type is not None:
            result['BudgetType'] = self.budget_type

        if self.calculated_values is not None:
            result['CalculatedValues'] = self.calculated_values

        if self.consume_period is not None:
            result['ConsumePeriod'] = self.consume_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Budget') is not None:
            self.budget = m.get('Budget')

        if m.get('BudgetName') is not None:
            self.budget_name = m.get('BudgetName')

        if m.get('BudgetStatus') is not None:
            self.budget_status = m.get('BudgetStatus')

        if m.get('BudgetType') is not None:
            self.budget_type = m.get('BudgetType')

        if m.get('CalculatedValues') is not None:
            self.calculated_values = m.get('CalculatedValues')

        if m.get('ConsumePeriod') is not None:
            self.consume_period = m.get('ConsumePeriod')

        return self

