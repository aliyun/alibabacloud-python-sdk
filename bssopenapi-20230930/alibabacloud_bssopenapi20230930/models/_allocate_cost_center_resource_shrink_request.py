# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateCostCenterResourceShrinkRequest(DaraModel):
    def __init__(
        self,
        from_cost_center_id: int = None,
        from_owner_account_id: int = None,
        nbid: str = None,
        resource_instance_list_shrink: str = None,
        to_cost_center_id: int = None,
    ):
        self.from_cost_center_id = from_cost_center_id
        self.from_owner_account_id = from_owner_account_id
        self.nbid = nbid
        # This parameter is required.
        self.resource_instance_list_shrink = resource_instance_list_shrink
        self.to_cost_center_id = to_cost_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_cost_center_id is not None:
            result['FromCostCenterId'] = self.from_cost_center_id

        if self.from_owner_account_id is not None:
            result['FromOwnerAccountId'] = self.from_owner_account_id

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.resource_instance_list_shrink is not None:
            result['ResourceInstanceList'] = self.resource_instance_list_shrink

        if self.to_cost_center_id is not None:
            result['ToCostCenterId'] = self.to_cost_center_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromCostCenterId') is not None:
            self.from_cost_center_id = m.get('FromCostCenterId')

        if m.get('FromOwnerAccountId') is not None:
            self.from_owner_account_id = m.get('FromOwnerAccountId')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('ResourceInstanceList') is not None:
            self.resource_instance_list_shrink = m.get('ResourceInstanceList')

        if m.get('ToCostCenterId') is not None:
            self.to_cost_center_id = m.get('ToCostCenterId')

        return self

