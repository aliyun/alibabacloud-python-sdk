# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunTextPolishingRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        origin_content: str = None,
        prompt: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # Text content.
        # 
        # This parameter is required.
        self.content = content
        # Original article.
        self.origin_content = origin_content
        # Custom polishing requirements.
        self.prompt = prompt
        # The task ID. The same task ID shares a session. The task timeout is 12 hours.
        self.task_id = task_id
        # The unique identifier of the Alibaba Cloud Model Studio workspace. Obtain the [Workspace ID](https://help.aliyun.com/document_detail/2782167.html).
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
        if self.content is not None:
            result['Content'] = self.content

        if self.origin_content is not None:
            result['OriginContent'] = self.origin_content

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('OriginContent') is not None:
            self.origin_content = m.get('OriginContent')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

