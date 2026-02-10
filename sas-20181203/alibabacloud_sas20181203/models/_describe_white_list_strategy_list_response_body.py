# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeWhiteListStrategyListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        strategies: List[main_models.DescribeWhiteListStrategyListResponseBodyStrategies] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the policies.
        self.strategies = strategies

    def validate(self):
        if self.strategies:
            for v1 in self.strategies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Strategies'] = []
        if self.strategies is not None:
            for k1 in self.strategies:
                result['Strategies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.strategies = []
        if m.get('Strategies') is not None:
            for k1 in m.get('Strategies'):
                temp_model = main_models.DescribeWhiteListStrategyListResponseBodyStrategies()
                self.strategies.append(temp_model.from_map(k1))

        return self

class DescribeWhiteListStrategyListResponseBodyStrategies(DaraModel):
    def __init__(
        self,
        status: int = None,
        strategy_id: int = None,
        strategy_name: str = None,
        study_time: int = None,
    ):
        # The status of the policy. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: learning
        # *   **2**: paused
        # *   **3**: learning completed
        # *   **4**: enabled
        self.status = status
        # The ID of the policy.
        self.strategy_id = strategy_id
        # The name of the policy.
        self.strategy_name = strategy_name
        # The intelligent learning duration. Unit: hour.
        self.study_time = study_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.study_time is not None:
            result['StudyTime'] = self.study_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('StudyTime') is not None:
            self.study_time = m.get('StudyTime')

        return self

