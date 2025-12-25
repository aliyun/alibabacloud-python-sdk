# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunTopicSelectionMergeRequest(DaraModel):
    def __init__(
        self,
        prompt: str = None,
        topics: List[main_models.TopicSelection] = None,
        workspace_id: str = None,
    ):
        self.prompt = prompt
        # This parameter is required.
        self.topics = topics
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.topics:
            for v1 in self.topics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prompt is not None:
            result['Prompt'] = self.prompt

        result['Topics'] = []
        if self.topics is not None:
            for k1 in self.topics:
                result['Topics'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        self.topics = []
        if m.get('Topics') is not None:
            for k1 in m.get('Topics'):
                temp_model = main_models.TopicSelection()
                self.topics.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

