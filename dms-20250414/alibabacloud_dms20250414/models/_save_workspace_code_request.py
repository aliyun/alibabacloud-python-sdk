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
        # This parameter is required.
        self.content = content
        self.force = force
        self.iac = iac
        self.mtime = mtime
        # This parameter is required.
        self.path = path
        self.repo = repo
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

