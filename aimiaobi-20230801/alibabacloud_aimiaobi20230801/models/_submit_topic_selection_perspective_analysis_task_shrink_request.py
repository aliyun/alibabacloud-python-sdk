# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitTopicSelectionPerspectiveAnalysisTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        documents_shrink: str = None,
        perspective_types_shrink: str = None,
        topic: str = None,
    ):
        # The unique identifier of the workspace: [AgentKey](https://help.aliyun.com/document_detail/2587494.html)
        # 
        # This parameter is required.
        self.agent_key = agent_key
        # The list of documents to be analyzed. (Provide at least one of documents or topic)
        self.documents_shrink = documents_shrink
        # The topic selection perspective tasks to be analyzed. By default, this parameter is empty, which means all tasks are analyzed. (TopicSummary: Topic event summary, HotViewPoints: Hot topic selection perspectives, TimedViewPoints: Timeliness topic selection perspectives, WebReviewPoints: Online review topic selection perspectives, FreshViewPoints: Novel topic selection perspectives)
        self.perspective_types_shrink = perspective_types_shrink
        # The name of the topic to be analyzed. (Provide at least one of documents or topic)
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

        if self.perspective_types_shrink is not None:
            result['PerspectiveTypes'] = self.perspective_types_shrink

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Documents') is not None:
            self.documents_shrink = m.get('Documents')

        if m.get('PerspectiveTypes') is not None:
            self.perspective_types_shrink = m.get('PerspectiveTypes')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

