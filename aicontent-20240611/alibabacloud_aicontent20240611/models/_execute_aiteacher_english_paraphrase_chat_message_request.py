# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteAITeacherEnglishParaphraseChatMessageRequest(DaraModel):
    def __init__(
        self,
        chat_id: str = None,
        content: str = None,
        grade: int = None,
        question_id: str = None,
        question_info: str = None,
        response_mode: str = None,
        user_answer: str = None,
        user_id: str = None,
    ):
        self.chat_id = chat_id
        # This parameter is required.
        self.content = content
        self.grade = grade
        self.question_id = question_id
        # This parameter is required.
        self.question_info = question_info
        # This parameter is required.
        self.response_mode = response_mode
        # This parameter is required.
        self.user_answer = user_answer
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_id is not None:
            result['chatId'] = self.chat_id

        if self.content is not None:
            result['content'] = self.content

        if self.grade is not None:
            result['grade'] = self.grade

        if self.question_id is not None:
            result['questionId'] = self.question_id

        if self.question_info is not None:
            result['questionInfo'] = self.question_info

        if self.response_mode is not None:
            result['responseMode'] = self.response_mode

        if self.user_answer is not None:
            result['userAnswer'] = self.user_answer

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('grade') is not None:
            self.grade = m.get('grade')

        if m.get('questionId') is not None:
            self.question_id = m.get('questionId')

        if m.get('questionInfo') is not None:
            self.question_info = m.get('questionInfo')

        if m.get('responseMode') is not None:
            self.response_mode = m.get('responseMode')

        if m.get('userAnswer') is not None:
            self.user_answer = m.get('userAnswer')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

