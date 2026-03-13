# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlightRefundApplyV2ShrinkRequest(DaraModel):
    def __init__(
        self,
        isv_name: str = None,
        order_id: str = None,
        out_order_id: str = None,
        out_sub_order_id: str = None,
        passenger_segment_relations_shrink: str = None,
        pre_cal_type: int = None,
        refund_reason: str = None,
        refund_reason_type: int = None,
        ticket_nos_shrink: str = None,
        total_refund_price: int = None,
        upload_pict_urls: str = None,
        voluntary: bool = None,
    ):
        self.isv_name = isv_name
        self.order_id = order_id
        self.out_order_id = out_order_id
        self.out_sub_order_id = out_sub_order_id
        self.passenger_segment_relations_shrink = passenger_segment_relations_shrink
        self.pre_cal_type = pre_cal_type
        self.refund_reason = refund_reason
        self.refund_reason_type = refund_reason_type
        self.ticket_nos_shrink = ticket_nos_shrink
        self.total_refund_price = total_refund_price
        self.upload_pict_urls = upload_pict_urls
        self.voluntary = voluntary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.out_sub_order_id is not None:
            result['out_sub_order_id'] = self.out_sub_order_id

        if self.passenger_segment_relations_shrink is not None:
            result['passenger_segment_relations'] = self.passenger_segment_relations_shrink

        if self.pre_cal_type is not None:
            result['pre_cal_type'] = self.pre_cal_type

        if self.refund_reason is not None:
            result['refund_reason'] = self.refund_reason

        if self.refund_reason_type is not None:
            result['refund_reason_type'] = self.refund_reason_type

        if self.ticket_nos_shrink is not None:
            result['ticket_nos'] = self.ticket_nos_shrink

        if self.total_refund_price is not None:
            result['total_refund_price'] = self.total_refund_price

        if self.upload_pict_urls is not None:
            result['upload_pict_urls'] = self.upload_pict_urls

        if self.voluntary is not None:
            result['voluntary'] = self.voluntary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_sub_order_id') is not None:
            self.out_sub_order_id = m.get('out_sub_order_id')

        if m.get('passenger_segment_relations') is not None:
            self.passenger_segment_relations_shrink = m.get('passenger_segment_relations')

        if m.get('pre_cal_type') is not None:
            self.pre_cal_type = m.get('pre_cal_type')

        if m.get('refund_reason') is not None:
            self.refund_reason = m.get('refund_reason')

        if m.get('refund_reason_type') is not None:
            self.refund_reason_type = m.get('refund_reason_type')

        if m.get('ticket_nos') is not None:
            self.ticket_nos_shrink = m.get('ticket_nos')

        if m.get('total_refund_price') is not None:
            self.total_refund_price = m.get('total_refund_price')

        if m.get('upload_pict_urls') is not None:
            self.upload_pict_urls = m.get('upload_pict_urls')

        if m.get('voluntary') is not None:
            self.voluntary = m.get('voluntary')

        return self

