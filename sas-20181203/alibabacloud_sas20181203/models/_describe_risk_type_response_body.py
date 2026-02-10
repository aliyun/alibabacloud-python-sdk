# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeRiskTypeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risk_types: List[main_models.DescribeRiskTypeResponseBodyRiskTypes] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the information about baseline types.
        self.risk_types = risk_types

    def validate(self):
        if self.risk_types:
            for v1 in self.risk_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RiskTypes'] = []
        if self.risk_types is not None:
            for k1 in self.risk_types:
                result['RiskTypes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.risk_types = []
        if m.get('RiskTypes') is not None:
            for k1 in m.get('RiskTypes'):
                temp_model = main_models.DescribeRiskTypeResponseBodyRiskTypes()
                self.risk_types.append(temp_model.from_map(k1))

        return self

class DescribeRiskTypeResponseBodyRiskTypes(DaraModel):
    def __init__(
        self,
        alias: str = None,
        auth_flag: bool = None,
        sub_types: List[main_models.DescribeRiskTypeResponseBodyRiskTypesSubTypes] = None,
        type_name: str = None,
    ):
        # The alias of the baseline type.
        self.alias = alias
        # The baseline type flag of the current user version. Valid values:
        # 
        # - **true**: Have access
        # - **false**: No permissions
        self.auth_flag = auth_flag
        # An array that consists of the information about baseline subtypes.
        self.sub_types = sub_types
        # The name of the baseline type.
        self.type_name = type_name

    def validate(self):
        if self.sub_types:
            for v1 in self.sub_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.auth_flag is not None:
            result['AuthFlag'] = self.auth_flag

        result['SubTypes'] = []
        if self.sub_types is not None:
            for k1 in self.sub_types:
                result['SubTypes'].append(k1.to_map() if k1 else None)

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('AuthFlag') is not None:
            self.auth_flag = m.get('AuthFlag')

        self.sub_types = []
        if m.get('SubTypes') is not None:
            for k1 in m.get('SubTypes'):
                temp_model = main_models.DescribeRiskTypeResponseBodyRiskTypesSubTypes()
                self.sub_types.append(temp_model.from_map(k1))

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

class DescribeRiskTypeResponseBodyRiskTypesSubTypes(DaraModel):
    def __init__(
        self,
        alias: str = None,
        auth_flag: bool = None,
        check_details: List[main_models.DescribeRiskTypeResponseBodyRiskTypesSubTypesCheckDetails] = None,
        supported_os: str = None,
        type_name: str = None,
    ):
        # The alias of the baseline subtype.
        self.alias = alias
        # The baseline subtype permission flag of the current user version. Valid values:
        # 
        # - **true**: Have access
        # - **false**: No permissions
        self.auth_flag = auth_flag
        # An array that consists of the check details about the baseline subtype.
        self.check_details = check_details
        # The operating system type of the server. Valid values:
        # 
        # - **windows**
        # - **linux**
        self.supported_os = supported_os
        # The name of the baseline subtype.
        self.type_name = type_name

    def validate(self):
        if self.check_details:
            for v1 in self.check_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.auth_flag is not None:
            result['AuthFlag'] = self.auth_flag

        result['CheckDetails'] = []
        if self.check_details is not None:
            for k1 in self.check_details:
                result['CheckDetails'].append(k1.to_map() if k1 else None)

        if self.supported_os is not None:
            result['SupportedOs'] = self.supported_os

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('AuthFlag') is not None:
            self.auth_flag = m.get('AuthFlag')

        self.check_details = []
        if m.get('CheckDetails') is not None:
            for k1 in m.get('CheckDetails'):
                temp_model = main_models.DescribeRiskTypeResponseBodyRiskTypesSubTypesCheckDetails()
                self.check_details.append(temp_model.from_map(k1))

        if m.get('SupportedOs') is not None:
            self.supported_os = m.get('SupportedOs')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

class DescribeRiskTypeResponseBodyRiskTypesSubTypesCheckDetails(DaraModel):
    def __init__(
        self,
        check_desc: str = None,
        check_id: int = None,
        check_item: str = None,
        rules: List[main_models.DescribeRiskTypeResponseBodyRiskTypesSubTypesCheckDetailsRules] = None,
    ):
        # The description of the baseline.
        self.check_desc = check_desc
        # The ID of the baseline.
        self.check_id = check_id
        # The baseline.
        self.check_item = check_item
        # An array that consists of the rule details about the baseline.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_desc is not None:
            result['CheckDesc'] = self.check_desc

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_item is not None:
            result['CheckItem'] = self.check_item

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckDesc') is not None:
            self.check_desc = m.get('CheckDesc')

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckItem') is not None:
            self.check_item = m.get('CheckItem')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeRiskTypeResponseBodyRiskTypesSubTypesCheckDetailsRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeRiskTypeResponseBodyRiskTypesSubTypesCheckDetailsRules(DaraModel):
    def __init__(
        self,
        optional: int = None,
        param_list: List[main_models.DescribeRiskTypeResponseBodyRiskTypesSubTypesCheckDetailsRulesParamList] = None,
        rule_desc: str = None,
        rule_id: str = None,
    ):
        # Indicates whether the baseline can be edited. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.optional = optional
        # An array that consists of the parameters in the rule for the baseline.
        self.param_list = param_list
        # The description of the rule for the baseline.
        self.rule_desc = rule_desc
        # The ID of the rule for the baseline.
        self.rule_id = rule_id

    def validate(self):
        if self.param_list:
            for v1 in self.param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.optional is not None:
            result['Optional'] = self.optional

        result['ParamList'] = []
        if self.param_list is not None:
            for k1 in self.param_list:
                result['ParamList'].append(k1.to_map() if k1 else None)

        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Optional') is not None:
            self.optional = m.get('Optional')

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.DescribeRiskTypeResponseBodyRiskTypesSubTypesCheckDetailsRulesParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

class DescribeRiskTypeResponseBodyRiskTypesSubTypesCheckDetailsRulesParamList(DaraModel):
    def __init__(
        self,
        enum_value: str = None,
        max_value: int = None,
        min_value: int = None,
        param_default_value: str = None,
        param_desc: str = None,
        param_name: str = None,
        param_type: int = None,
    ):
        # If the value of paramType is 1, this parameter is empty. If the value of paramType is 2, this parameter provides the options that can be selected for paramType.
        self.enum_value = enum_value
        # The maximum value of the parameter.
        self.max_value = max_value
        # The minimum value of the parameter.
        self.min_value = min_value
        # The default value of the parameter.
        self.param_default_value = param_default_value
        # The description of the parameter.
        self.param_desc = param_desc
        # The name of the parameter.
        self.param_name = param_name
        # The configuration type of the parameter. Valid values:
        # 
        # *   **1**: input
        # *   **2**: selection
        self.param_type = param_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value

        if self.max_value is not None:
            result['MaxValue'] = self.max_value

        if self.min_value is not None:
            result['MinValue'] = self.min_value

        if self.param_default_value is not None:
            result['ParamDefaultValue'] = self.param_default_value

        if self.param_desc is not None:
            result['ParamDesc'] = self.param_desc

        if self.param_name is not None:
            result['ParamName'] = self.param_name

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')

        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')

        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')

        if m.get('ParamDefaultValue') is not None:
            self.param_default_value = m.get('ParamDefaultValue')

        if m.get('ParamDesc') is not None:
            self.param_desc = m.get('ParamDesc')

        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        return self

