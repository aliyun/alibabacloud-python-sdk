# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightRefundApplyRequest(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        out_order_id: str = None,
        out_refund_apply_id: str = None,
        passenger_journey_group_key: str = None,
        refund_reason_code: str = None,
        refund_segment_list: List[main_models.IntlFlightRefundApplyRequestRefundSegmentList] = None,
        selected_passengers: List[main_models.IntlFlightRefundApplyRequestSelectedPassengers] = None,
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
        self.refund_segment_list = refund_segment_list
        # This parameter is required.
        self.selected_passengers = selected_passengers

    def validate(self):
        if self.refund_segment_list:
            for v1 in self.refund_segment_list:
                 if v1:
                    v1.validate()
        if self.selected_passengers:
            for v1 in self.selected_passengers:
                 if v1:
                    v1.validate()

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

        result['refund_segment_list'] = []
        if self.refund_segment_list is not None:
            for k1 in self.refund_segment_list:
                result['refund_segment_list'].append(k1.to_map() if k1 else None)

        result['selected_passengers'] = []
        if self.selected_passengers is not None:
            for k1 in self.selected_passengers:
                result['selected_passengers'].append(k1.to_map() if k1 else None)

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

        self.refund_segment_list = []
        if m.get('refund_segment_list') is not None:
            for k1 in m.get('refund_segment_list'):
                temp_model = main_models.IntlFlightRefundApplyRequestRefundSegmentList()
                self.refund_segment_list.append(temp_model.from_map(k1))

        self.selected_passengers = []
        if m.get('selected_passengers') is not None:
            for k1 in m.get('selected_passengers'):
                temp_model = main_models.IntlFlightRefundApplyRequestSelectedPassengers()
                self.selected_passengers.append(temp_model.from_map(k1))

        return self

class IntlFlightRefundApplyRequestSelectedPassengers(DaraModel):
    def __init__(
        self,
        full_name: str = None,
        passenger_id: int = None,
    ):
        self.full_name = full_name
        # This parameter is required.
        self.passenger_id = passenger_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full_name is not None:
            result['full_name'] = self.full_name

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('full_name') is not None:
            self.full_name = m.get('full_name')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        return self

class IntlFlightRefundApplyRequestRefundSegmentList(DaraModel):
    def __init__(
        self,
        segment_key: str = None,
    ):
        # This parameter is required.
        self.segment_key = segment_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.segment_key is not None:
            result['segment_key'] = self.segment_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('segment_key') is not None:
            self.segment_key = m.get('segment_key')

        return self

