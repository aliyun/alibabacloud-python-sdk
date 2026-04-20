# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveWorkspaceUserRequest(DaraModel):
    def __init__(
        self,
        dms_user_ids: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.dms_user_ids = dms_user_ids
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dms_user_ids is not None:
            result['DmsUserIds'] = self.dms_user_ids

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DmsUserIds') is not None:
            self.dms_user_ids = m.get('DmsUserIds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

