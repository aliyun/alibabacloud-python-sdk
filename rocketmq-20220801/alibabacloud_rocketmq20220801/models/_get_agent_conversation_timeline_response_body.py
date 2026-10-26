# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetAgentConversationTimelineResponseBody(DaraModel):
    def __init__(
        self,
        items: Any = None,
        replay_cursor: int = None,
        response_feedback: Any = None,
        runs: Any = None,
        source: str = None,
    ):
        self.items = items
        self.replay_cursor = replay_cursor
        self.response_feedback = response_feedback
        self.runs = runs
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['items'] = self.items

        if self.replay_cursor is not None:
            result['replayCursor'] = self.replay_cursor

        if self.response_feedback is not None:
            result['responseFeedback'] = self.response_feedback

        if self.runs is not None:
            result['runs'] = self.runs

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('items') is not None:
            self.items = m.get('items')

        if m.get('replayCursor') is not None:
            self.replay_cursor = m.get('replayCursor')

        if m.get('responseFeedback') is not None:
            self.response_feedback = m.get('responseFeedback')

        if m.get('runs') is not None:
            self.runs = m.get('runs')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

