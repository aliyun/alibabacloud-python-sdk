# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightRefundApplyRequest(DaraModel):
    def __init__(
        self,
        corp_refund_price: int = None,
        dis_order_id: str = None,
        dis_sub_order_id: str = None,
        display_refund_money: str = None,
        extra: Dict[str, str] = None,
        is_voluntary: int = None,
        item_unit_ids: str = None,
        passenger_segment_info_list: List[main_models.FlightRefundApplyRequestPassengerSegmentInfoList] = None,
        personal_refund_price: int = None,
        reason_detail: str = None,
        reason_type: int = None,
        refund_voucher_info: List[str] = None,
        session_id: str = None,
        total_refund_price: int = None,
    ):
        self.corp_refund_price = corp_refund_price
        # This parameter is required.
        self.dis_order_id = dis_order_id
        # This parameter is required.
        self.dis_sub_order_id = dis_sub_order_id
        # This parameter is required.
        self.display_refund_money = display_refund_money
        self.extra = extra
        # This parameter is required.
        self.is_voluntary = is_voluntary
        # This parameter is required.
        self.item_unit_ids = item_unit_ids
        self.passenger_segment_info_list = passenger_segment_info_list
        self.personal_refund_price = personal_refund_price
        self.reason_detail = reason_detail
        # This parameter is required.
        self.reason_type = reason_type
        self.refund_voucher_info = refund_voucher_info
        # This parameter is required.
        self.session_id = session_id
        self.total_refund_price = total_refund_price

    def validate(self):
        if self.passenger_segment_info_list:
            for v1 in self.passenger_segment_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_refund_price is not None:
            result['corp_refund_price'] = self.corp_refund_price

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.dis_sub_order_id is not None:
            result['dis_sub_order_id'] = self.dis_sub_order_id

        if self.display_refund_money is not None:
            result['display_refund_money'] = self.display_refund_money

        if self.extra is not None:
            result['extra'] = self.extra

        if self.is_voluntary is not None:
            result['is_voluntary'] = self.is_voluntary

        if self.item_unit_ids is not None:
            result['item_unit_ids'] = self.item_unit_ids

        result['passenger_segment_info_list'] = []
        if self.passenger_segment_info_list is not None:
            for k1 in self.passenger_segment_info_list:
                result['passenger_segment_info_list'].append(k1.to_map() if k1 else None)

        if self.personal_refund_price is not None:
            result['personal_refund_price'] = self.personal_refund_price

        if self.reason_detail is not None:
            result['reason_detail'] = self.reason_detail

        if self.reason_type is not None:
            result['reason_type'] = self.reason_type

        if self.refund_voucher_info is not None:
            result['refund_voucher_info'] = self.refund_voucher_info

        if self.session_id is not None:
            result['session_id'] = self.session_id

        if self.total_refund_price is not None:
            result['total_refund_price'] = self.total_refund_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_refund_price') is not None:
            self.corp_refund_price = m.get('corp_refund_price')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('dis_sub_order_id') is not None:
            self.dis_sub_order_id = m.get('dis_sub_order_id')

        if m.get('display_refund_money') is not None:
            self.display_refund_money = m.get('display_refund_money')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('is_voluntary') is not None:
            self.is_voluntary = m.get('is_voluntary')

        if m.get('item_unit_ids') is not None:
            self.item_unit_ids = m.get('item_unit_ids')

        self.passenger_segment_info_list = []
        if m.get('passenger_segment_info_list') is not None:
            for k1 in m.get('passenger_segment_info_list'):
                temp_model = main_models.FlightRefundApplyRequestPassengerSegmentInfoList()
                self.passenger_segment_info_list.append(temp_model.from_map(k1))

        if m.get('personal_refund_price') is not None:
            self.personal_refund_price = m.get('personal_refund_price')

        if m.get('reason_detail') is not None:
            self.reason_detail = m.get('reason_detail')

        if m.get('reason_type') is not None:
            self.reason_type = m.get('reason_type')

        if m.get('refund_voucher_info') is not None:
            self.refund_voucher_info = m.get('refund_voucher_info')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('total_refund_price') is not None:
            self.total_refund_price = m.get('total_refund_price')

        return self

class FlightRefundApplyRequestPassengerSegmentInfoList(DaraModel):
    def __init__(
        self,
        flight_no: str = None,
        passenger_name: str = None,
        user_id: str = None,
    ):
        self.flight_no = flight_no
        self.passenger_name = passenger_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

