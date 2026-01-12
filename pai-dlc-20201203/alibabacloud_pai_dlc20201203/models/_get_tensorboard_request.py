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
        # The job ID. For more information about how to query the job ID, see [ListJob](https://help.aliyun.com/document_detail/459676.html).
        self.jod_id = jod_id
        # The information about the shared token. You can specify this parameter to obtain the permission to view a TensorBoard job based on the shared token information. You can execute [GetTensorboardSharedUrl](https://help.aliyun.com/document_detail/2557813.html) and extract the shared token from the obtained information.
        self.token = token
        # The workspace ID.
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

