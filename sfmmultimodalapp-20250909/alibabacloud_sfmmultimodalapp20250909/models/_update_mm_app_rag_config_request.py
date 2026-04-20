# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMmAppRagConfigRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        prompt_strategy: str = None,
        retrieve_max_length: int = None,
        top_k: int = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.prompt_strategy = prompt_strategy
        # This parameter is required.
        self.retrieve_max_length = retrieve_max_length
        self.top_k = top_k
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.prompt_strategy is not None:
            result['PromptStrategy'] = self.prompt_strategy

        if self.retrieve_max_length is not None:
            result['RetrieveMaxLength'] = self.retrieve_max_length

        if self.top_k is not None:
            result['TopK'] = self.top_k

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('PromptStrategy') is not None:
            self.prompt_strategy = m.get('PromptStrategy')

        if m.get('RetrieveMaxLength') is not None:
            self.retrieve_max_length = m.get('RetrieveMaxLength')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

