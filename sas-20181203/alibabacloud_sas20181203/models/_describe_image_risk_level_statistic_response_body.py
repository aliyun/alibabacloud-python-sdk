# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageRiskLevelStatisticResponseBody(DaraModel):
    def __init__(
        self,
        image_risk_level_list: List[main_models.DescribeImageRiskLevelStatisticResponseBodyImageRiskLevelList] = None,
        request_id: str = None,
    ):
        # The information about risks at the image level. The risks include vulnerabilities, baselines risks, and malicious file risks.
        self.image_risk_level_list = image_risk_level_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.image_risk_level_list:
            for v1 in self.image_risk_level_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageRiskLevelList'] = []
        if self.image_risk_level_list is not None:
            for k1 in self.image_risk_level_list:
                result['ImageRiskLevelList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_risk_level_list = []
        if m.get('ImageRiskLevelList') is not None:
            for k1 in m.get('ImageRiskLevelList'):
                temp_model = main_models.DescribeImageRiskLevelStatisticResponseBodyImageRiskLevelList()
                self.image_risk_level_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageRiskLevelStatisticResponseBodyImageRiskLevelList(DaraModel):
    def __init__(
        self,
        cnt: int = None,
        image_risk_level: str = None,
    ):
        # The number of images at the risk level.
        self.cnt = cnt
        # The risk level of the image. Valid values:
        # 
        # *   **3**: high risk.
        # *   **2**: medium risk.
        # *   **1**: low risk.
        # *   **0**: no risk.
        self.image_risk_level = image_risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cnt is not None:
            result['Cnt'] = self.cnt

        if self.image_risk_level is not None:
            result['ImageRiskLevel'] = self.image_risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cnt') is not None:
            self.cnt = m.get('Cnt')

        if m.get('ImageRiskLevel') is not None:
            self.image_risk_level = m.get('ImageRiskLevel')

        return self

