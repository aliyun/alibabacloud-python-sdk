# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrainOrderCreateShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_no_seat: str = None,
        book_train_infos_shrink: str = None,
        btrip_user_id: str = None,
        btrip_user_name: str = None,
        business_info_shrink: str = None,
        contact_info_shrink: str = None,
        force_match: str = None,
        is_pay_now: bool = None,
        out_order_id: str = None,
        passenger_open_info_sshrink: str = None,
    ):
        self.accept_no_seat = accept_no_seat
        # This parameter is required.
        self.book_train_infos_shrink = book_train_infos_shrink
        # This parameter is required.
        self.btrip_user_id = btrip_user_id
        # This parameter is required.
        self.btrip_user_name = btrip_user_name
        self.business_info_shrink = business_info_shrink
        # This parameter is required.
        self.contact_info_shrink = contact_info_shrink
        self.force_match = force_match
        self.is_pay_now = is_pay_now
        # This parameter is required.
        self.out_order_id = out_order_id
        # This parameter is required.
        self.passenger_open_info_sshrink = passenger_open_info_sshrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_no_seat is not None:
            result['accept_no_seat'] = self.accept_no_seat

        if self.book_train_infos_shrink is not None:
            result['book_train_infos'] = self.book_train_infos_shrink

        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.btrip_user_name is not None:
            result['btrip_user_name'] = self.btrip_user_name

        if self.business_info_shrink is not None:
            result['business_info'] = self.business_info_shrink

        if self.contact_info_shrink is not None:
            result['contact_info'] = self.contact_info_shrink

        if self.force_match is not None:
            result['force_match'] = self.force_match

        if self.is_pay_now is not None:
            result['is_pay_now'] = self.is_pay_now

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.passenger_open_info_sshrink is not None:
            result['passenger_open_info_s'] = self.passenger_open_info_sshrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accept_no_seat') is not None:
            self.accept_no_seat = m.get('accept_no_seat')

        if m.get('book_train_infos') is not None:
            self.book_train_infos_shrink = m.get('book_train_infos')

        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('btrip_user_name') is not None:
            self.btrip_user_name = m.get('btrip_user_name')

        if m.get('business_info') is not None:
            self.business_info_shrink = m.get('business_info')

        if m.get('contact_info') is not None:
            self.contact_info_shrink = m.get('contact_info')

        if m.get('force_match') is not None:
            self.force_match = m.get('force_match')

        if m.get('is_pay_now') is not None:
            self.is_pay_now = m.get('is_pay_now')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('passenger_open_info_s') is not None:
            self.passenger_open_info_sshrink = m.get('passenger_open_info_s')

        return self

