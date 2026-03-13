# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightRefundPreCalResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightRefundPreCalResponseBodyModule = None,
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
            temp_model = main_models.FlightRefundPreCalResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightRefundPreCalResponseBodyModule(DaraModel):
    def __init__(
        self,
        flight_change: bool = None,
        item_unit_id: str = None,
        multi_refund_cal_list: List[main_models.FlightRefundPreCalResponseBodyModuleMultiRefundCalList] = None,
        pre_refund_money: int = None,
        refund_fee: int = None,
        return_reason: List[main_models.FlightRefundPreCalResponseBodyModuleReturnReason] = None,
        session_id: str = None,
        tips: str = None,
    ):
        self.flight_change = flight_change
        self.item_unit_id = item_unit_id
        self.multi_refund_cal_list = multi_refund_cal_list
        self.pre_refund_money = pre_refund_money
        self.refund_fee = refund_fee
        self.return_reason = return_reason
        self.session_id = session_id
        self.tips = tips

    def validate(self):
        if self.multi_refund_cal_list:
            for v1 in self.multi_refund_cal_list:
                 if v1:
                    v1.validate()
        if self.return_reason:
            for v1 in self.return_reason:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flight_change is not None:
            result['flight_change'] = self.flight_change

        if self.item_unit_id is not None:
            result['item_unit_id'] = self.item_unit_id

        result['multi_refund_cal_list'] = []
        if self.multi_refund_cal_list is not None:
            for k1 in self.multi_refund_cal_list:
                result['multi_refund_cal_list'].append(k1.to_map() if k1 else None)

        if self.pre_refund_money is not None:
            result['pre_refund_money'] = self.pre_refund_money

        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee

        result['return_reason'] = []
        if self.return_reason is not None:
            for k1 in self.return_reason:
                result['return_reason'].append(k1.to_map() if k1 else None)

        if self.session_id is not None:
            result['session_id'] = self.session_id

        if self.tips is not None:
            result['tips'] = self.tips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flight_change') is not None:
            self.flight_change = m.get('flight_change')

        if m.get('item_unit_id') is not None:
            self.item_unit_id = m.get('item_unit_id')

        self.multi_refund_cal_list = []
        if m.get('multi_refund_cal_list') is not None:
            for k1 in m.get('multi_refund_cal_list'):
                temp_model = main_models.FlightRefundPreCalResponseBodyModuleMultiRefundCalList()
                self.multi_refund_cal_list.append(temp_model.from_map(k1))

        if m.get('pre_refund_money') is not None:
            self.pre_refund_money = m.get('pre_refund_money')

        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')

        self.return_reason = []
        if m.get('return_reason') is not None:
            for k1 in m.get('return_reason'):
                temp_model = main_models.FlightRefundPreCalResponseBodyModuleReturnReason()
                self.return_reason.append(temp_model.from_map(k1))

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('tips') is not None:
            self.tips = m.get('tips')

        return self

class FlightRefundPreCalResponseBodyModuleReturnReason(DaraModel):
    def __init__(
        self,
        extend_desc: str = None,
        person: int = None,
        reason_code: int = None,
        reason_show: str = None,
        reason_type: int = None,
        volunteer: int = None,
    ):
        self.extend_desc = extend_desc
        self.person = person
        self.reason_code = reason_code
        self.reason_show = reason_show
        self.reason_type = reason_type
        self.volunteer = volunteer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend_desc is not None:
            result['extend_desc'] = self.extend_desc

        if self.person is not None:
            result['person'] = self.person

        if self.reason_code is not None:
            result['reason_code'] = self.reason_code

        if self.reason_show is not None:
            result['reason_show'] = self.reason_show

        if self.reason_type is not None:
            result['reason_type'] = self.reason_type

        if self.volunteer is not None:
            result['volunteer'] = self.volunteer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extend_desc') is not None:
            self.extend_desc = m.get('extend_desc')

        if m.get('person') is not None:
            self.person = m.get('person')

        if m.get('reason_code') is not None:
            self.reason_code = m.get('reason_code')

        if m.get('reason_show') is not None:
            self.reason_show = m.get('reason_show')

        if m.get('reason_type') is not None:
            self.reason_type = m.get('reason_type')

        if m.get('volunteer') is not None:
            self.volunteer = m.get('volunteer')

        return self

class FlightRefundPreCalResponseBodyModuleMultiRefundCalList(DaraModel):
    def __init__(
        self,
        can_apply_refund: bool = None,
        name: str = None,
        pre_refund_money: int = None,
        refund_fee: int = None,
        user_id: str = None,
    ):
        self.can_apply_refund = can_apply_refund
        self.name = name
        self.pre_refund_money = pre_refund_money
        self.refund_fee = refund_fee
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_apply_refund is not None:
            result['can_apply_refund'] = self.can_apply_refund

        if self.name is not None:
            result['name'] = self.name

        if self.pre_refund_money is not None:
            result['pre_refund_money'] = self.pre_refund_money

        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('can_apply_refund') is not None:
            self.can_apply_refund = m.get('can_apply_refund')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pre_refund_money') is not None:
            self.pre_refund_money = m.get('pre_refund_money')

        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

