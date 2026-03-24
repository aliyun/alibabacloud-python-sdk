# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageBaselineStrategyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        strategy: main_models.DescribeImageBaselineStrategyResponseBodyStrategy = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the baseline check policy.
        self.strategy = strategy

    def validate(self):
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Strategy') is not None:
            temp_model = main_models.DescribeImageBaselineStrategyResponseBodyStrategy()
            self.strategy = temp_model.from_map(m.get('Strategy'))

        return self

class DescribeImageBaselineStrategyResponseBodyStrategy(DaraModel):
    def __init__(
        self,
        baseline_item: str = None,
        baseline_item_list: List[main_models.DescribeImageBaselineStrategyResponseBodyStrategyBaselineItemList] = None,
        image_vul_clean: int = None,
        selected_item_count: int = None,
        strategy_id: int = None,
        strategy_name: str = None,
        total_item_count: int = None,
        type: str = None,
    ):
        # The baseline check policy for agentless detection.
        self.baseline_item = baseline_item
        # An array that contains the baselines.
        self.baseline_item_list = baseline_item_list
        self.image_vul_clean = image_vul_clean
        # The number of selected baseline check items.
        self.selected_item_count = selected_item_count
        # The ID of the baseline check policy.
        self.strategy_id = strategy_id
        # The name of the baseline check policy.
        self.strategy_name = strategy_name
        # The total number of baseline check items.
        self.total_item_count = total_item_count
        # The type of the baseline check policy. Valid values:
        # 
        # *   **default**: the default policy
        # *   **full**: a policy that uses all baselines
        # *   **normal**: a policy that uses general baselines
        self.type = type

    def validate(self):
        if self.baseline_item_list:
            for v1 in self.baseline_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_item is not None:
            result['BaselineItem'] = self.baseline_item

        result['BaselineItemList'] = []
        if self.baseline_item_list is not None:
            for k1 in self.baseline_item_list:
                result['BaselineItemList'].append(k1.to_map() if k1 else None)

        if self.image_vul_clean is not None:
            result['ImageVulClean'] = self.image_vul_clean

        if self.selected_item_count is not None:
            result['SelectedItemCount'] = self.selected_item_count

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.total_item_count is not None:
            result['TotalItemCount'] = self.total_item_count

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineItem') is not None:
            self.baseline_item = m.get('BaselineItem')

        self.baseline_item_list = []
        if m.get('BaselineItemList') is not None:
            for k1 in m.get('BaselineItemList'):
                temp_model = main_models.DescribeImageBaselineStrategyResponseBodyStrategyBaselineItemList()
                self.baseline_item_list.append(temp_model.from_map(k1))

        if m.get('ImageVulClean') is not None:
            self.image_vul_clean = m.get('ImageVulClean')

        if m.get('SelectedItemCount') is not None:
            self.selected_item_count = m.get('SelectedItemCount')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('TotalItemCount') is not None:
            self.total_item_count = m.get('TotalItemCount')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeImageBaselineStrategyResponseBodyStrategyBaselineItemList(DaraModel):
    def __init__(
        self,
        class_key: str = None,
        item_key: str = None,
        name_key: str = None,
    ):
        # The key of the baseline type.
        self.class_key = class_key
        # The key of the baseline check item.
        self.item_key = item_key
        # The key of the name for the baseline.
        self.name_key = name_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_key is not None:
            result['ClassKey'] = self.class_key

        if self.item_key is not None:
            result['ItemKey'] = self.item_key

        if self.name_key is not None:
            result['NameKey'] = self.name_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassKey') is not None:
            self.class_key = m.get('ClassKey')

        if m.get('ItemKey') is not None:
            self.item_key = m.get('ItemKey')

        if m.get('NameKey') is not None:
            self.name_key = m.get('NameKey')

        return self

