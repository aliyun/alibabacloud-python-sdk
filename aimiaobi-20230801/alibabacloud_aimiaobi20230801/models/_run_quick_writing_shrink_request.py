# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunQuickWritingShrinkRequest(DaraModel):
    def __init__(
        self,
        articles_shrink: str = None,
        prompt: str = None,
        search_sources_shrink: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # Referenced articles
        self.articles_shrink = articles_shrink
        # Other writing parameters. Choose either prompt or writingParams.
        # 
        # This parameter is required.
        self.prompt = prompt
        # Use the specified search source list.
        self.search_sources_shrink = search_sources_shrink
        # Task ID. Reuse the same task ID for multi-turn conversations.
        self.task_id = task_id
        # [Workspace ID](https://help.aliyun.com/document_detail/2782167.html)
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.articles_shrink is not None:
            result['Articles'] = self.articles_shrink

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.search_sources_shrink is not None:
            result['SearchSources'] = self.search_sources_shrink

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Articles') is not None:
            self.articles_shrink = m.get('Articles')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('SearchSources') is not None:
            self.search_sources_shrink = m.get('SearchSources')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

