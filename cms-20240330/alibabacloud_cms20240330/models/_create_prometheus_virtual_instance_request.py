# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePrometheusVirtualInstanceRequest(DaraModel):
    def __init__(
        self,
        namespace: str = None,
        tenant_id: str = None,
    ):
        # Each cloud product can only create one virtual instance in each region.
        # 
        # This parameter is required.
        self.namespace = namespace
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

