# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelPickUpWaybillRequest(DaraModel):
    def __init__(
        self,
        cancel_desc: str = None,
        outer_order_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The cancellation reason.
        # 
        # This parameter is required.
        self.cancel_desc = cancel_desc
        # The ID of the external order.
        # 
        # This parameter is required.
        self.outer_order_code = outer_order_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_desc is not None:
            result['CancelDesc'] = self.cancel_desc

        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelDesc') is not None:
            self.cancel_desc = m.get('CancelDesc')

        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

