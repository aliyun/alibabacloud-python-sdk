# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefundRenderCmd(DaraModel):
    def __init__(
        self,
        biz_claim_type: int = None,
        goods_status: int = None,
        order_line_id: str = None,
    ):
        # This parameter is required.
        self.biz_claim_type = biz_claim_type
        # This parameter is required.
        self.goods_status = goods_status
        # This parameter is required.
        self.order_line_id = order_line_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_claim_type is not None:
            result['bizClaimType'] = self.biz_claim_type

        if self.goods_status is not None:
            result['goodsStatus'] = self.goods_status

        if self.order_line_id is not None:
            result['orderLineId'] = self.order_line_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizClaimType') is not None:
            self.biz_claim_type = m.get('bizClaimType')

        if m.get('goodsStatus') is not None:
            self.goods_status = m.get('goodsStatus')

        if m.get('orderLineId') is not None:
            self.order_line_id = m.get('orderLineId')

        return self

