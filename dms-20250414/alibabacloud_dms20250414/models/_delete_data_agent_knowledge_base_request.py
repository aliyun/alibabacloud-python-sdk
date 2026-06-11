# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDataAgentKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        dmsunit: str = None,
        kb_uuid: str = None,
        workspace_id: str = None,
    ):
        # The current DMS unit.
        self.dmsunit = dmsunit
        # The ID of the knowledge base.
        # 
        # This parameter is required.
        self.kb_uuid = kb_uuid
        # The ID of the workspace.
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
        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.kb_uuid is not None:
            result['KbUuid'] = self.kb_uuid

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('KbUuid') is not None:
            self.kb_uuid = m.get('KbUuid')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

