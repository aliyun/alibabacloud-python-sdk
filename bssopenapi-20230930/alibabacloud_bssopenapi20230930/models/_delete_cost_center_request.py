# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCostCenterRequest(DaraModel):
    def __init__(
        self,
        cost_center_id: int = None,
        nbid: str = None,
        owner_account_id: int = None,
    ):
        # This parameter is required.
        self.cost_center_id = cost_center_id
        self.nbid = nbid
        # This parameter is required.
        self.owner_account_id = owner_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        return self

