# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeCfwRiskLevelSummaryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risk_list: List[main_models.DescribeCfwRiskLevelSummaryResponseBodyRiskList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The list of risks.
        self.risk_list = risk_list

    def validate(self):
        if self.risk_list:
            for v1 in self.risk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RiskList'] = []
        if self.risk_list is not None:
            for k1 in self.risk_list:
                result['RiskList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.risk_list = []
        if m.get('RiskList') is not None:
            for k1 in m.get('RiskList'):
                temp_model = main_models.DescribeCfwRiskLevelSummaryResponseBodyRiskList()
                self.risk_list.append(temp_model.from_map(k1))

        return self

class DescribeCfwRiskLevelSummaryResponseBodyRiskList(DaraModel):
    def __init__(
        self,
        level: str = None,
        num: str = None,
        type: str = None,
    ):
        # The risk levels. Valid values:
        # 
        # *   **medium**
        self.level = level
        # The number of at-risk Elastic Compute Service (ECS) instances.
        self.num = num
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['Level'] = self.level

        if self.num is not None:
            result['Num'] = self.num

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

