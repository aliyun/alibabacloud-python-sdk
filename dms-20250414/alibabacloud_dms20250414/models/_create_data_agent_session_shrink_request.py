# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataAgentSessionShrinkRequest(DaraModel):
    def __init__(
        self,
        dmsunit: str = None,
        file: str = None,
        session_config_shrink: str = None,
        title: str = None,
        workspace_id: str = None,
    ):
        self.dmsunit = dmsunit
        self.file = file
        self.session_config_shrink = session_config_shrink
        self.title = title
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

        if self.file is not None:
            result['File'] = self.file

        if self.session_config_shrink is not None:
            result['SessionConfig'] = self.session_config_shrink

        if self.title is not None:
            result['Title'] = self.title

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('File') is not None:
            self.file = m.get('File')

        if m.get('SessionConfig') is not None:
            self.session_config_shrink = m.get('SessionConfig')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

