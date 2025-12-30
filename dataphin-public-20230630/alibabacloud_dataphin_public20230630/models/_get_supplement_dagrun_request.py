# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSupplementDagrunRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        supplement_id: str = None,
    ):
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.supplement_id = supplement_id

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

        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')

        return self

