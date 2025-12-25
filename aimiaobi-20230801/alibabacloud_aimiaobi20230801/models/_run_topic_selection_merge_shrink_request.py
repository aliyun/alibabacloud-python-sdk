# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunTopicSelectionMergeShrinkRequest(DaraModel):
    def __init__(
        self,
        prompt: str = None,
        topics_shrink: str = None,
        workspace_id: str = None,
    ):
        self.prompt = prompt
        # This parameter is required.
        self.topics_shrink = topics_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.topics_shrink is not None:
            result['Topics'] = self.topics_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Topics') is not None:
            self.topics_shrink = m.get('Topics')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

