# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_farui20240628 import models as main_models
from darabonba.model import DaraModel

class RunContractRuleGenerationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        output: main_models.RunContractRuleGenerationResponseBodyOutput = None,
        request_id: str = None,
        success: bool = None,
        usage: main_models.RunContractRuleGenerationResponseBodyUsage = None,
        http_status_code: int = None,
    ):
        self.code = code
        self.message = message
        self.output = output
        self.request_id = request_id
        self.success = success
        self.usage = usage
        self.http_status_code = http_status_code

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Output') is not None:
            temp_model = main_models.RunContractRuleGenerationResponseBodyOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Usage') is not None:
            temp_model = main_models.RunContractRuleGenerationResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        return self

class RunContractRuleGenerationResponseBodyUsage(DaraModel):
    def __init__(
        self,
        input: int = None,
        unit: str = None,
    ):
        self.input = input
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['input'] = self.input

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input') is not None:
            self.input = m.get('input')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

class RunContractRuleGenerationResponseBodyOutput(DaraModel):
    def __init__(
        self,
        rule_task_id: str = None,
        rules: List[main_models.RunContractRuleGenerationResponseBodyOutputRules] = None,
    ):
        self.rule_task_id = rule_task_id
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
        if self.rule_task_id is not None:
            result['ruleTaskId'] = self.rule_task_id

        result['rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleTaskId') is not None:
            self.rule_task_id = m.get('ruleTaskId')

        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.RunContractRuleGenerationResponseBodyOutputRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class RunContractRuleGenerationResponseBodyOutputRules(DaraModel):
    def __init__(
        self,
        risk_level: str = None,
        rule_sequence: str = None,
        rule_tag: str = None,
        rule_title: str = None,
    ):
        self.risk_level = risk_level
        self.rule_sequence = rule_sequence
        self.rule_tag = rule_tag
        self.rule_title = rule_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level

        if self.rule_sequence is not None:
            result['ruleSequence'] = self.rule_sequence

        if self.rule_tag is not None:
            result['ruleTag'] = self.rule_tag

        if self.rule_title is not None:
            result['ruleTitle'] = self.rule_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')

        if m.get('ruleSequence') is not None:
            self.rule_sequence = m.get('ruleSequence')

        if m.get('ruleTag') is not None:
            self.rule_tag = m.get('ruleTag')

        if m.get('ruleTitle') is not None:
            self.rule_title = m.get('ruleTitle')

        return self

