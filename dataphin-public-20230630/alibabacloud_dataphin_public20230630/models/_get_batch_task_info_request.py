# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBatchTaskInfoRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        file_id: int = None,
        include_all_up_streams: bool = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.file_id = file_id
        self.include_all_up_streams = include_all_up_streams
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.include_all_up_streams is not None:
            result['IncludeAllUpStreams'] = self.include_all_up_streams

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('IncludeAllUpStreams') is not None:
            self.include_all_up_streams = m.get('IncludeAllUpStreams')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

