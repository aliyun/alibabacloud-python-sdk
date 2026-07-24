# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefundApplyShrinkRequest(DaraModel):
    def __init__(
        self,
        order_num: int = None,
        refund_journeys_shrink: str = None,
        refund_passenger_list_shrink: str = None,
        refund_type_shrink: str = None,
    ):
        # The order number.
        # 
        # This parameter is required.
        self.order_num = order_num
        # The journeys for the refund application.
        # 
        # This parameter is required.
        self.refund_journeys_shrink = refund_journeys_shrink
        # The list of passengers for the refund application.
        # 
        # This parameter is required.
        self.refund_passenger_list_shrink = refund_passenger_list_shrink
        # The refund type. Attachments are required for involuntary refund applications.
        # 
        # This parameter is required.
        self.refund_type_shrink = refund_type_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_num is not None:
            result['order_num'] = self.order_num

        if self.refund_journeys_shrink is not None:
            result['refund_journeys'] = self.refund_journeys_shrink

        if self.refund_passenger_list_shrink is not None:
            result['refund_passenger_list'] = self.refund_passenger_list_shrink

        if self.refund_type_shrink is not None:
            result['refund_type'] = self.refund_type_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        if m.get('refund_journeys') is not None:
            self.refund_journeys_shrink = m.get('refund_journeys')

        if m.get('refund_passenger_list') is not None:
            self.refund_passenger_list_shrink = m.get('refund_passenger_list')

        if m.get('refund_type') is not None:
            self.refund_type_shrink = m.get('refund_type')

        return self

