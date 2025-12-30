# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceDownStreamShrinkRequest(DaraModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        env: str = None,
        instance_get_shrink: str = None,
        op_tenant_id: int = None,
        run_status: str = None,
    ):
        # This parameter is required.
        self.down_stream_depth = down_stream_depth
        self.env = env
        # This parameter is required.
        self.instance_get_shrink = instance_get_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.run_status = run_status

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

        if self.instance_get_shrink is not None:
            result['InstanceGet'] = self.instance_get_shrink

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.run_status is not None:
            result['RunStatus'] = self.run_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownStreamDepth') is not None:
            self.down_stream_depth = m.get('DownStreamDepth')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('InstanceGet') is not None:
            self.instance_get_shrink = m.get('InstanceGet')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('RunStatus') is not None:
            self.run_status = m.get('RunStatus')

        return self

