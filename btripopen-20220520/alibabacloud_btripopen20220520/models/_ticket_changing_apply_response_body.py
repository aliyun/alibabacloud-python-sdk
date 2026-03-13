# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TicketChangingApplyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TicketChangingApplyResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.TicketChangingApplyResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TicketChangingApplyResponseBodyModule(DaraModel):
    def __init__(
        self,
        booking_changed_total_fee: int = None,
        booking_origin_total_fee: int = None,
        booking_price_changed: bool = None,
        btrip_order_id: int = None,
        btrip_sub_order_id: int = None,
        can_pay: bool = None,
        change_fee: int = None,
        deadline_time: str = None,
        dis_order_id: str = None,
        dis_sub_order_id: str = None,
        max_retry_times: int = None,
        next_retry_interval: int = None,
        retry: bool = None,
        retry_client_tips: str = None,
        status: int = None,
        upgrade_fee: int = None,
    ):
        self.booking_changed_total_fee = booking_changed_total_fee
        self.booking_origin_total_fee = booking_origin_total_fee
        self.booking_price_changed = booking_price_changed
        self.btrip_order_id = btrip_order_id
        self.btrip_sub_order_id = btrip_sub_order_id
        self.can_pay = can_pay
        self.change_fee = change_fee
        self.deadline_time = deadline_time
        self.dis_order_id = dis_order_id
        self.dis_sub_order_id = dis_sub_order_id
        self.max_retry_times = max_retry_times
        self.next_retry_interval = next_retry_interval
        self.retry = retry
        self.retry_client_tips = retry_client_tips
        self.status = status
        self.upgrade_fee = upgrade_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.booking_changed_total_fee is not None:
            result['booking_changed_total_fee'] = self.booking_changed_total_fee

        if self.booking_origin_total_fee is not None:
            result['booking_origin_total_fee'] = self.booking_origin_total_fee

        if self.booking_price_changed is not None:
            result['booking_price_changed'] = self.booking_price_changed

        if self.btrip_order_id is not None:
            result['btrip_order_id'] = self.btrip_order_id

        if self.btrip_sub_order_id is not None:
            result['btrip_sub_order_id'] = self.btrip_sub_order_id

        if self.can_pay is not None:
            result['can_pay'] = self.can_pay

        if self.change_fee is not None:
            result['change_fee'] = self.change_fee

        if self.deadline_time is not None:
            result['deadline_time'] = self.deadline_time

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.dis_sub_order_id is not None:
            result['dis_sub_order_id'] = self.dis_sub_order_id

        if self.max_retry_times is not None:
            result['max_retry_times'] = self.max_retry_times

        if self.next_retry_interval is not None:
            result['next_retry_interval'] = self.next_retry_interval

        if self.retry is not None:
            result['retry'] = self.retry

        if self.retry_client_tips is not None:
            result['retry_client_tips'] = self.retry_client_tips

        if self.status is not None:
            result['status'] = self.status

        if self.upgrade_fee is not None:
            result['upgrade_fee'] = self.upgrade_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('booking_changed_total_fee') is not None:
            self.booking_changed_total_fee = m.get('booking_changed_total_fee')

        if m.get('booking_origin_total_fee') is not None:
            self.booking_origin_total_fee = m.get('booking_origin_total_fee')

        if m.get('booking_price_changed') is not None:
            self.booking_price_changed = m.get('booking_price_changed')

        if m.get('btrip_order_id') is not None:
            self.btrip_order_id = m.get('btrip_order_id')

        if m.get('btrip_sub_order_id') is not None:
            self.btrip_sub_order_id = m.get('btrip_sub_order_id')

        if m.get('can_pay') is not None:
            self.can_pay = m.get('can_pay')

        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')

        if m.get('deadline_time') is not None:
            self.deadline_time = m.get('deadline_time')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('dis_sub_order_id') is not None:
            self.dis_sub_order_id = m.get('dis_sub_order_id')

        if m.get('max_retry_times') is not None:
            self.max_retry_times = m.get('max_retry_times')

        if m.get('next_retry_interval') is not None:
            self.next_retry_interval = m.get('next_retry_interval')

        if m.get('retry') is not None:
            self.retry = m.get('retry')

        if m.get('retry_client_tips') is not None:
            self.retry_client_tips = m.get('retry_client_tips')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('upgrade_fee') is not None:
            self.upgrade_fee = m.get('upgrade_fee')

        return self

