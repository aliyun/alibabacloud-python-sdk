# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GuidingQuestion(DaraModel):
    def __init__(
        self,
        answer: str = None,
        question: str = None,
    ):
        # The answer.
        self.answer = answer
        # The question.
        self.question = question

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        if self.question is not None:
            result['Question'] = self.question

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        return self

