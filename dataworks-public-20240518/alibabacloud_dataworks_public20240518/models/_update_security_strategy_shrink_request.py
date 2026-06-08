# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSecurityStrategyShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        content_shrink: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
        workspaces_shrink: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.content_shrink = content_shrink
        self.description = description
        # This parameter is required.
        self.id = id
        self.name = name
        self.workspaces_shrink = workspaces_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.workspaces_shrink is not None:
            result['Workspaces'] = self.workspaces_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Workspaces') is not None:
            self.workspaces_shrink = m.get('Workspaces')

        return self

