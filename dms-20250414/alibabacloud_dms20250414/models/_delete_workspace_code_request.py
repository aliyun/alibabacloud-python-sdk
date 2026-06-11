# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWorkspaceCodeRequest(DaraModel):
    def __init__(
        self,
        path: str = None,
        repo: str = None,
        symlink: bool = None,
        workspace_id: str = None,
    ):
        # The full path of the code file or directory. The path must be prefixed with `/Workspace/code/`.
        # 
        # This parameter is required.
        self.path = path
        # The repository information.
        self.repo = repo
        # Specifies whether the item to delete is a symbolic link.
        self.symlink = symlink
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
        if self.path is not None:
            result['Path'] = self.path

        if self.repo is not None:
            result['Repo'] = self.repo

        if self.symlink is not None:
            result['Symlink'] = self.symlink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Repo') is not None:
            self.repo = m.get('Repo')

        if m.get('Symlink') is not None:
            self.symlink = m.get('Symlink')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

