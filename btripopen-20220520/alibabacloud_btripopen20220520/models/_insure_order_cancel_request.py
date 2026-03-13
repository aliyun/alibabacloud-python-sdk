# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsureOrderCancelRequest(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        buyer_name: str = None,
        isv_name: str = None,
        supplier_code: str = None,
    ):
        # This parameter is required.
        self.btrip_user_id = btrip_user_id
        self.buyer_name = buyer_name
        self.isv_name = isv_name
        self.supplier_code = supplier_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.buyer_name is not None:
            result['buyer_name'] = self.buyer_name

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.supplier_code is not None:
            result['supplier_code'] = self.supplier_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('buyer_name') is not None:
            self.buyer_name = m.get('buyer_name')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('supplier_code') is not None:
            self.supplier_code = m.get('supplier_code')

        return self

