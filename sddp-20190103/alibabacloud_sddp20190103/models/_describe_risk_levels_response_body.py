# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeRiskLevelsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risk_level_list: List[main_models.DescribeRiskLevelsResponseBodyRiskLevelList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of sensitivity levels.
        self.risk_level_list = risk_level_list

    def validate(self):
        if self.risk_level_list:
            for v1 in self.risk_level_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RiskLevelList'] = []
        if self.risk_level_list is not None:
            for k1 in self.risk_level_list:
                result['RiskLevelList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.risk_level_list = []
        if m.get('RiskLevelList') is not None:
            for k1 in m.get('RiskLevelList'):
                temp_model = main_models.DescribeRiskLevelsResponseBodyRiskLevelList()
                self.risk_level_list.append(temp_model.from_map(k1))

        return self

class DescribeRiskLevelsResponseBodyRiskLevelList(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
        reference_num: int = None,
    ):
        # The description of the sensitivity level. You can enter a custom description.
        # 
        # The following list describes the sensitivity level names and the corresponding default description:
        # 
        # *   **NA**: which indicates that no sensitive data is detected.
        # *   **S1**: which indicates the sensitive data at sensitivity level 1.
        # *   **S2**: which indicates the sensitive data at sensitivity level 2.
        # *   **S3**: which indicates the sensitive data at sensitivity level 3.
        # *   **S4**: which indicates the sensitive data at sensitivity level 4.
        # *   **S5**: which indicates the sensitive data at sensitivity level 5.
        # *   **S6**: which indicates the sensitive data at sensitivity level 6.
        # *   **S7**: which indicates the sensitive data at sensitivity level 7.
        # *   **S8**: which indicates the sensitive data at sensitivity level 8.
        # *   **S9**: which indicates the sensitive data at sensitivity level 9.
        # *   **S10**: which indicates the sensitive data at sensitivity level 10.
        self.description = description
        # The unique ID of the sensitivity level. Valid values: 1 to 11. Each sensitivity level ID maps a sensitivity level. For example, the sensitivity level ID of 2 corresponds to the sensitivity level S1.
        # 
        # For more information, see the description of the Name parameter.
        self.id = id
        # The name of the sensitivity level. The highest sensitivity level varies based on rule templates. The highest sensitivity level is S10. The highest sensitivity level of the **Built-in data security classification templates for Alibaba and Ant Group** is S4, and that of the **built-in classification templates for financial data** and **built-in classification templates for assets** is S5. For more information about the built-in classification templates for financial data, see Guidelines for Security Classification of Financial Data and Security Data - JRT 0197-2020. For a copied rule template, the highest sensitivity level is S10. The following list describes the sensitivity level names and the corresponding IDs:
        # 
        # *   **NA**: 1
        # *   **S1**: 2
        # *   **S2**: 3
        # *   **S3**: 4
        # *   **S4**: 5
        # *   **S5**: 6
        # *   **S6**: 7
        # *   **S7**: 8
        # *   **S8**: 9
        # *   **S9**: 10
        # *   **S10**: 11
        self.name = name
        # The number of times that each sensitivity level is referenced in the rule template. Default value: 0.
        self.reference_num = reference_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.reference_num is not None:
            result['ReferenceNum'] = self.reference_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ReferenceNum') is not None:
            self.reference_num = m.get('ReferenceNum')

        return self

