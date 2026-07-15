# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTensorboardRequest(DaraModel):
    def __init__(
        self,
        jod_id: str = None,
        token: str = None,
        workspace_id: str = None,
    ):
        # The job ID. Refer to [ListJobs](https://help.aliyun.com/document_detail/459676.html) to obtain the job ID.
        self.jod_id = jod_id
        # The sharing token. Specify this parameter to use the sharing token to obtain the permission to view a specific Tensorboard job. You can extract the token from the URL returned by calling [GetTensorboardSharedUrl](https://help.aliyun.com/document_detail/2557813.html).
        self.token = token
        # The workspace ID. <props="china">Refer to [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID..
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.jod_id is not None:
            result['JodId'] = self.jod_id

        if self.token is not None:
            result['Token'] = self.token

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JodId') is not None:
            self.jod_id = m.get('JodId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

