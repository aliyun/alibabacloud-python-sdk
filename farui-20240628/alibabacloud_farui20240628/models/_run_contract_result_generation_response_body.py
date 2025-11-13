# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_farui20240628 import models as main_models
from darabonba.model import DaraModel

class RunContractResultGenerationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        output: main_models.RunContractResultGenerationResponseBodyOutput = None,
        request_id: str = None,
        success: bool = None,
        usage: main_models.RunContractResultGenerationResponseBodyUsage = None,
        http_status_code: str = None,
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
            temp_model = main_models.RunContractResultGenerationResponseBodyOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Usage') is not None:
            temp_model = main_models.RunContractResultGenerationResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        return self

class RunContractResultGenerationResponseBodyUsage(DaraModel):
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

class RunContractResultGenerationResponseBodyOutput(DaraModel):
    def __init__(
        self,
        result: main_models.RunContractResultGenerationResponseBodyOutputResult = None,
        result_task_id: str = None,
    ):
        self.result = result
        self.result_task_id = result_task_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.result_task_id is not None:
            result['resultTaskId'] = self.result_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = main_models.RunContractResultGenerationResponseBodyOutputResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('resultTaskId') is not None:
            self.result_task_id = m.get('resultTaskId')

        return self

class RunContractResultGenerationResponseBodyOutputResult(DaraModel):
    def __init__(
        self,
        examine_brief: str = None,
        examine_result: str = None,
        risk_level: str = None,
        rule_sequence: str = None,
        rule_tag: str = None,
        rule_title: str = None,
        sub_risks: List[main_models.RunContractResultGenerationResponseBodyOutputResultSubRisks] = None,
    ):
        self.examine_brief = examine_brief
        self.examine_result = examine_result
        self.risk_level = risk_level
        self.rule_sequence = rule_sequence
        self.rule_tag = rule_tag
        self.rule_title = rule_title
        self.sub_risks = sub_risks

    def validate(self):
        if self.sub_risks:
            for v1 in self.sub_risks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.examine_brief is not None:
            result['examineBrief'] = self.examine_brief

        if self.examine_result is not None:
            result['examineResult'] = self.examine_result

        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level

        if self.rule_sequence is not None:
            result['ruleSequence'] = self.rule_sequence

        if self.rule_tag is not None:
            result['ruleTag'] = self.rule_tag

        if self.rule_title is not None:
            result['ruleTitle'] = self.rule_title

        result['subRisks'] = []
        if self.sub_risks is not None:
            for k1 in self.sub_risks:
                result['subRisks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('examineBrief') is not None:
            self.examine_brief = m.get('examineBrief')

        if m.get('examineResult') is not None:
            self.examine_result = m.get('examineResult')

        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')

        if m.get('ruleSequence') is not None:
            self.rule_sequence = m.get('ruleSequence')

        if m.get('ruleTag') is not None:
            self.rule_tag = m.get('ruleTag')

        if m.get('ruleTitle') is not None:
            self.rule_title = m.get('ruleTitle')

        self.sub_risks = []
        if m.get('subRisks') is not None:
            for k1 in m.get('subRisks'):
                temp_model = main_models.RunContractResultGenerationResponseBodyOutputResultSubRisks()
                self.sub_risks.append(temp_model.from_map(k1))

        return self

class RunContractResultGenerationResponseBodyOutputResultSubRisks(DaraModel):
    def __init__(
        self,
        original_content: str = None,
        result_content: str = None,
        result_type: str = None,
        risk_brief: str = None,
        risk_clause: str = None,
        risk_explain: str = None,
        standard_original_content: str = None,
    ):
        self.original_content = original_content
        self.result_content = result_content
        self.result_type = result_type
        self.risk_brief = risk_brief
        self.risk_clause = risk_clause
        self.risk_explain = risk_explain
        self.standard_original_content = standard_original_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.original_content is not None:
            result['originalContent'] = self.original_content

        if self.result_content is not None:
            result['resultContent'] = self.result_content

        if self.result_type is not None:
            result['resultType'] = self.result_type

        if self.risk_brief is not None:
            result['riskBrief'] = self.risk_brief

        if self.risk_clause is not None:
            result['riskClause'] = self.risk_clause

        if self.risk_explain is not None:
            result['riskExplain'] = self.risk_explain

        if self.standard_original_content is not None:
            result['standardOriginalContent'] = self.standard_original_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalContent') is not None:
            self.original_content = m.get('originalContent')

        if m.get('resultContent') is not None:
            self.result_content = m.get('resultContent')

        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')

        if m.get('riskBrief') is not None:
            self.risk_brief = m.get('riskBrief')

        if m.get('riskClause') is not None:
            self.risk_clause = m.get('riskClause')

        if m.get('riskExplain') is not None:
            self.risk_explain = m.get('riskExplain')

        if m.get('standardOriginalContent') is not None:
            self.standard_original_content = m.get('standardOriginalContent')

        return self

