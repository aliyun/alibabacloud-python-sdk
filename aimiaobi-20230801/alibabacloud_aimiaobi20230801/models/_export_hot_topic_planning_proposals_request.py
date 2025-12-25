# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ExportHotTopicPlanningProposalsRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        custom_view_point_ids: List[str] = None,
        export_type: str = None,
        titles: List[str] = None,
        topic: str = None,
        topic_source: str = None,
        view_point_type: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.custom_view_point_ids = custom_view_point_ids
        self.export_type = export_type
        self.titles = titles
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.topic_source = topic_source
        self.view_point_type = view_point_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.custom_view_point_ids is not None:
            result['CustomViewPointIds'] = self.custom_view_point_ids

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.titles is not None:
            result['Titles'] = self.titles

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source

        if self.view_point_type is not None:
            result['ViewPointType'] = self.view_point_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('CustomViewPointIds') is not None:
            self.custom_view_point_ids = m.get('CustomViewPointIds')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('Titles') is not None:
            self.titles = m.get('Titles')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')

        if m.get('ViewPointType') is not None:
            self.view_point_type = m.get('ViewPointType')

        return self

