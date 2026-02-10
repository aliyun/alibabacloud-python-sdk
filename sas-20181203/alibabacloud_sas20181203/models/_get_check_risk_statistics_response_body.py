# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCheckRiskStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        data: List[main_models.GetCheckRiskStatisticsResponseBodyData] = None,
        request_id: str = None,
        summary: main_models.GetCheckRiskStatisticsResponseBodySummary = None,
    ):
        # The number of risk scenarios.
        self.count = count
        # An array consisting of the statistics on check items that are used in risk scenarios.
        self.data = data
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Historical check item statistics.
        self.summary = summary

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.summary is not None:
            result['Summary'] = self.summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetCheckRiskStatisticsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Summary') is not None:
            temp_model = main_models.GetCheckRiskStatisticsResponseBodySummary()
            self.summary = temp_model.from_map(m.get('Summary'))

        return self

class GetCheckRiskStatisticsResponseBodySummary(DaraModel):
    def __init__(
        self,
        handled_check_today: int = None,
        handled_check_total: int = None,
        handled_days: int = None,
        risk_check_cnt: int = None,
        risk_days: int = None,
        risk_warning_cnt: int = None,
    ):
        # Check items handled today.
        self.handled_check_today = handled_check_today
        # A risk item exists.
        self.handled_check_total = handled_check_total
        # Total days since check items were handled.
        self.handled_days = handled_days
        # Check items that failed to pass the check.
        self.risk_check_cnt = risk_check_cnt
        # Days since check items failed.
        self.risk_days = risk_days
        # Risks to be handled.
        self.risk_warning_cnt = risk_warning_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.handled_check_today is not None:
            result['HandledCheckToday'] = self.handled_check_today

        if self.handled_check_total is not None:
            result['HandledCheckTotal'] = self.handled_check_total

        if self.handled_days is not None:
            result['HandledDays'] = self.handled_days

        if self.risk_check_cnt is not None:
            result['RiskCheckCnt'] = self.risk_check_cnt

        if self.risk_days is not None:
            result['RiskDays'] = self.risk_days

        if self.risk_warning_cnt is not None:
            result['RiskWarningCnt'] = self.risk_warning_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandledCheckToday') is not None:
            self.handled_check_today = m.get('HandledCheckToday')

        if m.get('HandledCheckTotal') is not None:
            self.handled_check_total = m.get('HandledCheckTotal')

        if m.get('HandledDays') is not None:
            self.handled_days = m.get('HandledDays')

        if m.get('RiskCheckCnt') is not None:
            self.risk_check_cnt = m.get('RiskCheckCnt')

        if m.get('RiskDays') is not None:
            self.risk_days = m.get('RiskDays')

        if m.get('RiskWarningCnt') is not None:
            self.risk_warning_cnt = m.get('RiskWarningCnt')

        return self

class GetCheckRiskStatisticsResponseBodyData(DaraModel):
    def __init__(
        self,
        high_warning_count: int = None,
        low_warning_count: int = None,
        medium_warning_count: int = None,
        pass_count: int = None,
        scene_name: str = None,
        sub_statistics: List[main_models.GetCheckRiskStatisticsResponseBodyDataSubStatistics] = None,
        total_count: int = None,
    ):
        # The number of high-risk items.
        self.high_warning_count = high_warning_count
        # The number of low-risk items.
        self.low_warning_count = low_warning_count
        # The number of medium-risk items.
        self.medium_warning_count = medium_warning_count
        # The number of passed check items.
        self.pass_count = pass_count
        # The name of the risk scenario.
        self.scene_name = scene_name
        # The statistics on check items that are used in the risk scenario by baseline type.
        self.sub_statistics = sub_statistics
        # The total number of check items.
        self.total_count = total_count

    def validate(self):
        if self.sub_statistics:
            for v1 in self.sub_statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.high_warning_count is not None:
            result['HighWarningCount'] = self.high_warning_count

        if self.low_warning_count is not None:
            result['LowWarningCount'] = self.low_warning_count

        if self.medium_warning_count is not None:
            result['MediumWarningCount'] = self.medium_warning_count

        if self.pass_count is not None:
            result['PassCount'] = self.pass_count

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        result['SubStatistics'] = []
        if self.sub_statistics is not None:
            for k1 in self.sub_statistics:
                result['SubStatistics'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HighWarningCount') is not None:
            self.high_warning_count = m.get('HighWarningCount')

        if m.get('LowWarningCount') is not None:
            self.low_warning_count = m.get('LowWarningCount')

        if m.get('MediumWarningCount') is not None:
            self.medium_warning_count = m.get('MediumWarningCount')

        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        self.sub_statistics = []
        if m.get('SubStatistics') is not None:
            for k1 in m.get('SubStatistics'):
                temp_model = main_models.GetCheckRiskStatisticsResponseBodyDataSubStatistics()
                self.sub_statistics.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetCheckRiskStatisticsResponseBodyDataSubStatistics(DaraModel):
    def __init__(
        self,
        alias: str = None,
        high_warning_count: int = None,
        low_warning_count: int = None,
        medium_warning_count: int = None,
        pass_count: int = None,
        total_count: int = None,
        type_name: str = None,
    ):
        # The name of the baseline type.
        self.alias = alias
        # The number of high-risk items.
        self.high_warning_count = high_warning_count
        # The number of low-risk items.
        self.low_warning_count = low_warning_count
        # The number of medium-risk items.
        self.medium_warning_count = medium_warning_count
        # The number of passed check items.
        self.pass_count = pass_count
        # The total number of check items.
        self.total_count = total_count
        # The baseline type.
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.high_warning_count is not None:
            result['HighWarningCount'] = self.high_warning_count

        if self.low_warning_count is not None:
            result['LowWarningCount'] = self.low_warning_count

        if self.medium_warning_count is not None:
            result['MediumWarningCount'] = self.medium_warning_count

        if self.pass_count is not None:
            result['PassCount'] = self.pass_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('HighWarningCount') is not None:
            self.high_warning_count = m.get('HighWarningCount')

        if m.get('LowWarningCount') is not None:
            self.low_warning_count = m.get('LowWarningCount')

        if m.get('MediumWarningCount') is not None:
            self.medium_warning_count = m.get('MediumWarningCount')

        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

