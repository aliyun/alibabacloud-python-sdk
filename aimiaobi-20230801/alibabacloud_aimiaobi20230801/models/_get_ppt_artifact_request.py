# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPptArtifactRequest(DaraModel):
    def __init__(
        self,
        external_user_id: str = None,
        ppt_artifact_id: int = None,
        workspace_id: str = None,
    ):
        self.external_user_id = external_user_id
        self.ppt_artifact_id = ppt_artifact_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id

        if self.ppt_artifact_id is not None:
            result['PptArtifactId'] = self.ppt_artifact_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')

        if m.get('PptArtifactId') is not None:
            self.ppt_artifact_id = m.get('PptArtifactId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

