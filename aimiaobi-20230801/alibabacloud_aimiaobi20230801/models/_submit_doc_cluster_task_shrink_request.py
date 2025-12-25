# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitDocClusterTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        documents_shrink: str = None,
        summary_length: int = None,
        title_length: int = None,
        topic_count: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.documents_shrink = documents_shrink
        self.summary_length = summary_length
        self.title_length = title_length
        self.topic_count = topic_count

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

        if self.summary_length is not None:
            result['SummaryLength'] = self.summary_length

        if self.title_length is not None:
            result['TitleLength'] = self.title_length

        if self.topic_count is not None:
            result['TopicCount'] = self.topic_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Documents') is not None:
            self.documents_shrink = m.get('Documents')

        if m.get('SummaryLength') is not None:
            self.summary_length = m.get('SummaryLength')

        if m.get('TitleLength') is not None:
            self.title_length = m.get('TitleLength')

        if m.get('TopicCount') is not None:
            self.topic_count = m.get('TopicCount')

        return self

