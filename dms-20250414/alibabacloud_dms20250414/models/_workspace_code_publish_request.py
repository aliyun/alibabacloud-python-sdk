# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WorkspaceCodePublishRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        workspace_id: str = None,
    ):
        # The configuration for the code deployment, specified as a JSON string. The `repos` array identifies the Git repositories in the workspace and specifies the branch to deploy. The `exclude` array lists directories to skip during the deployment.
        # 
        # This parameter is required.
        self.config = config
        # The workspace ID (numeric ID) for the code deployment.
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
        if self.config is not None:
            result['Config'] = self.config

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

