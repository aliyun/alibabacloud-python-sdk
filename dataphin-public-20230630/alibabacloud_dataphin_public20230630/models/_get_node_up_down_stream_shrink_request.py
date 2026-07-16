# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNodeUpDownStreamShrinkRequest(DaraModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        env: str = None,
        node_id_shrink: str = None,
        op_tenant_id: int = None,
        project_id: int = None,
        up_stream_depth: int = None,
    ):
        # The downstream depth. Default value: 1.
        self.down_stream_depth = down_stream_depth
        # The environment identifier. Valid values:
        # - DEV: development environment. 
        # - PROD (default): production environment.
        self.env = env
        # The node ID.
        # 
        # This parameter is required.
        self.node_id_shrink = node_id_shrink
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The project ID.
        self.project_id = project_id
        # The upstream depth. Default value: 1.
        self.up_stream_depth = up_stream_depth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.down_stream_depth is not None:
            result['DownStreamDepth'] = self.down_stream_depth

        if self.env is not None:
            result['Env'] = self.env

        if self.node_id_shrink is not None:
            result['NodeId'] = self.node_id_shrink

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.up_stream_depth is not None:
            result['UpStreamDepth'] = self.up_stream_depth

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownStreamDepth') is not None:
            self.down_stream_depth = m.get('DownStreamDepth')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('NodeId') is not None:
            self.node_id_shrink = m.get('NodeId')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('UpStreamDepth') is not None:
            self.up_stream_depth = m.get('UpStreamDepth')

        return self

