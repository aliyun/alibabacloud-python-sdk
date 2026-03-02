# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMemoryShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        content: str = None,
        memory_node_id: str = None,
        meta_data_shrink: str = None,
        source: str = None,
        user_defined_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.content = content
        self.memory_node_id = memory_node_id
        self.meta_data_shrink = meta_data_shrink
        self.source = source
        # This parameter is required.
        self.user_defined_id = user_defined_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.content is not None:
            result['Content'] = self.content

        if self.memory_node_id is not None:
            result['MemoryNodeId'] = self.memory_node_id

        if self.meta_data_shrink is not None:
            result['MetaData'] = self.meta_data_shrink

        if self.source is not None:
            result['Source'] = self.source

        if self.user_defined_id is not None:
            result['UserDefinedId'] = self.user_defined_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('MemoryNodeId') is not None:
            self.memory_node_id = m.get('MemoryNodeId')

        if m.get('MetaData') is not None:
            self.meta_data_shrink = m.get('MetaData')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('UserDefinedId') is not None:
            self.user_defined_id = m.get('UserDefinedId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

