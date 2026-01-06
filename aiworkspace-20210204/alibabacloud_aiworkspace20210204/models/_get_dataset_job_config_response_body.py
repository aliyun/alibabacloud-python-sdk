# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDatasetJobConfigResponseBody(DaraModel):
    def __init__(
        self,
        config: str = None,
        config_type: str = None,
        create_time: str = None,
        dataset_id: str = None,
        modify_time: str = None,
        request_id: str = None,
        workspace_id: str = None,
    ):
        # The configuration content. Configuration format for MultimodalIntelligentTag:
        # 
        # { "apiKey":"sk-xxxxxxxxxxxxxxxxxxxxx" }
        # 
        # MultimodalSemanticIndex
        # 
        # { "defaultModelId": "xxx" "defaultModelVersion":"1.0.0" }
        self.config = config
        # The configuration type. Valid values:
        # 
        # *   MultimodalIntelligentTag
        # *   MultimodalSemanticIndex
        self.config_type = config_type
        # The time when the configuration is created.
        self.create_time = create_time
        # The dataset ID.
        self.dataset_id = dataset_id
        # The time when the configuration is modified.
        self.modify_time = modify_time
        # The request ID.
        self.request_id = request_id
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

