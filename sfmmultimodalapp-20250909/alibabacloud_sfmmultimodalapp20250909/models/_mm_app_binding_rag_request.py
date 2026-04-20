# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MmAppBindingRagRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        knowledge_base_code_list: List[str] = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.knowledge_base_code_list = knowledge_base_code_list
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

        if self.knowledge_base_code_list is not None:
            result['KnowledgeBaseCodeList'] = self.knowledge_base_code_list

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('KnowledgeBaseCodeList') is not None:
            self.knowledge_base_code_list = m.get('KnowledgeBaseCodeList')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

