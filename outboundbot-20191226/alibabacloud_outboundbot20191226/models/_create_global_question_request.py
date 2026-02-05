# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGlobalQuestionRequest(DaraModel):
    def __init__(
        self,
        answers: str = None,
        global_question_name: str = None,
        global_question_type: str = None,
        instance_id: str = None,
        questions: str = None,
        script_id: str = None,
    ):
        # This parameter is required.
        self.answers = answers
        # This parameter is required.
        self.global_question_name = global_question_name
        # This parameter is required.
        self.global_question_type = global_question_type
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.questions = questions
        # This parameter is required.
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

        if self.global_question_name is not None:
            result['GlobalQuestionName'] = self.global_question_name

        if self.global_question_type is not None:
            result['GlobalQuestionType'] = self.global_question_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.questions is not None:
            result['Questions'] = self.questions

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')

        if m.get('GlobalQuestionName') is not None:
            self.global_question_name = m.get('GlobalQuestionName')

        if m.get('GlobalQuestionType') is not None:
            self.global_question_type = m.get('GlobalQuestionType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Questions') is not None:
            self.questions = m.get('Questions')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        return self

