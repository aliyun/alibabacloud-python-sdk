# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWorkspaceCodeRequest(DaraModel):
    def __init__(
        self,
        iac: str = None,
        path: str = None,
        workspace_id: str = None,
    ):
        # If the file is a JSON file and Iac is set to true, the returned content is converted from JSON format to YAML format.
        self.iac = iac
        # The code file path: /Workspace/code/test.py
        # Request path.
        # 
        # This parameter is required.
        self.path = path
        # The workspace ID.
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
        if self.iac is not None:
            result['Iac'] = self.iac

        if self.path is not None:
            result['Path'] = self.path

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iac') is not None:
            self.iac = m.get('Iac')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

