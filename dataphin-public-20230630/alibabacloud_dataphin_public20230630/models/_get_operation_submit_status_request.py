# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOperationSubmitStatusRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        job_id: str = None,
        op_tenant_id: int = None,
    ):
        # The environment identifier. Valid values:
        # - DEV: Development environment. 
        # - PROD (default): Production environment.
        self.env = env
        # The job ID returned after submission in batch mode.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

