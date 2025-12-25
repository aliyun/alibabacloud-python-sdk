# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitCustomTopicSelectionPerspectiveAnalysisTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        documents_shrink: str = None,
        prompt: str = None,
        topic: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.documents_shrink = documents_shrink
        # This parameter is required.
        self.prompt = prompt
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.documents_shrink is not None:
            result['Documents'] = self.documents_shrink

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Documents') is not None:
            self.documents_shrink = m.get('Documents')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

