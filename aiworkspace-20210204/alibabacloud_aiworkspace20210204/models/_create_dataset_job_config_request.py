# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatasetJobConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        config_type: str = None,
        dataset_version: str = None,
        workspace_id: str = None,
    ):
        # The configuration content. Format:
        # 
        # *   MultimodalIntelligentTag
        # 
        # { "apiKey":"sk-xxxxxxxxxxxxxxxxxxxxx" }
        # 
        # *   MultimodalSemanticIndex
        # 
        # { "defaultModelId": "xxx" "defaultModelVersion":"1.0.0" }
        # 
        # This parameter is required.
        self.config = config
        # The configuration type.
        # 
        # Valid values:
        # 
        # *   MultimodalIntelligentTag
        # *   MultimodalSemanticIndex
        # 
        # This parameter is required.
        self.config_type = config_type
        self.dataset_version = dataset_version
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
        if self.config is not None:
            result['Config'] = self.config

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

