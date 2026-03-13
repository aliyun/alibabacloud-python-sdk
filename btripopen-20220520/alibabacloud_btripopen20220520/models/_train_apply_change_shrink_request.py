# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrainApplyChangeShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_no_seat: str = None,
        change_train_info_sshrink: str = None,
        force_match: str = None,
        is_pay_now: bool = None,
        order_id: str = None,
        out_change_apply_id: str = None,
        out_order_id: str = None,
    ):
        self.accept_no_seat = accept_no_seat
        # This parameter is required.
        self.change_train_info_sshrink = change_train_info_sshrink
        self.force_match = force_match
        self.is_pay_now = is_pay_now
        # This parameter is required.
        self.order_id = order_id
        # This parameter is required.
        self.out_change_apply_id = out_change_apply_id
        # This parameter is required.
        self.out_order_id = out_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_no_seat is not None:
            result['accept_no_seat'] = self.accept_no_seat

        if self.change_train_info_sshrink is not None:
            result['change_train_info_s'] = self.change_train_info_sshrink

        if self.force_match is not None:
            result['force_match'] = self.force_match

        if self.is_pay_now is not None:
            result['is_pay_now'] = self.is_pay_now

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_change_apply_id is not None:
            result['out_change_apply_id'] = self.out_change_apply_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accept_no_seat') is not None:
            self.accept_no_seat = m.get('accept_no_seat')

        if m.get('change_train_info_s') is not None:
            self.change_train_info_sshrink = m.get('change_train_info_s')

        if m.get('force_match') is not None:
            self.force_match = m.get('force_match')

        if m.get('is_pay_now') is not None:
            self.is_pay_now = m.get('is_pay_now')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_change_apply_id') is not None:
            self.out_change_apply_id = m.get('out_change_apply_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        return self

