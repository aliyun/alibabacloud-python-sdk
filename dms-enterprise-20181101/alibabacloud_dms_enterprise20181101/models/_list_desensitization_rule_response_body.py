# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListDesensitizationRuleResponseBody(DaraModel):
    def __init__(
        self,
        desensitization_rule_list: List[main_models.ListDesensitizationRuleResponseBodyDesensitizationRuleList] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The list of masking rules.
        self.desensitization_rule_list = desensitization_rule_list
        # The error code returned if the request failed.
        # 
        # This parameter is required.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success
        # The total number of entries returned. By default, this parameter is not returned.
        self.total_count = total_count

    def validate(self):
        if self.desensitization_rule_list:
            for v1 in self.desensitization_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DesensitizationRuleList'] = []
        if self.desensitization_rule_list is not None:
            for k1 in self.desensitization_rule_list:
                result['DesensitizationRuleList'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desensitization_rule_list = []
        if m.get('DesensitizationRuleList') is not None:
            for k1 in m.get('DesensitizationRuleList'):
                temp_model = main_models.ListDesensitizationRuleResponseBodyDesensitizationRuleList()
                self.desensitization_rule_list.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDesensitizationRuleResponseBodyDesensitizationRuleList(DaraModel):
    def __init__(
        self,
        func_params: str = None,
        func_sample: str = None,
        function_type: str = None,
        last_modifier_id: str = None,
        last_modifier_name: str = None,
        reference_count: int = None,
        rule_desc: str = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_type: str = None,
    ):
        # The parameter.
        self.func_params = func_params
        # The example.
        self.func_sample = func_sample
        # The algorithm type.
        self.function_type = function_type
        # The ID of the user who last modified the masking rule.
        self.last_modifier_id = last_modifier_id
        # The name of the user who last modified the masking rule.
        self.last_modifier_name = last_modifier_name
        # The number of times that the masking was used.
        self.reference_count = reference_count
        # The description of the rule.
        self.rule_desc = rule_desc
        # The ID of the masking rule.
        self.rule_id = rule_id
        # The name of the masking rule.
        self.rule_name = rule_name
        # The algorithm used for masking.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.func_params is not None:
            result['FuncParams'] = self.func_params

        if self.func_sample is not None:
            result['FuncSample'] = self.func_sample

        if self.function_type is not None:
            result['FunctionType'] = self.function_type

        if self.last_modifier_id is not None:
            result['LastModifierId'] = self.last_modifier_id

        if self.last_modifier_name is not None:
            result['LastModifierName'] = self.last_modifier_name

        if self.reference_count is not None:
            result['ReferenceCount'] = self.reference_count

        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FuncParams') is not None:
            self.func_params = m.get('FuncParams')

        if m.get('FuncSample') is not None:
            self.func_sample = m.get('FuncSample')

        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')

        if m.get('LastModifierId') is not None:
            self.last_modifier_id = m.get('LastModifierId')

        if m.get('LastModifierName') is not None:
            self.last_modifier_name = m.get('LastModifierName')

        if m.get('ReferenceCount') is not None:
            self.reference_count = m.get('ReferenceCount')

        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

