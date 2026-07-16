# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefundOrderResult(DaraModel):
    def __init__(
        self,
        dispute_id: str = None,
        dispute_status: int = None,
        order_line_id: str = None,
        request_id: str = None,
    ):
        # Dispute ID
        self.dispute_id = dispute_id
        # Status of the reverse operation  
        # 1 – Return pending  
        # 2 – Awaiting buyer return  
        # 3 – Awaiting merchant receipt  
        # 4 – Refund closed  
        # 5 – Refund succeeded  
        # 6 – Refund denied  
        # 17 – Canceling refund
        self.dispute_status = dispute_status
        # Sub-distribution order ID for which the reverse operation was initiated
        self.order_line_id = order_line_id
        # API request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dispute_id is not None:
            result['disputeId'] = self.dispute_id

        if self.dispute_status is not None:
            result['disputeStatus'] = self.dispute_status

        if self.order_line_id is not None:
            result['orderLineId'] = self.order_line_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disputeId') is not None:
            self.dispute_id = m.get('disputeId')

        if m.get('disputeStatus') is not None:
            self.dispute_status = m.get('disputeStatus')

        if m.get('orderLineId') is not None:
            self.order_line_id = m.get('orderLineId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

