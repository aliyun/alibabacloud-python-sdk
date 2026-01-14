# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class GetAICoachAssessmentPointResponseBody(DaraModel):
    def __init__(
        self,
        answer_list: List[main_models.GetAICoachAssessmentPointResponseBodyAnswerList] = None,
        citations: int = None,
        document_id: str = None,
        document_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        kb_id: str = None,
        kb_type: str = None,
        knowledge_list: List[str] = None,
        name: str = None,
        point_id: str = None,
        question_description: str = None,
        question_sample: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.answer_list = answer_list
        self.citations = citations
        self.document_id = document_id
        self.document_name = document_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.kb_id = kb_id
        self.kb_type = kb_type
        self.knowledge_list = knowledge_list
        self.name = name
        self.point_id = point_id
        self.question_description = question_description
        self.question_sample = question_sample
        # Id of the request
        self.request_id = request_id
        self.status = status

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

        if self.citations is not None:
            result['citations'] = self.citations

        if self.document_id is not None:
            result['documentId'] = self.document_id

        if self.document_name is not None:
            result['documentName'] = self.document_name

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.kb_id is not None:
            result['kbId'] = self.kb_id

        if self.kb_type is not None:
            result['kbType'] = self.kb_type

        if self.knowledge_list is not None:
            result['knowledgeList'] = self.knowledge_list

        if self.name is not None:
            result['name'] = self.name

        if self.point_id is not None:
            result['pointId'] = self.point_id

        if self.question_description is not None:
            result['questionDescription'] = self.question_description

        if self.question_sample is not None:
            result['questionSample'] = self.question_sample

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_list = []
        if m.get('answerList') is not None:
            for k1 in m.get('answerList'):
                temp_model = main_models.GetAICoachAssessmentPointResponseBodyAnswerList()
                self.answer_list.append(temp_model.from_map(k1))

        if m.get('citations') is not None:
            self.citations = m.get('citations')

        if m.get('documentId') is not None:
            self.document_id = m.get('documentId')

        if m.get('documentName') is not None:
            self.document_name = m.get('documentName')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('kbId') is not None:
            self.kb_id = m.get('kbId')

        if m.get('kbType') is not None:
            self.kb_type = m.get('kbType')

        if m.get('knowledgeList') is not None:
            self.knowledge_list = m.get('knowledgeList')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pointId') is not None:
            self.point_id = m.get('pointId')

        if m.get('questionDescription') is not None:
            self.question_description = m.get('questionDescription')

        if m.get('questionSample') is not None:
            self.question_sample = m.get('questionSample')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetAICoachAssessmentPointResponseBodyAnswerList(DaraModel):
    def __init__(
        self,
        answer_values: List[main_models.GetAICoachAssessmentPointResponseBodyAnswerListAnswerValues] = None,
        enabled_keyword: bool = None,
        name_list: List[str] = None,
        operators: str = None,
        parameters: List[main_models.GetAICoachAssessmentPointResponseBodyAnswerListParameters] = None,
        type: str = None,
        weight: int = None,
    ):
        self.answer_values = answer_values
        self.enabled_keyword = enabled_keyword
        self.name_list = name_list
        self.operators = operators
        self.parameters = parameters
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
                temp_model = main_models.GetAICoachAssessmentPointResponseBodyAnswerListAnswerValues()
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
                temp_model = main_models.GetAICoachAssessmentPointResponseBodyAnswerListParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class GetAICoachAssessmentPointResponseBodyAnswerListParameters(DaraModel):
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

class GetAICoachAssessmentPointResponseBodyAnswerListAnswerValues(DaraModel):
    def __init__(
        self,
        answer_name: str = None,
        answer_weight: int = None,
        keyword_values: List[main_models.GetAICoachAssessmentPointResponseBodyAnswerListAnswerValuesKeywordValues] = None,
        keyword_weight: int = None,
        scoring_rules: List[main_models.GetAICoachAssessmentPointResponseBodyAnswerListAnswerValuesScoringRules] = None,
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
                temp_model = main_models.GetAICoachAssessmentPointResponseBodyAnswerListAnswerValuesKeywordValues()
                self.keyword_values.append(temp_model.from_map(k1))

        if m.get('keywordWeight') is not None:
            self.keyword_weight = m.get('keywordWeight')

        self.scoring_rules = []
        if m.get('scoringRules') is not None:
            for k1 in m.get('scoringRules'):
                temp_model = main_models.GetAICoachAssessmentPointResponseBodyAnswerListAnswerValuesScoringRules()
                self.scoring_rules.append(temp_model.from_map(k1))

        return self

class GetAICoachAssessmentPointResponseBodyAnswerListAnswerValuesScoringRules(DaraModel):
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

class GetAICoachAssessmentPointResponseBodyAnswerListAnswerValuesKeywordValues(DaraModel):
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

