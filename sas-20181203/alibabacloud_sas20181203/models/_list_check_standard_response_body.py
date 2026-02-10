# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCheckStandardResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        standards: List[main_models.ListCheckStandardResponseBodyStandards] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The standards.
        self.standards = standards

    def validate(self):
        if self.standards:
            for v1 in self.standards:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Standards'] = []
        if self.standards is not None:
            for k1 in self.standards:
                result['Standards'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.standards = []
        if m.get('Standards') is not None:
            for k1 in m.get('Standards'):
                temp_model = main_models.ListCheckStandardResponseBodyStandards()
                self.standards.append(temp_model.from_map(k1))

        return self

class ListCheckStandardResponseBodyStandards(DaraModel):
    def __init__(
        self,
        bind_vendor: int = None,
        id: int = None,
        requirements: List[main_models.ListCheckStandardResponseBodyStandardsRequirements] = None,
        show_name: str = None,
        show_priority_level: int = None,
        type: str = None,
    ):
        # The cloud service provider that uses the standard. Valid values:
        # 
        # *   **0**: Alibaba Cloud.
        # *   **3**: Tencent Cloud.
        # *   **4**: Huawei Cloud.
        # *   **5**: Microsoft Azure.
        # *   **7**: AWS.
        self.bind_vendor = bind_vendor
        # The ID of the standard.
        self.id = id
        # The requirements.
        self.requirements = requirements
        # The display name of the check item.
        self.show_name = show_name
        # The priority for display.
        self.show_priority_level = show_priority_level
        # The type of the standard.
        self.type = type

    def validate(self):
        if self.requirements:
            for v1 in self.requirements:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_vendor is not None:
            result['BindVendor'] = self.bind_vendor

        if self.id is not None:
            result['Id'] = self.id

        result['Requirements'] = []
        if self.requirements is not None:
            for k1 in self.requirements:
                result['Requirements'].append(k1.to_map() if k1 else None)

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.show_priority_level is not None:
            result['ShowPriorityLevel'] = self.show_priority_level

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindVendor') is not None:
            self.bind_vendor = m.get('BindVendor')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.requirements = []
        if m.get('Requirements') is not None:
            for k1 in m.get('Requirements'):
                temp_model = main_models.ListCheckStandardResponseBodyStandardsRequirements()
                self.requirements.append(temp_model.from_map(k1))

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('ShowPriorityLevel') is not None:
            self.show_priority_level = m.get('ShowPriorityLevel')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListCheckStandardResponseBodyStandardsRequirements(DaraModel):
    def __init__(
        self,
        id: int = None,
        risk_check_count: int = None,
        show_name: str = None,
        show_priority_level: int = None,
    ):
        # The ID of the requirement.
        self.id = id
        # The number of check items in the requirement.
        self.risk_check_count = risk_check_count
        # The display name of the search condition.
        self.show_name = show_name
        # The priority for display.
        self.show_priority_level = show_priority_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.risk_check_count is not None:
            result['RiskCheckCount'] = self.risk_check_count

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.show_priority_level is not None:
            result['ShowPriorityLevel'] = self.show_priority_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RiskCheckCount') is not None:
            self.risk_check_count = m.get('RiskCheckCount')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('ShowPriorityLevel') is not None:
            self.show_priority_level = m.get('ShowPriorityLevel')

        return self

