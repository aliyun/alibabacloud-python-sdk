# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateModelLimitsShrinkRequest(DaraModel):
    def __init__(
        self,
        workspace_id: str = None,
        workspace_limits_shrink: str = None,
    ):
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id
        # The throttling values for the workspace.
        self.workspace_limits_shrink = workspace_limits_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        if self.workspace_limits_shrink is not None:
            result['workspaceLimits'] = self.workspace_limits_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        if m.get('workspaceLimits') is not None:
            self.workspace_limits_shrink = m.get('workspaceLimits')

        return self

