# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataAgentKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        dmsunit: str = None,
        description: str = None,
        from_kb_uuid: str = None,
        name: str = None,
        workspace_id: str = None,
    ):
        self.dmsunit = dmsunit
        self.description = description
        self.from_kb_uuid = from_kb_uuid
        # This parameter is required.
        self.name = name
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

        if self.description is not None:
            result['Description'] = self.description

        if self.from_kb_uuid is not None:
            result['FromKbUuid'] = self.from_kb_uuid

        if self.name is not None:
            result['Name'] = self.name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FromKbUuid') is not None:
            self.from_kb_uuid = m.get('FromKbUuid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

