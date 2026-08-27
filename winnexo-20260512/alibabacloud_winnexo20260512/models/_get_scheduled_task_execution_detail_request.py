# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScheduledTaskExecutionDetailRequest(DaraModel):
    def __init__(
        self,
        execution_id: str = None,
        tenant_id: str = None,
    ):
        # The execution record ID.
        # 
        # This parameter is required.
        self.execution_id = execution_id
        # The tenant ID that takes effect.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_id is not None:
            result['executionId'] = self.execution_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('executionId') is not None:
            self.execution_id = m.get('executionId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

