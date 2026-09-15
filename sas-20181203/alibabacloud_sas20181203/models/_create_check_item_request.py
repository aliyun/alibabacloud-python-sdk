# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateCheckItemRequest(DaraModel):
    def __init__(
        self,
        assist_info: main_models.CreateCheckItemRequestAssistInfo = None,
        check_rule: str = None,
        check_show_name: str = None,
        description: main_models.CreateCheckItemRequestDescription = None,
        instance_sub_type: str = None,
        instance_type: str = None,
        remark: str = None,
        risk_level: str = None,
        section_ids: List[int] = None,
        solution: main_models.CreateCheckItemRequestSolution = None,
        status: str = None,
        vendor: str = None,
    ):
        # The help information of the check item.
        self.assist_info = assist_info
        # The rule definition of the custom check item.
        # 
        # This parameter is required.
        self.check_rule = check_rule
        # The name of the custom check item.
        # 
        # This parameter is required.
        self.check_show_name = check_show_name
        # The description of the check item.
        self.description = description
        # The asset subtype of the cloud service.
        # > You can call the [ListCloudAssetSchemas](~~ListCloudAssetSchemas~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_sub_type = instance_sub_type
        # The asset type of the cloud service.
        # > You can call the [ListCloudAssetSchemas](~~ListCloudAssetSchemas~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The remarks.
        self.remark = remark
        # The risk level of the check item. Valid values:
        # - **HIGH**: High risk.
        # - **MEDIUM**: Medium risk.
        # - **LOW**: Low risk.
        # 
        # This parameter is required.
        self.risk_level = risk_level
        # The IDs of the sections associated with the check item.
        # 
        # This parameter is required.
        self.section_ids = section_ids
        # The solution information of the check item.
        self.solution = solution
        # The status of the check item. Valid values:
        # - **EDIT**: Being edited.
        # - **RELEASE**: Published.
        # 
        # > - Changing the status from **Published** to **Being edited** will purge all historical records.
        # > - Only check items in the **Published** status can be used for checks.
        # 
        # This parameter is required.
        self.status = status
        # The cloud asset vendor.
        # > You can call the [ListCloudAssetSchemas](~~ListCloudAssetSchemas~~) operation to obtain the available vendors.
        # 
        # This parameter is required.
        self.vendor = vendor

    def validate(self):
        if self.assist_info:
            self.assist_info.validate()
        if self.description:
            self.description.validate()
        if self.solution:
            self.solution.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assist_info is not None:
            result['AssistInfo'] = self.assist_info.to_map()

        if self.check_rule is not None:
            result['CheckRule'] = self.check_rule

        if self.check_show_name is not None:
            result['CheckShowName'] = self.check_show_name

        if self.description is not None:
            result['Description'] = self.description.to_map()

        if self.instance_sub_type is not None:
            result['InstanceSubType'] = self.instance_sub_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.section_ids is not None:
            result['SectionIds'] = self.section_ids

        if self.solution is not None:
            result['Solution'] = self.solution.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssistInfo') is not None:
            temp_model = main_models.CreateCheckItemRequestAssistInfo()
            self.assist_info = temp_model.from_map(m.get('AssistInfo'))

        if m.get('CheckRule') is not None:
            self.check_rule = m.get('CheckRule')

        if m.get('CheckShowName') is not None:
            self.check_show_name = m.get('CheckShowName')

        if m.get('Description') is not None:
            temp_model = main_models.CreateCheckItemRequestDescription()
            self.description = temp_model.from_map(m.get('Description'))

        if m.get('InstanceSubType') is not None:
            self.instance_sub_type = m.get('InstanceSubType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SectionIds') is not None:
            self.section_ids = m.get('SectionIds')

        if m.get('Solution') is not None:
            temp_model = main_models.CreateCheckItemRequestSolution()
            self.solution = temp_model.from_map(m.get('Solution'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class CreateCheckItemRequestSolution(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of the check item solution information. Valid values:
        # 
        # - **text**: text
        self.type = type
        # The content of the solution for the check item risk.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateCheckItemRequestDescription(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of the check item description. Valid values:
        # 
        # - **text**: text
        self.type = type
        # The content of the description.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateCheckItemRequestAssistInfo(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of the help information for the check item risk. Valid values:
        # 
        # - **text**: text
        self.type = type
        # The content of the help information for the check item risk.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

