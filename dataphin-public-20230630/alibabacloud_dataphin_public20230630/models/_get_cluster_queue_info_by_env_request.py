# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetClusterQueueInfoByEnvRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        project_id: int = None,
        stream_batch_mode: str = None,
    ):
        # This parameter is required.
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.stream_batch_mode = stream_batch_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.stream_batch_mode is not None:
            result['StreamBatchMode'] = self.stream_batch_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StreamBatchMode') is not None:
            self.stream_batch_mode = m.get('StreamBatchMode')

        return self

