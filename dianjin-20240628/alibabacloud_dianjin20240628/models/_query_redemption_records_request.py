# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRedemptionRecordsRequest(DaraModel):
    def __init__(
        self,
        external_user_id: str = None,
        page: int = None,
        page_size: int = None,
        redemption_order_no: str = None,
    ):
        self.external_user_id = external_user_id
        self.page = page
        self.page_size = page_size
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

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.redemption_order_no is not None:
            result['redemptionOrderNo'] = self.redemption_order_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalUserId') is not None:
            self.external_user_id = m.get('externalUserId')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('redemptionOrderNo') is not None:
            self.redemption_order_no = m.get('redemptionOrderNo')

        return self

