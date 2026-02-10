# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeStrategyDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        strategy: main_models.DescribeStrategyDetailResponseBodyStrategy = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The information about the baseline check policy.
        self.strategy = strategy

    def validate(self):
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Strategy') is not None:
            temp_model = main_models.DescribeStrategyDetailResponseBodyStrategy()
            self.strategy = temp_model.from_map(m.get('Strategy'))

        return self

class DescribeStrategyDetailResponseBodyStrategy(DaraModel):
    def __init__(
        self,
        custom_type: str = None,
        cycle_days: int = None,
        cycle_start_time: int = None,
        end_time: str = None,
        id: int = None,
        name: str = None,
        risk_sub_type_name: str = None,
        risk_type_white_list_query_result_list: List[main_models.DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultList] = None,
        start_time: str = None,
        target_type: str = None,
        type: int = None,
    ):
        # The type of the baseline check policy that you want to query. Valid values:
        # 
        # *   **common**: standard baseline check policy
        # *   **custom**: custom baseline check policy
        self.custom_type = custom_type
        # The check interval of the policy.
        self.cycle_days = cycle_days
        # The time period during which the check starts. Valid values:
        # 
        # *   **0**: 00:00 to 06:00
        # *   **6**: 06:00 to 12:00
        # *   **12**: 12:00 to 18:00
        # *   **18**: 18:00 to 24:00
        self.cycle_start_time = cycle_start_time
        # The end time of the check. Specify the time in the HH:mm:ss format.
        self.end_time = end_time
        # The ID of the baseline check policy.
        self.id = id
        # The name of the baseline check policy.
        self.name = name
        # The subtype of the baselines. 
        # 
        # > You can call the [DescribeRiskType](~~DescribeRiskType~~) operation to query the subtypes of baselines.
        self.risk_sub_type_name = risk_sub_type_name
        # The information about the whitelist of risk items.
        self.risk_type_white_list_query_result_list = risk_type_white_list_query_result_list
        # The start time of the check. Specify the time in the HH:mm:ss format.
        self.start_time = start_time
        # The method that is used to apply the baseline check policy. Valid values:
        # 
        # *   **groupId**: asset groups
        # *   **uuid**: assets
        self.target_type = target_type
        # The type of the baseline check policy. Valid values:
        # 
        # *   **1**: standard policies
        # *   **2**: custom policies
        self.type = type

    def validate(self):
        if self.risk_type_white_list_query_result_list:
            for v1 in self.risk_type_white_list_query_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_type is not None:
            result['CustomType'] = self.custom_type

        if self.cycle_days is not None:
            result['CycleDays'] = self.cycle_days

        if self.cycle_start_time is not None:
            result['CycleStartTime'] = self.cycle_start_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.risk_sub_type_name is not None:
            result['RiskSubTypeName'] = self.risk_sub_type_name

        result['RiskTypeWhiteListQueryResultList'] = []
        if self.risk_type_white_list_query_result_list is not None:
            for k1 in self.risk_type_white_list_query_result_list:
                result['RiskTypeWhiteListQueryResultList'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomType') is not None:
            self.custom_type = m.get('CustomType')

        if m.get('CycleDays') is not None:
            self.cycle_days = m.get('CycleDays')

        if m.get('CycleStartTime') is not None:
            self.cycle_start_time = m.get('CycleStartTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RiskSubTypeName') is not None:
            self.risk_sub_type_name = m.get('RiskSubTypeName')

        self.risk_type_white_list_query_result_list = []
        if m.get('RiskTypeWhiteListQueryResultList') is not None:
            for k1 in m.get('RiskTypeWhiteListQueryResultList'):
                temp_model = main_models.DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultList()
                self.risk_type_white_list_query_result_list.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultList(DaraModel):
    def __init__(
        self,
        alias: str = None,
        on: bool = None,
        sub_types: List[main_models.DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultListSubTypes] = None,
        type_name: str = None,
    ):
        # The alias of the check item.
        self.alias = alias
        # Indicates whether the check item is selected. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.on = on
        # The information about sub-check items.
        self.sub_types = sub_types
        # The name of the check item.
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

        if self.on is not None:
            result['On'] = self.on

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

        if m.get('On') is not None:
            self.on = m.get('On')

        self.sub_types = []
        if m.get('SubTypes') is not None:
            for k1 in m.get('SubTypes'):
                temp_model = main_models.DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultListSubTypes()
                self.sub_types.append(temp_model.from_map(k1))

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

class DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultListSubTypes(DaraModel):
    def __init__(
        self,
        alias: str = None,
        check_details: List[main_models.DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultListSubTypesCheckDetails] = None,
        on: bool = None,
        supported_os: str = None,
        type_name: str = None,
    ):
        # The alias of the check item.
        self.alias = alias
        # The details of custom check items.
        self.check_details = check_details
        # Indicates whether the sub-check item is selected. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.on = on
        # The operating system type of the server. Valid values:
        # *   **windows**
        # *   **linux**
        self.supported_os = supported_os
        # The type of the sub-check item.
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

        result['CheckDetails'] = []
        if self.check_details is not None:
            for k1 in self.check_details:
                result['CheckDetails'].append(k1.to_map() if k1 else None)

        if self.on is not None:
            result['On'] = self.on

        if self.supported_os is not None:
            result['SupportedOs'] = self.supported_os

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        self.check_details = []
        if m.get('CheckDetails') is not None:
            for k1 in m.get('CheckDetails'):
                temp_model = main_models.DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultListSubTypesCheckDetails()
                self.check_details.append(temp_model.from_map(k1))

        if m.get('On') is not None:
            self.on = m.get('On')

        if m.get('SupportedOs') is not None:
            self.supported_os = m.get('SupportedOs')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

class DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultListSubTypesCheckDetails(DaraModel):
    def __init__(
        self,
        check_desc: str = None,
        check_id: int = None,
        check_item: str = None,
        rules: List[main_models.DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultListSubTypesCheckDetailsRules] = None,
    ):
        # The description of the check item.
        self.check_desc = check_desc
        # The ID of the check item.
        self.check_id = check_id
        # The check item.
        self.check_item = check_item
        # The details of rules.
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
                temp_model = main_models.DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultListSubTypesCheckDetailsRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultListSubTypesCheckDetailsRules(DaraModel):
    def __init__(
        self,
        default_value: int = None,
        optional: int = None,
        param_list: List[main_models.DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultListSubTypesCheckDetailsRulesParamList] = None,
        rule_desc: str = None,
        rule_id: str = None,
    ):
        # The default value of the rule.
        self.default_value = default_value
        # Indicates whether the rule can be selected. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.optional = optional
        # The rule parameters.
        self.param_list = param_list
        # The description of the rule.
        self.rule_desc = rule_desc
        # The rule ID.
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Optional') is not None:
            self.optional = m.get('Optional')

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultListSubTypesCheckDetailsRulesParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

class DescribeStrategyDetailResponseBodyStrategyRiskTypeWhiteListQueryResultListSubTypesCheckDetailsRulesParamList(DaraModel):
    def __init__(
        self,
        enum_value: str = None,
        max_value: int = None,
        min_value: int = None,
        param_default_value: str = None,
        param_desc: str = None,
        param_name: str = None,
        param_type: int = None,
        value: str = None,
    ):
        # The options that can be selected for the rule parameter if the value of ParamType is set to 2.
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
        # The configured value of the rule parameter.
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

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

