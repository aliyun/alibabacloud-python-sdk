# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListGlobalQuestionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        global_questions: main_models.ListGlobalQuestionsResponseBodyGlobalQuestions = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.global_questions = global_questions
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.global_questions:
            self.global_questions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.global_questions is not None:
            result['GlobalQuestions'] = self.global_questions.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('GlobalQuestions') is not None:
            temp_model = main_models.ListGlobalQuestionsResponseBodyGlobalQuestions()
            self.global_questions = temp_model.from_map(m.get('GlobalQuestions'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListGlobalQuestionsResponseBodyGlobalQuestions(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListGlobalQuestionsResponseBodyGlobalQuestionsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListGlobalQuestionsResponseBodyGlobalQuestionsList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListGlobalQuestionsResponseBodyGlobalQuestionsList(DaraModel):
    def __init__(
        self,
        answers: str = None,
        global_question_id: str = None,
        global_question_name: str = None,
        global_question_type: str = None,
        questions: str = None,
        script_id: str = None,
    ):
        self.answers = answers
        self.global_question_id = global_question_id
        self.global_question_name = global_question_name
        self.global_question_type = global_question_type
        self.questions = questions
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answers is not None:
            result['Answers'] = self.answers

        if self.global_question_id is not None:
            result['GlobalQuestionId'] = self.global_question_id

        if self.global_question_name is not None:
            result['GlobalQuestionName'] = self.global_question_name

        if self.global_question_type is not None:
            result['GlobalQuestionType'] = self.global_question_type

        if self.questions is not None:
            result['Questions'] = self.questions

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')

        if m.get('GlobalQuestionId') is not None:
            self.global_question_id = m.get('GlobalQuestionId')

        if m.get('GlobalQuestionName') is not None:
            self.global_question_name = m.get('GlobalQuestionName')

        if m.get('GlobalQuestionType') is not None:
            self.global_question_type = m.get('GlobalQuestionType')

        if m.get('Questions') is not None:
            self.questions = m.get('Questions')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        return self

