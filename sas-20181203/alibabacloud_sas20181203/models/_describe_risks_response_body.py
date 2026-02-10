# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeRisksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risks: List[main_models.DescribeRisksResponseBodyRisks] = None,
        total_count: int = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The baselines.
        self.risks = risks
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.risks:
            for v1 in self.risks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Risks'] = []
        if self.risks is not None:
            for k1 in self.risks:
                result['Risks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.risks = []
        if m.get('Risks') is not None:
            for k1 in m.get('Risks'):
                temp_model = main_models.DescribeRisksResponseBodyRisks()
                self.risks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRisksResponseBodyRisks(DaraModel):
    def __init__(
        self,
        risk_detail: str = None,
        risk_id: int = None,
        risk_name: str = None,
        risk_type: str = None,
        sub_risk_type: str = None,
        sub_type_alias: str = None,
        type_alias: str = None,
    ):
        # The description of the baseline.
        self.risk_detail = risk_detail
        # The baseline ID.
        self.risk_id = risk_id
        # The name of the baseline.
        self.risk_name = risk_name
        # The name of the baseline type.
        self.risk_type = risk_type
        # The name of the baseline subtype.
        self.sub_risk_type = sub_risk_type
        # The display name of the baseline subtype.
        self.sub_type_alias = sub_type_alias
        # The display name of the baseline type.
        self.type_alias = type_alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.risk_detail is not None:
            result['RiskDetail'] = self.risk_detail

        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.risk_name is not None:
            result['RiskName'] = self.risk_name

        if self.risk_type is not None:
            result['RiskType'] = self.risk_type

        if self.sub_risk_type is not None:
            result['SubRiskType'] = self.sub_risk_type

        if self.sub_type_alias is not None:
            result['SubTypeAlias'] = self.sub_type_alias

        if self.type_alias is not None:
            result['TypeAlias'] = self.type_alias

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskDetail') is not None:
            self.risk_detail = m.get('RiskDetail')

        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('RiskName') is not None:
            self.risk_name = m.get('RiskName')

        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')

        if m.get('SubRiskType') is not None:
            self.sub_risk_type = m.get('SubRiskType')

        if m.get('SubTypeAlias') is not None:
            self.sub_type_alias = m.get('SubTypeAlias')

        if m.get('TypeAlias') is not None:
            self.type_alias = m.get('TypeAlias')

        return self

