# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTransferInfoRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        proposal_id: int = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.proposal_id = proposal_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.proposal_id is not None:
            result['ProposalId'] = self.proposal_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProposalId') is not None:
            self.proposal_id = m.get('ProposalId')

        return self

