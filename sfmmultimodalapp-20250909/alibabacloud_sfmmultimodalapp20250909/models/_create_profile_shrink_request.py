# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProfileShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        attributes_shrink: str = None,
        description: str = None,
        name: str = None,
        user_defined_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.attributes_shrink = attributes_shrink
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.name = name
        self.user_defined_id = user_defined_id
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

        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.user_defined_id is not None:
            result['UserDefinedId'] = self.user_defined_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UserDefinedId') is not None:
            self.user_defined_id = m.get('UserDefinedId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

