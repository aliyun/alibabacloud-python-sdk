# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class GetRiskLevelDistributionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        time_list: List[main_models.GetRiskLevelDistributionResponseBodyTimeList] = None,
    ):
        self.request_id = request_id
        self.time_list = time_list

    def validate(self):
        if self.time_list:
            for v1 in self.time_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TimeList'] = []
        if self.time_list is not None:
            for k1 in self.time_list:
                result['TimeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.time_list = []
        if m.get('TimeList') is not None:
            for k1 in m.get('TimeList'):
                temp_model = main_models.GetRiskLevelDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k1))

        return self

class GetRiskLevelDistributionResponseBodyTimeList(DaraModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        high_risk_count: int = None,
        low_risk_count: int = None,
        middle_risk_count: int = None,
        risk_count: int = None,
    ):
        self.begin_date = begin_date
        self.end_date = end_date
        self.high_risk_count = high_risk_count
        self.low_risk_count = low_risk_count
        self.middle_risk_count = middle_risk_count
        self.risk_count = risk_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.high_risk_count is not None:
            result['HighRiskCount'] = self.high_risk_count

        if self.low_risk_count is not None:
            result['LowRiskCount'] = self.low_risk_count

        if self.middle_risk_count is not None:
            result['MiddleRiskCount'] = self.middle_risk_count

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('HighRiskCount') is not None:
            self.high_risk_count = m.get('HighRiskCount')

        if m.get('LowRiskCount') is not None:
            self.low_risk_count = m.get('LowRiskCount')

        if m.get('MiddleRiskCount') is not None:
            self.middle_risk_count = m.get('MiddleRiskCount')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        return self

