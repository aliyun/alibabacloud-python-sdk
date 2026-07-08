# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFreshViewPointsRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        max_results: int = None,
        next_token: str = None,
        topic: str = None,
        topic_source: str = None,
    ):
        # UUID of the workspace: AgentKey
        # 
        # This parameter is required.
        self.agent_key = agent_key
        # Maximum number of returned results
        self.max_results = max_results
        # Token for the next page
        self.next_token = next_token
        # Trending list topic
        # 
        # This parameter is required.
        self.topic = topic
        # Trending list source
        # 
        # This parameter is required.
        self.topic_source = topic_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')

        return self

