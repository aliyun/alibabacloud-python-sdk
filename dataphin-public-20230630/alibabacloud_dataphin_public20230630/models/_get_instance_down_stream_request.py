# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetInstanceDownStreamRequest(DaraModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        env: str = None,
        instance_get: main_models.GetInstanceDownStreamRequestInstanceGet = None,
        op_tenant_id: int = None,
        run_status: str = None,
    ):
        # This parameter is required.
        self.down_stream_depth = down_stream_depth
        self.env = env
        # This parameter is required.
        self.instance_get = instance_get
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.run_status = run_status

    def validate(self):
        if self.instance_get:
            self.instance_get.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.down_stream_depth is not None:
            result['DownStreamDepth'] = self.down_stream_depth

        if self.env is not None:
            result['Env'] = self.env

        if self.instance_get is not None:
            result['InstanceGet'] = self.instance_get.to_map()

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
            temp_model = main_models.GetInstanceDownStreamRequestInstanceGet()
            self.instance_get = temp_model.from_map(m.get('InstanceGet'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('RunStatus') is not None:
            self.run_status = m.get('RunStatus')

        return self

class GetInstanceDownStreamRequestInstanceGet(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        node_type: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        return self

