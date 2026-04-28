# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_advisor20180120 import models as main_models
from darabonba.model import DaraModel

class DescribeCostCheckResultsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeCostCheckResultsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = main_models.DescribeCostCheckResultsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCostCheckResultsResponseBodyData(DaraModel):
    def __init__(
        self,
        advice_resource_count: int = None,
        group_by: str = None,
        normal_count: int = None,
        resource_count: int = None,
        total_count: int = None,
        view_group: List[main_models.DescribeCostCheckResultsResponseBodyDataViewGroup] = None,
        warning_count: int = None,
    ):
        self.advice_resource_count = advice_resource_count
        self.group_by = group_by
        self.normal_count = normal_count
        self.resource_count = resource_count
        self.total_count = total_count
        self.view_group = view_group
        self.warning_count = warning_count

    def validate(self):
        if self.view_group:
            for v1 in self.view_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice_resource_count is not None:
            result['AdviceResourceCount'] = self.advice_resource_count

        if self.group_by is not None:
            result['GroupBy'] = self.group_by

        if self.normal_count is not None:
            result['NormalCount'] = self.normal_count

        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['ViewGroup'] = []
        if self.view_group is not None:
            for k1 in self.view_group:
                result['ViewGroup'].append(k1.to_map() if k1 else None)

        if self.warning_count is not None:
            result['WarningCount'] = self.warning_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceResourceCount') is not None:
            self.advice_resource_count = m.get('AdviceResourceCount')

        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')

        if m.get('NormalCount') is not None:
            self.normal_count = m.get('NormalCount')

        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.view_group = []
        if m.get('ViewGroup') is not None:
            for k1 in m.get('ViewGroup'):
                temp_model = main_models.DescribeCostCheckResultsResponseBodyDataViewGroup()
                self.view_group.append(temp_model.from_map(k1))

        if m.get('WarningCount') is not None:
            self.warning_count = m.get('WarningCount')

        return self

class DescribeCostCheckResultsResponseBodyDataViewGroup(DaraModel):
    def __init__(
        self,
        check_items: List[main_models.DescribeCostCheckResultsResponseBodyDataViewGroupCheckItems] = None,
        group_code: str = None,
        group_count: int = None,
        group_expected_saving_cost: float = None,
        group_name: str = None,
    ):
        self.check_items = check_items
        self.group_code = group_code
        self.group_count = group_count
        self.group_expected_saving_cost = group_expected_saving_cost
        self.group_name = group_name

    def validate(self):
        if self.check_items:
            for v1 in self.check_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckItems'] = []
        if self.check_items is not None:
            for k1 in self.check_items:
                result['CheckItems'].append(k1.to_map() if k1 else None)

        if self.group_code is not None:
            result['GroupCode'] = self.group_code

        if self.group_count is not None:
            result['GroupCount'] = self.group_count

        if self.group_expected_saving_cost is not None:
            result['GroupExpectedSavingCost'] = self.group_expected_saving_cost

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_items = []
        if m.get('CheckItems') is not None:
            for k1 in m.get('CheckItems'):
                temp_model = main_models.DescribeCostCheckResultsResponseBodyDataViewGroupCheckItems()
                self.check_items.append(temp_model.from_map(k1))

        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')

        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')

        if m.get('GroupExpectedSavingCost') is not None:
            self.group_expected_saving_cost = m.get('GroupExpectedSavingCost')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

class DescribeCostCheckResultsResponseBodyDataViewGroupCheckItems(DaraModel):
    def __init__(
        self,
        advice_count: int = None,
        advice_resource_count: int = None,
        category: str = None,
        check_id: str = None,
        check_name: str = None,
        current_cost: float = None,
        description: str = None,
        expected_saving_cost: float = None,
        optimized_cost: float = None,
        product: str = None,
        severity: int = None,
        summary: str = None,
        tips: str = None,
    ):
        self.advice_count = advice_count
        self.advice_resource_count = advice_resource_count
        self.category = category
        self.check_id = check_id
        self.check_name = check_name
        self.current_cost = current_cost
        self.description = description
        self.expected_saving_cost = expected_saving_cost
        self.optimized_cost = optimized_cost
        self.product = product
        self.severity = severity
        self.summary = summary
        self.tips = tips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice_count is not None:
            result['AdviceCount'] = self.advice_count

        if self.advice_resource_count is not None:
            result['AdviceResourceCount'] = self.advice_resource_count

        if self.category is not None:
            result['Category'] = self.category

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_name is not None:
            result['CheckName'] = self.check_name

        if self.current_cost is not None:
            result['CurrentCost'] = self.current_cost

        if self.description is not None:
            result['Description'] = self.description

        if self.expected_saving_cost is not None:
            result['ExpectedSavingCost'] = self.expected_saving_cost

        if self.optimized_cost is not None:
            result['OptimizedCost'] = self.optimized_cost

        if self.product is not None:
            result['Product'] = self.product

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.tips is not None:
            result['Tips'] = self.tips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceCount') is not None:
            self.advice_count = m.get('AdviceCount')

        if m.get('AdviceResourceCount') is not None:
            self.advice_resource_count = m.get('AdviceResourceCount')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('CurrentCost') is not None:
            self.current_cost = m.get('CurrentCost')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpectedSavingCost') is not None:
            self.expected_saving_cost = m.get('ExpectedSavingCost')

        if m.get('OptimizedCost') is not None:
            self.optimized_cost = m.get('OptimizedCost')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Tips') is not None:
            self.tips = m.get('Tips')

        return self

