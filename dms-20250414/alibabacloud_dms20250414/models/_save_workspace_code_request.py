# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveWorkspaceCodeRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        force: bool = None,
        iac: bool = None,
        mtime: str = None,
        path: str = None,
        repo: str = None,
        workspace_id: str = None,
    ):
        # The code content.
        # 
        # This parameter is required.
        self.content = content
        # Specifies whether to forcibly overwrite the file. If set to true, the file is overwritten regardless of whether it has been modified by others.
        self.force = force
        # Specifies whether the file is an infrastructure as code template file. Set this parameter to true for YAML configuration files that are edited in the visual editor.
        self.iac = iac
        # The file modification time. The GetWorkspaceCode operation returns this mtime value. When you call SaveWorkspaceCode, include this mtime value to check whether the file has been changed on the server. If the mtime values do not match, the save operation fails, which indicates that the server-side version has been modified.
        self.mtime = mtime
        # The file path to save.
        # 
        # This parameter is required.
        self.path = path
        # The repository information. Specify this parameter when creating a git repository directory during the save operation.
        self.repo = repo
        # The workspace ID (numeric ID).
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

        if self.force is not None:
            result['Force'] = self.force

        if self.iac is not None:
            result['Iac'] = self.iac

        if self.mtime is not None:
            result['Mtime'] = self.mtime

        if self.path is not None:
            result['Path'] = self.path

        if self.repo is not None:
            result['Repo'] = self.repo

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('Iac') is not None:
            self.iac = m.get('Iac')

        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Repo') is not None:
            self.repo = m.get('Repo')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

