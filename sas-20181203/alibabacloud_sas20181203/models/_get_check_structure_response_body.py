# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCheckStructureResponseBody(DaraModel):
    def __init__(
        self,
        check_structure_response: List[main_models.GetCheckStructureResponseBodyCheckStructureResponse] = None,
        request_id: str = None,
    ):
        # The structure information about check items provided by the configuration assessment feature.
        self.check_structure_response = check_structure_response
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.check_structure_response:
            for v1 in self.check_structure_response:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckStructureResponse'] = []
        if self.check_structure_response is not None:
            for k1 in self.check_structure_response:
                result['CheckStructureResponse'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_structure_response = []
        if m.get('CheckStructureResponse') is not None:
            for k1 in m.get('CheckStructureResponse'):
                temp_model = main_models.GetCheckStructureResponseBodyCheckStructureResponse()
                self.check_structure_response.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCheckStructureResponseBodyCheckStructureResponse(DaraModel):
    def __init__(
        self,
        standard_type: str = None,
        standards: List[main_models.GetCheckStructureResponseBodyCheckStructureResponseStandards] = None,
    ):
        # The type of the check item.
        # 
        # *   RISK: security risk.
        # *   IDENTITY_PERMISSION: Cloud Infrastructure Entitlement Management (CIEM).
        # *   COMPLIANCE: security compliance.
        self.standard_type = standard_type
        # The structure information about the check items of the business type.
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
        if self.standard_type is not None:
            result['StandardType'] = self.standard_type

        result['Standards'] = []
        if self.standards is not None:
            for k1 in self.standards:
                result['Standards'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandardType') is not None:
            self.standard_type = m.get('StandardType')

        self.standards = []
        if m.get('Standards') is not None:
            for k1 in m.get('Standards'):
                temp_model = main_models.GetCheckStructureResponseBodyCheckStructureResponseStandards()
                self.standards.append(temp_model.from_map(k1))

        return self

class GetCheckStructureResponseBodyCheckStructureResponseStandards(DaraModel):
    def __init__(
        self,
        id: int = None,
        requirements: List[main_models.GetCheckStructureResponseBodyCheckStructureResponseStandardsRequirements] = None,
        show_name: str = None,
        type: str = None,
    ):
        # The standard ID of the check item.
        self.id = id
        # The standards of the check items.
        self.requirements = requirements
        # The display name of the standard for the check item.
        self.show_name = show_name
        # The standard type of the check item. Valid values:
        # 
        # *   RISK: security risk.
        # *   IDENTITY_PERMISSION: CIEM.
        # *   COMPLIANCE: security compliance.
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
        if self.id is not None:
            result['Id'] = self.id

        result['Requirements'] = []
        if self.requirements is not None:
            for k1 in self.requirements:
                result['Requirements'].append(k1.to_map() if k1 else None)

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.requirements = []
        if m.get('Requirements') is not None:
            for k1 in m.get('Requirements'):
                temp_model = main_models.GetCheckStructureResponseBodyCheckStructureResponseStandardsRequirements()
                self.requirements.append(temp_model.from_map(k1))

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetCheckStructureResponseBodyCheckStructureResponseStandardsRequirements(DaraModel):
    def __init__(
        self,
        id: int = None,
        sections: List[main_models.GetCheckStructureResponseBodyCheckStructureResponseStandardsRequirementsSections] = None,
        show_name: str = None,
        total_check_count: int = None,
    ):
        # The ID of the requirement item for the check item.
        self.id = id
        # The information about the sections of check items.
        self.sections = sections
        # The display name of the requirement item for the check item.
        self.show_name = show_name
        # The total number of check items for the requirement.
        self.total_check_count = total_check_count

    def validate(self):
        if self.sections:
            for v1 in self.sections:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        result['Sections'] = []
        if self.sections is not None:
            for k1 in self.sections:
                result['Sections'].append(k1.to_map() if k1 else None)

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.total_check_count is not None:
            result['TotalCheckCount'] = self.total_check_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.sections = []
        if m.get('Sections') is not None:
            for k1 in m.get('Sections'):
                temp_model = main_models.GetCheckStructureResponseBodyCheckStructureResponseStandardsRequirementsSections()
                self.sections.append(temp_model.from_map(k1))

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('TotalCheckCount') is not None:
            self.total_check_count = m.get('TotalCheckCount')

        return self

class GetCheckStructureResponseBodyCheckStructureResponseStandardsRequirementsSections(DaraModel):
    def __init__(
        self,
        id: int = None,
        show_name: str = None,
    ):
        # The ID of the section for the check item.
        self.id = id
        # The display name of the section for the check item.
        self.show_name = show_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        return self

