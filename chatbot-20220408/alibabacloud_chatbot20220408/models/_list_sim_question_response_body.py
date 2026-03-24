# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class ListSimQuestionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sim_questions: List[main_models.ListSimQuestionResponseBodySimQuestions] = None,
    ):
        self.request_id = request_id
        self.sim_questions = sim_questions

    def validate(self):
        if self.sim_questions:
            for v1 in self.sim_questions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k1 in self.sim_questions:
                result['SimQuestions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sim_questions = []
        if m.get('SimQuestions') is not None:
            for k1 in m.get('SimQuestions'):
                temp_model = main_models.ListSimQuestionResponseBodySimQuestions()
                self.sim_questions.append(temp_model.from_map(k1))

        return self

class ListSimQuestionResponseBodySimQuestions(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        sim_question_id: int = None,
        title: str = None,
    ):
        self.create_time = create_time
        self.modify_time = modify_time
        self.sim_question_id = sim_question_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

