# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCustomViewPointsShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        attitude: str = None,
        attitudes_shrink: str = None,
        custom_view_point_id: str = None,
        custom_view_point_ids_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        topic: str = None,
        topic_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.attitude = attitude
        self.attitudes_shrink = attitudes_shrink
        self.custom_view_point_id = custom_view_point_id
        self.custom_view_point_ids_shrink = custom_view_point_ids_shrink
        self.max_results = max_results
        self.next_token = next_token
        self.topic = topic
        self.topic_id = topic_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.attitude is not None:
            result['Attitude'] = self.attitude

        if self.attitudes_shrink is not None:
            result['Attitudes'] = self.attitudes_shrink

        if self.custom_view_point_id is not None:
            result['CustomViewPointId'] = self.custom_view_point_id

        if self.custom_view_point_ids_shrink is not None:
            result['CustomViewPointIds'] = self.custom_view_point_ids_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')

        if m.get('Attitudes') is not None:
            self.attitudes_shrink = m.get('Attitudes')

        if m.get('CustomViewPointId') is not None:
            self.custom_view_point_id = m.get('CustomViewPointId')

        if m.get('CustomViewPointIds') is not None:
            self.custom_view_point_ids_shrink = m.get('CustomViewPointIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        return self

