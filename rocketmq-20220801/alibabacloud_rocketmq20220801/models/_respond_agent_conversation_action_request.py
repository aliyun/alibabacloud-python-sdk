# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class RespondAgentConversationActionRequest(DaraModel):
    def __init__(
        self,
        answers: Dict[str, str] = None,
        decision: str = None,
        note: str = None,
    ):
        self.answers = answers
        self.decision = decision
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answers is not None:
            result['answers'] = self.answers

        if self.decision is not None:
            result['decision'] = self.decision

        if self.note is not None:
            result['note'] = self.note

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answers') is not None:
            self.answers = m.get('answers')

        if m.get('decision') is not None:
            self.decision = m.get('decision')

        if m.get('note') is not None:
            self.note = m.get('note')

        return self

