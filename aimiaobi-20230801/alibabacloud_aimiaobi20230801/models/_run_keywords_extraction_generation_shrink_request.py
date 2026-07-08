# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunKeywordsExtractionGenerationShrinkRequest(DaraModel):
    def __init__(
        self,
        prompt: str = None,
        reference_data_shrink: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # Custom prompt.
        self.prompt = prompt
        # Data required for generation.
        # 
        # This parameter is required.
        self.reference_data_shrink = reference_data_shrink
        # The unique identifier for the associated creation article.
        # 
        # > TaskId is not required by default; the system automatically generates it. If subsequent tasks use the same TaskId, they belong to the same conversation group.
        self.task_id = task_id
        # The unique identifier for the Alibaba Cloud Model Studio workspace. Obtain the [Workspace ID](https://help.aliyun.com/document_detail/2782167.html).
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
        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.reference_data_shrink is not None:
            result['ReferenceData'] = self.reference_data_shrink

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('ReferenceData') is not None:
            self.reference_data_shrink = m.get('ReferenceData')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

