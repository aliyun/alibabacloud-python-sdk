# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUsageRequest(DaraModel):
    def __init__(
        self,
        external_user_id: str = None,
        redemption_order_no: str = None,
    ):
        self.external_user_id = external_user_id
        self.redemption_order_no = redemption_order_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_user_id is not None:
            result['externalUserId'] = self.external_user_id

        if self.redemption_order_no is not None:
            result['redemptionOrderNo'] = self.redemption_order_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalUserId') is not None:
            self.external_user_id = m.get('externalUserId')

        if m.get('redemptionOrderNo') is not None:
            self.redemption_order_no = m.get('redemptionOrderNo')

        return self

