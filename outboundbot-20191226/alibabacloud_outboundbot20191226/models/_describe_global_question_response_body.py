# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class DescribeGlobalQuestionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        global_question: main_models.DescribeGlobalQuestionResponseBodyGlobalQuestion = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.global_question = global_question
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.global_question:
            self.global_question.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.global_question is not None:
            result['GlobalQuestion'] = self.global_question.to_map()

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

        if m.get('GlobalQuestion') is not None:
            temp_model = main_models.DescribeGlobalQuestionResponseBodyGlobalQuestion()
            self.global_question = temp_model.from_map(m.get('GlobalQuestion'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeGlobalQuestionResponseBodyGlobalQuestion(DaraModel):
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

