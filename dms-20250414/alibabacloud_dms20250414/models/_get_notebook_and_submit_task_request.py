# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNotebookAndSubmitTaskRequest(DaraModel):
    def __init__(
        self,
        params: str = None,
        path: str = None,
        retry: int = None,
        session_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.params = params
        # This parameter is required.
        self.path = path
        self.retry = retry
        # This parameter is required.
        self.session_id = session_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.params is not None:
            result['Params'] = self.params

        if self.path is not None:
            result['Path'] = self.path

        if self.retry is not None:
            result['Retry'] = self.retry

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Retry') is not None:
            self.retry = m.get('Retry')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

