# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCheckFixDetailsResponseBody(DaraModel):
    def __init__(
        self,
        check_fix_details: List[main_models.DescribeCheckFixDetailsResponseBodyCheckFixDetails] = None,
        count: int = None,
        request_id: str = None,
    ):
        # An array that consists of the parameters.
        self.check_fix_details = check_fix_details
        # The number of risk items that can be fixed.
        self.count = count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.check_fix_details:
            for v1 in self.check_fix_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckFixDetails'] = []
        if self.check_fix_details is not None:
            for k1 in self.check_fix_details:
                result['CheckFixDetails'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_fix_details = []
        if m.get('CheckFixDetails') is not None:
            for k1 in m.get('CheckFixDetails'):
                temp_model = main_models.DescribeCheckFixDetailsResponseBodyCheckFixDetails()
                self.check_fix_details.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCheckFixDetailsResponseBodyCheckFixDetails(DaraModel):
    def __init__(
        self,
        check_desc: str = None,
        check_id: int = None,
        check_item: str = None,
        rules: List[main_models.DescribeCheckFixDetailsResponseBodyCheckFixDetailsRules] = None,
    ):
        # The detailed description of the risk item.
        self.check_desc = check_desc
        # The ID of the risk item.
        self.check_id = check_id
        # The description of the risk item.
        self.check_item = check_item
        # An array consisting of the rules that are supported by the risk item.
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
                temp_model = main_models.DescribeCheckFixDetailsResponseBodyCheckFixDetailsRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeCheckFixDetailsResponseBodyCheckFixDetailsRules(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        default_value: int = None,
        optional: int = None,
        param_list: List[main_models.DescribeCheckFixDetailsResponseBodyCheckFixDetailsRulesParamList] = None,
        rule_desc: str = None,
        rule_id: str = None,
        value: int = None,
        var_name: str = None,
    ):
        # The ID of the risk item.
        self.check_id = check_id
        # The default value of the rule.
        self.default_value = default_value
        # Indicates whether the rule is optional. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.optional = optional
        # An array that consists of the rule parameters.
        self.param_list = param_list
        # The description of the rule.
        self.rule_desc = rule_desc
        # The ID of the rule.
        self.rule_id = rule_id
        # The specified value of the rule parameter.
        self.value = value
        # The name of the variable.
        self.var_name = var_name

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
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

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

        if self.value is not None:
            result['Value'] = self.value

        if self.var_name is not None:
            result['VarName'] = self.var_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Optional') is not None:
            self.optional = m.get('Optional')

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.DescribeCheckFixDetailsResponseBodyCheckFixDetailsRulesParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('VarName') is not None:
            self.var_name = m.get('VarName')

        return self

class DescribeCheckFixDetailsResponseBodyCheckFixDetailsRulesParamList(DaraModel):
    def __init__(
        self,
        enum_value: str = None,
        max_value: int = None,
        min_value: int = None,
        param_default_value: str = None,
        param_desc: str = None,
        param_name: str = None,
        param_type: int = None,
        rule_id: str = None,
        value: str = None,
    ):
        # The options that can be selected for the rule parameter if the value of the ParamType parameter is 2.
        self.enum_value = enum_value
        # The maximum value of the rule parameter.
        self.max_value = max_value
        # The minimum value of the rule parameter.
        self.min_value = min_value
        # The default value of the rule parameter.
        self.param_default_value = param_default_value
        # The description of the rule parameter.
        self.param_desc = param_desc
        # The name of the rule parameter.
        self.param_name = param_name
        # The type of the rule parameter. Valid values:
        # 
        # *   **1**: input
        # *   **2**: selection
        self.param_type = param_type
        # The ID of the rule.
        self.rule_id = rule_id
        # The specified value of the rule parameter.
        self.value = value

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

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.value is not None:
            result['Value'] = self.value

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

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

