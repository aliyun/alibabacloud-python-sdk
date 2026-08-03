# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class SubmitAICoachDebugRequest(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        data_type: int = None,
        deduction_rule: main_models.SubmitAICoachDebugRequestDeductionRule = None,
        dialogue_list: List[main_models.SubmitAICoachDebugRequestDialogueList] = None,
        expressiveness: main_models.SubmitAICoachDebugRequestExpressiveness = None,
        point: main_models.SubmitAICoachDebugRequestPoint = None,
    ):
        self.data_id = data_id
        self.data_type = data_type
        self.deduction_rule = deduction_rule
        self.dialogue_list = dialogue_list
        self.expressiveness = expressiveness
        self.point = point

    def validate(self):
        if self.deduction_rule:
            self.deduction_rule.validate()
        if self.dialogue_list:
            for v1 in self.dialogue_list:
                 if v1:
                    v1.validate()
        if self.expressiveness:
            self.expressiveness.validate()
        if self.point:
            self.point.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['dataId'] = self.data_id

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.deduction_rule is not None:
            result['deductionRule'] = self.deduction_rule.to_map()

        result['dialogueList'] = []
        if self.dialogue_list is not None:
            for k1 in self.dialogue_list:
                result['dialogueList'].append(k1.to_map() if k1 else None)

        if self.expressiveness is not None:
            result['expressiveness'] = self.expressiveness.to_map()

        if self.point is not None:
            result['point'] = self.point.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('deductionRule') is not None:
            temp_model = main_models.SubmitAICoachDebugRequestDeductionRule()
            self.deduction_rule = temp_model.from_map(m.get('deductionRule'))

        self.dialogue_list = []
        if m.get('dialogueList') is not None:
            for k1 in m.get('dialogueList'):
                temp_model = main_models.SubmitAICoachDebugRequestDialogueList()
                self.dialogue_list.append(temp_model.from_map(k1))

        if m.get('expressiveness') is not None:
            temp_model = main_models.SubmitAICoachDebugRequestExpressiveness()
            self.expressiveness = temp_model.from_map(m.get('expressiveness'))

        if m.get('point') is not None:
            temp_model = main_models.SubmitAICoachDebugRequestPoint()
            self.point = temp_model.from_map(m.get('point'))

        return self

class SubmitAICoachDebugRequestPoint(DaraModel):
    def __init__(
        self,
        answer_list: List[main_models.SubmitAICoachDebugRequestPointAnswerList] = None,
        knowledge_list: List[str] = None,
        name: str = None,
        question_sample: str = None,
        weight: int = None,
    ):
        self.answer_list = answer_list
        self.knowledge_list = knowledge_list
        self.name = name
        self.question_sample = question_sample
        self.weight = weight

    def validate(self):
        if self.answer_list:
            for v1 in self.answer_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['answerList'] = []
        if self.answer_list is not None:
            for k1 in self.answer_list:
                result['answerList'].append(k1.to_map() if k1 else None)

        if self.knowledge_list is not None:
            result['knowledgeList'] = self.knowledge_list

        if self.name is not None:
            result['name'] = self.name

        if self.question_sample is not None:
            result['questionSample'] = self.question_sample

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_list = []
        if m.get('answerList') is not None:
            for k1 in m.get('answerList'):
                temp_model = main_models.SubmitAICoachDebugRequestPointAnswerList()
                self.answer_list.append(temp_model.from_map(k1))

        if m.get('knowledgeList') is not None:
            self.knowledge_list = m.get('knowledgeList')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('questionSample') is not None:
            self.question_sample = m.get('questionSample')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class SubmitAICoachDebugRequestPointAnswerList(DaraModel):
    def __init__(
        self,
        answer_values: List[main_models.SubmitAICoachDebugRequestPointAnswerListAnswerValues] = None,
        enabled_keyword: bool = None,
        name_list: List[str] = None,
        operators: str = None,
        parameters: List[main_models.SubmitAICoachDebugRequestPointAnswerListParameters] = None,
        score: int = None,
        type: str = None,
        weight: int = None,
    ):
        self.answer_values = answer_values
        self.enabled_keyword = enabled_keyword
        self.name_list = name_list
        self.operators = operators
        self.parameters = parameters
        self.score = score
        self.type = type
        self.weight = weight

    def validate(self):
        if self.answer_values:
            for v1 in self.answer_values:
                 if v1:
                    v1.validate()
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['answerValues'] = []
        if self.answer_values is not None:
            for k1 in self.answer_values:
                result['answerValues'].append(k1.to_map() if k1 else None)

        if self.enabled_keyword is not None:
            result['enabledKeyword'] = self.enabled_keyword

        if self.name_list is not None:
            result['nameList'] = self.name_list

        if self.operators is not None:
            result['operators'] = self.operators

        result['parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['parameters'].append(k1.to_map() if k1 else None)

        if self.score is not None:
            result['score'] = self.score

        if self.type is not None:
            result['type'] = self.type

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_values = []
        if m.get('answerValues') is not None:
            for k1 in m.get('answerValues'):
                temp_model = main_models.SubmitAICoachDebugRequestPointAnswerListAnswerValues()
                self.answer_values.append(temp_model.from_map(k1))

        if m.get('enabledKeyword') is not None:
            self.enabled_keyword = m.get('enabledKeyword')

        if m.get('nameList') is not None:
            self.name_list = m.get('nameList')

        if m.get('operators') is not None:
            self.operators = m.get('operators')

        self.parameters = []
        if m.get('parameters') is not None:
            for k1 in m.get('parameters'):
                temp_model = main_models.SubmitAICoachDebugRequestPointAnswerListParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class SubmitAICoachDebugRequestPointAnswerListParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class SubmitAICoachDebugRequestPointAnswerListAnswerValues(DaraModel):
    def __init__(
        self,
        answer_name: str = None,
        answer_weight: int = None,
        keyword_values: List[main_models.SubmitAICoachDebugRequestPointAnswerListAnswerValuesKeywordValues] = None,
        keyword_weight: int = None,
        scoring_rules: List[main_models.SubmitAICoachDebugRequestPointAnswerListAnswerValuesScoringRules] = None,
    ):
        self.answer_name = answer_name
        self.answer_weight = answer_weight
        self.keyword_values = keyword_values
        self.keyword_weight = keyword_weight
        self.scoring_rules = scoring_rules

    def validate(self):
        if self.keyword_values:
            for v1 in self.keyword_values:
                 if v1:
                    v1.validate()
        if self.scoring_rules:
            for v1 in self.scoring_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer_name is not None:
            result['answerName'] = self.answer_name

        if self.answer_weight is not None:
            result['answerWeight'] = self.answer_weight

        result['keywordValues'] = []
        if self.keyword_values is not None:
            for k1 in self.keyword_values:
                result['keywordValues'].append(k1.to_map() if k1 else None)

        if self.keyword_weight is not None:
            result['keywordWeight'] = self.keyword_weight

        result['scoringRules'] = []
        if self.scoring_rules is not None:
            for k1 in self.scoring_rules:
                result['scoringRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answerName') is not None:
            self.answer_name = m.get('answerName')

        if m.get('answerWeight') is not None:
            self.answer_weight = m.get('answerWeight')

        self.keyword_values = []
        if m.get('keywordValues') is not None:
            for k1 in m.get('keywordValues'):
                temp_model = main_models.SubmitAICoachDebugRequestPointAnswerListAnswerValuesKeywordValues()
                self.keyword_values.append(temp_model.from_map(k1))

        if m.get('keywordWeight') is not None:
            self.keyword_weight = m.get('keywordWeight')

        self.scoring_rules = []
        if m.get('scoringRules') is not None:
            for k1 in m.get('scoringRules'):
                temp_model = main_models.SubmitAICoachDebugRequestPointAnswerListAnswerValuesScoringRules()
                self.scoring_rules.append(temp_model.from_map(k1))

        return self

class SubmitAICoachDebugRequestPointAnswerListAnswerValuesScoringRules(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class SubmitAICoachDebugRequestPointAnswerListAnswerValuesKeywordValues(DaraModel):
    def __init__(
        self,
        name: str = None,
        weight: int = None,
    ):
        self.name = name
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class SubmitAICoachDebugRequestExpressiveness(DaraModel):
    def __init__(
        self,
        desc: str = None,
        expressiveness_id: str = None,
        name: str = None,
        rule: str = None,
    ):
        self.desc = desc
        self.expressiveness_id = expressiveness_id
        self.name = name
        self.rule = rule

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.expressiveness_id is not None:
            result['expressivenessId'] = self.expressiveness_id

        if self.name is not None:
            result['name'] = self.name

        if self.rule is not None:
            result['rule'] = self.rule

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('expressivenessId') is not None:
            self.expressiveness_id = m.get('expressivenessId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('rule') is not None:
            self.rule = m.get('rule')

        return self

class SubmitAICoachDebugRequestDialogueList(DaraModel):
    def __init__(
        self,
        message: str = None,
        role: str = None,
    ):
        self.message = message
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

class SubmitAICoachDebugRequestDeductionRule(DaraModel):
    def __init__(
        self,
        deduction_rule_id: str = None,
        description: str = None,
        punishment_types: List[str] = None,
        rule_value: str = None,
        weight: int = None,
    ):
        self.deduction_rule_id = deduction_rule_id
        self.description = description
        self.punishment_types = punishment_types
        self.rule_value = rule_value
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deduction_rule_id is not None:
            result['deductionRuleId'] = self.deduction_rule_id

        if self.description is not None:
            result['description'] = self.description

        if self.punishment_types is not None:
            result['punishmentTypes'] = self.punishment_types

        if self.rule_value is not None:
            result['ruleValue'] = self.rule_value

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deductionRuleId') is not None:
            self.deduction_rule_id = m.get('deductionRuleId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('punishmentTypes') is not None:
            self.punishment_types = m.get('punishmentTypes')

        if m.get('ruleValue') is not None:
            self.rule_value = m.get('ruleValue')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

