# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveContextDatabaseSyncJobExclusionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        document_id: str = None,
        job_id: str = None,
        workspace_id: str = None,
    ):
        # The idempotency token.
        self.client_token = client_token
        # The document ID.
        # 
        # This parameter is required.
        self.document_id = document_id
        # The job ID, which is a system-generated UUID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The workspace ID.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

