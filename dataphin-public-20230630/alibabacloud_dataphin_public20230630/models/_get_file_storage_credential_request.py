# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFileStorageCredentialRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        project_id: int = None,
        purpose: str = None,
        use_vpc_endpoint: bool = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.project_id = project_id
        self.purpose = purpose
        self.use_vpc_endpoint = use_vpc_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.purpose is not None:
            result['Purpose'] = self.purpose

        if self.use_vpc_endpoint is not None:
            result['UseVpcEndpoint'] = self.use_vpc_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Purpose') is not None:
            self.purpose = m.get('Purpose')

        if m.get('UseVpcEndpoint') is not None:
            self.use_vpc_endpoint = m.get('UseVpcEndpoint')

        return self

