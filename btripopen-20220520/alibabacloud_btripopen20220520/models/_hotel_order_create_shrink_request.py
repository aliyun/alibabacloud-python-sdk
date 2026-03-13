# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotelOrderCreateShrinkRequest(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        check_in: str = None,
        check_out: str = None,
        contract_email: str = None,
        contract_name: str = None,
        contract_phone: str = None,
        corp_pay_price: int = None,
        dis_order_id: str = None,
        extra: str = None,
        invoice_info_shrink: str = None,
        item_id: int = None,
        itinerary_no: str = None,
        member_info_shrink: str = None,
        occupant_info_list_shrink: str = None,
        person_pay_price: int = None,
        promotion_info_shrink: str = None,
        rate_plan_id: int = None,
        room_id: int = None,
        room_num: int = None,
        seller_id: int = None,
        shid: int = None,
        total_order_price: int = None,
        validate_res_key: str = None,
    ):
        # This parameter is required.
        self.btrip_user_id = btrip_user_id
        # This parameter is required.
        self.check_in = check_in
        # This parameter is required.
        self.check_out = check_out
        self.contract_email = contract_email
        self.contract_name = contract_name
        # This parameter is required.
        self.contract_phone = contract_phone
        # This parameter is required.
        self.corp_pay_price = corp_pay_price
        # This parameter is required.
        self.dis_order_id = dis_order_id
        self.extra = extra
        self.invoice_info_shrink = invoice_info_shrink
        # This parameter is required.
        self.item_id = item_id
        # This parameter is required.
        self.itinerary_no = itinerary_no
        self.member_info_shrink = member_info_shrink
        # This parameter is required.
        self.occupant_info_list_shrink = occupant_info_list_shrink
        # This parameter is required.
        self.person_pay_price = person_pay_price
        self.promotion_info_shrink = promotion_info_shrink
        # This parameter is required.
        self.rate_plan_id = rate_plan_id
        # This parameter is required.
        self.room_id = room_id
        # This parameter is required.
        self.room_num = room_num
        # This parameter is required.
        self.seller_id = seller_id
        # This parameter is required.
        self.shid = shid
        # This parameter is required.
        self.total_order_price = total_order_price
        # This parameter is required.
        self.validate_res_key = validate_res_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.check_in is not None:
            result['check_in'] = self.check_in

        if self.check_out is not None:
            result['check_out'] = self.check_out

        if self.contract_email is not None:
            result['contract_email'] = self.contract_email

        if self.contract_name is not None:
            result['contract_name'] = self.contract_name

        if self.contract_phone is not None:
            result['contract_phone'] = self.contract_phone

        if self.corp_pay_price is not None:
            result['corp_pay_price'] = self.corp_pay_price

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.extra is not None:
            result['extra'] = self.extra

        if self.invoice_info_shrink is not None:
            result['invoice_info'] = self.invoice_info_shrink

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.itinerary_no is not None:
            result['itinerary_no'] = self.itinerary_no

        if self.member_info_shrink is not None:
            result['member_info'] = self.member_info_shrink

        if self.occupant_info_list_shrink is not None:
            result['occupant_info_list'] = self.occupant_info_list_shrink

        if self.person_pay_price is not None:
            result['person_pay_price'] = self.person_pay_price

        if self.promotion_info_shrink is not None:
            result['promotion_info'] = self.promotion_info_shrink

        if self.rate_plan_id is not None:
            result['rate_plan_id'] = self.rate_plan_id

        if self.room_id is not None:
            result['room_id'] = self.room_id

        if self.room_num is not None:
            result['room_num'] = self.room_num

        if self.seller_id is not None:
            result['seller_id'] = self.seller_id

        if self.shid is not None:
            result['shid'] = self.shid

        if self.total_order_price is not None:
            result['total_order_price'] = self.total_order_price

        if self.validate_res_key is not None:
            result['validate_res_key'] = self.validate_res_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')

        if m.get('check_out') is not None:
            self.check_out = m.get('check_out')

        if m.get('contract_email') is not None:
            self.contract_email = m.get('contract_email')

        if m.get('contract_name') is not None:
            self.contract_name = m.get('contract_name')

        if m.get('contract_phone') is not None:
            self.contract_phone = m.get('contract_phone')

        if m.get('corp_pay_price') is not None:
            self.corp_pay_price = m.get('corp_pay_price')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('invoice_info') is not None:
            self.invoice_info_shrink = m.get('invoice_info')

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('itinerary_no') is not None:
            self.itinerary_no = m.get('itinerary_no')

        if m.get('member_info') is not None:
            self.member_info_shrink = m.get('member_info')

        if m.get('occupant_info_list') is not None:
            self.occupant_info_list_shrink = m.get('occupant_info_list')

        if m.get('person_pay_price') is not None:
            self.person_pay_price = m.get('person_pay_price')

        if m.get('promotion_info') is not None:
            self.promotion_info_shrink = m.get('promotion_info')

        if m.get('rate_plan_id') is not None:
            self.rate_plan_id = m.get('rate_plan_id')

        if m.get('room_id') is not None:
            self.room_id = m.get('room_id')

        if m.get('room_num') is not None:
            self.room_num = m.get('room_num')

        if m.get('seller_id') is not None:
            self.seller_id = m.get('seller_id')

        if m.get('shid') is not None:
            self.shid = m.get('shid')

        if m.get('total_order_price') is not None:
            self.total_order_price = m.get('total_order_price')

        if m.get('validate_res_key') is not None:
            self.validate_res_key = m.get('validate_res_key')

        return self

