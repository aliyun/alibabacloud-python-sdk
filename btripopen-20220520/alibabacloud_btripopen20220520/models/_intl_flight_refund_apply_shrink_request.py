# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IntlFlightRefundApplyShrinkRequest(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        out_order_id: str = None,
        out_refund_apply_id: str = None,
        passenger_journey_group_key: str = None,
        refund_reason_code: str = None,
        refund_segment_list_shrink: str = None,
        selected_passengers_shrink: str = None,
    ):
        # This parameter is required.
        self.order_id = order_id
        self.out_order_id = out_order_id
        self.out_refund_apply_id = out_refund_apply_id
        # This parameter is required.
        self.passenger_journey_group_key = passenger_journey_group_key
        # This parameter is required.
        self.refund_reason_code = refund_reason_code
        # This parameter is required.
        self.refund_segment_list_shrink = refund_segment_list_shrink
        # This parameter is required.
        self.selected_passengers_shrink = selected_passengers_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.out_refund_apply_id is not None:
            result['out_refund_apply_id'] = self.out_refund_apply_id

        if self.passenger_journey_group_key is not None:
            result['passenger_journey_group_key'] = self.passenger_journey_group_key

        if self.refund_reason_code is not None:
            result['refund_reason_code'] = self.refund_reason_code

        if self.refund_segment_list_shrink is not None:
            result['refund_segment_list'] = self.refund_segment_list_shrink

        if self.selected_passengers_shrink is not None:
            result['selected_passengers'] = self.selected_passengers_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_refund_apply_id') is not None:
            self.out_refund_apply_id = m.get('out_refund_apply_id')

        if m.get('passenger_journey_group_key') is not None:
            self.passenger_journey_group_key = m.get('passenger_journey_group_key')

        if m.get('refund_reason_code') is not None:
            self.refund_reason_code = m.get('refund_reason_code')

        if m.get('refund_segment_list') is not None:
            self.refund_segment_list_shrink = m.get('refund_segment_list')

        if m.get('selected_passengers') is not None:
            self.selected_passengers_shrink = m.get('selected_passengers')

        return self

