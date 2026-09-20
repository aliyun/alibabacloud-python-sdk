# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNodeIORequest(DaraModel):
    def __init__(
        self,
        io_type: str = None,
        node_id: int = None,
        project_env: str = None,
    ):
        # Specifies whether to query upstream or downstream nodes. Valid values: input and output.
        # 
        # This parameter is required.
        self.io_type = io_type
        # The ID of the node. You can call [ListNodes](https://help.aliyun.com/document_detail/173979.html) to query the NodeId.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The environment in which the node runs. Valid values: DEV (development environment) and PROD (production environment).
        # 
        # This parameter is required.
        self.project_env = project_env

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.io_type is not None:
            result['IoType'] = self.io_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoType') is not None:
            self.io_type = m.get('IoType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        return self

