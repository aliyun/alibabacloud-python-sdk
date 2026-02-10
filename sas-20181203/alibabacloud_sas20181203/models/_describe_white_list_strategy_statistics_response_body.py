# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeWhiteListStrategyStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        strategies: List[main_models.DescribeWhiteListStrategyStatisticsResponseBodyStrategies] = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The statistics of the policies.
        self.strategies = strategies
        # The total number of entries returned.
        self.total_count = total_count

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
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Strategies'] = []
        if self.strategies is not None:
            for k1 in self.strategies:
                result['Strategies'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.strategies = []
        if m.get('Strategies') is not None:
            for k1 in m.get('Strategies'):
                temp_model = main_models.DescribeWhiteListStrategyStatisticsResponseBodyStrategies()
                self.strategies.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeWhiteListStrategyStatisticsResponseBodyStrategies(DaraModel):
    def __init__(
        self,
        asset_count: int = None,
        progress: int = None,
        status: int = None,
        strategy_id: int = None,
        strategy_name: str = None,
        study_time: int = None,
        suspicious_proc_count: int = None,
        trust_proc_count: int = None,
        virus_proc_count: int = None,
    ):
        # The number of the servers on which the policy takes effect.
        self.asset_count = asset_count
        # The learning progress of the policy. Unit: percent (%).
        self.progress = progress
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
        # The number of suspicious processes.
        self.suspicious_proc_count = suspicious_proc_count
        # The number of trusted processes.
        self.trust_proc_count = trust_proc_count
        # The number of malicious processes.
        self.virus_proc_count = virus_proc_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_count is not None:
            result['AssetCount'] = self.asset_count

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.study_time is not None:
            result['StudyTime'] = self.study_time

        if self.suspicious_proc_count is not None:
            result['SuspiciousProcCount'] = self.suspicious_proc_count

        if self.trust_proc_count is not None:
            result['TrustProcCount'] = self.trust_proc_count

        if self.virus_proc_count is not None:
            result['VirusProcCount'] = self.virus_proc_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetCount') is not None:
            self.asset_count = m.get('AssetCount')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('StudyTime') is not None:
            self.study_time = m.get('StudyTime')

        if m.get('SuspiciousProcCount') is not None:
            self.suspicious_proc_count = m.get('SuspiciousProcCount')

        if m.get('TrustProcCount') is not None:
            self.trust_proc_count = m.get('TrustProcCount')

        if m.get('VirusProcCount') is not None:
            self.virus_proc_count = m.get('VirusProcCount')

        return self

