# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteDataPermissionsRequest(DaraModel):
    def __init__(
        self,
        ids: List[int] = None,
        workspace_id: str = None,
    ):
        # The permission IDs.
        # 
        # This parameter is required.
        self.ids = ids
        # The unique ID of the Alibaba Cloud Model Studio workspace. For more information, see [Get a workspace ID](https://help.aliyun.com/document_detail/2587495.html).
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
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

