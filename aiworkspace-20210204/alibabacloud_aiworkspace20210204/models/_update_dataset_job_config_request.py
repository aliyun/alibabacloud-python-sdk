# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDatasetJobConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        config_type: str = None,
        workspace_id: str = None,
    ):
        # The configuration content. Formats:
        # 
        # *   MultimodalIntelligentTag
        # 
        # { "apiKey":"sk-xxxxxxxxxxxxxxxxxxxxx" }
        # 
        # *   MultimodalSemanticIndex
        # 
        # { "defaultModelId": "xxx" "defaultModelVersion":"1.0.0" }
        self.config = config
        # The configuration type.
        # 
        # *   MultimodalIntelligentTag
        # *   MultimodalSemanticIndex
        self.config_type = config_type
        # The workspace ID.
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

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

