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
        # A list of risk levels.
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
        # The description of the risk level. You can customize the description.
        # 
        # The following list describes the mappings between risk level names and their default descriptions:
        # 
        # - **NA**: No sensitive data is detected
        # 
        # - **S1**: Level-1 sensitive data
        # 
        # - **S2**: Level-2 sensitive data
        # 
        # - **S3**: Level-3 sensitive data
        # 
        # - **S4**: Level-4 sensitive data
        # 
        # - **S5**: Level-5 sensitive data
        # 
        # - **S6**: Level-6 sensitive data
        # 
        # - **S7**: Level-7 sensitive data
        # 
        # - **S8**: Level-8 sensitive data
        # 
        # - **S9**: Level-9 sensitive data
        # 
        # - **S10**: Level-10 sensitive data
        self.description = description
        # The unique ID of the risk level. Valid values: 1 to 11. Each risk level ID corresponds to a risk level name. For example, the risk level ID 2 corresponds to the risk level S1.
        # 
        # For more information about the mappings, see the description of the Name parameter.
        self.id = id
        # The name of the risk level for the sensitive data. The maximum risk level is S10 and varies based on the data classification template. The maximum risk level is S4 for the **built-in data security classification template for Alibaba and Ant Group**, and S5 for the **built-in data classification template for the finance industry (with reference to JR/T 0197-2020 Financial Data Security - Guidelines for Data Security Classification)** and the **built-in data classification standard for the energy industry**. If you use a copied template, the maximum risk level is S10.
        # The following list describes the mappings between risk level names and IDs:
        # 
        # - **NA**: 1
        # 
        # - **S1**: 2
        # 
        # - **S2**: 3
        # 
        # - **S3**: 4
        # 
        # - **S4**: 5
        # 
        # - **S5**: 6
        # 
        # - **S6**: 7
        # 
        # - **S7**: 8
        # 
        # - **S8**: 9
        # 
        # - **S9**: 10
        # 
        # - **S10**: 11
        self.name = name
        # The number of times the risk level is referenced in the template. The default value is 0.
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

