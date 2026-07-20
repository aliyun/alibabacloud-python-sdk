# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightRefundPreCalV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightRefundPreCalV2ResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module
        self.module = module
        # requestId
        self.request_id = request_id
        self.success = success
        # traceId
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
            temp_model = main_models.FlightRefundPreCalV2ResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightRefundPreCalV2ResponseBodyModule(DaraModel):
    def __init__(
        self,
        multi_refund_fee_dtos: List[main_models.FlightRefundPreCalV2ResponseBodyModuleMultiRefundFeeDTOS] = None,
        pre_refund_money: int = None,
        refund_charge_fee: int = None,
        refund_reason_option_dtos: List[main_models.FlightRefundPreCalV2ResponseBodyModuleRefundReasonOptionDTOS] = None,
        service_charge_fee: int = None,
    ):
        self.multi_refund_fee_dtos = multi_refund_fee_dtos
        self.pre_refund_money = pre_refund_money
        self.refund_charge_fee = refund_charge_fee
        self.refund_reason_option_dtos = refund_reason_option_dtos
        self.service_charge_fee = service_charge_fee

    def validate(self):
        if self.multi_refund_fee_dtos:
            for v1 in self.multi_refund_fee_dtos:
                 if v1:
                    v1.validate()
        if self.refund_reason_option_dtos:
            for v1 in self.refund_reason_option_dtos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['multi_refund_fee_d_t_o_s'] = []
        if self.multi_refund_fee_dtos is not None:
            for k1 in self.multi_refund_fee_dtos:
                result['multi_refund_fee_d_t_o_s'].append(k1.to_map() if k1 else None)

        if self.pre_refund_money is not None:
            result['pre_refund_money'] = self.pre_refund_money

        if self.refund_charge_fee is not None:
            result['refund_charge_fee'] = self.refund_charge_fee

        result['refund_reason_option_d_t_o_s'] = []
        if self.refund_reason_option_dtos is not None:
            for k1 in self.refund_reason_option_dtos:
                result['refund_reason_option_d_t_o_s'].append(k1.to_map() if k1 else None)

        if self.service_charge_fee is not None:
            result['service_charge_fee'] = self.service_charge_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.multi_refund_fee_dtos = []
        if m.get('multi_refund_fee_d_t_o_s') is not None:
            for k1 in m.get('multi_refund_fee_d_t_o_s'):
                temp_model = main_models.FlightRefundPreCalV2ResponseBodyModuleMultiRefundFeeDTOS()
                self.multi_refund_fee_dtos.append(temp_model.from_map(k1))

        if m.get('pre_refund_money') is not None:
            self.pre_refund_money = m.get('pre_refund_money')

        if m.get('refund_charge_fee') is not None:
            self.refund_charge_fee = m.get('refund_charge_fee')

        self.refund_reason_option_dtos = []
        if m.get('refund_reason_option_d_t_o_s') is not None:
            for k1 in m.get('refund_reason_option_d_t_o_s'):
                temp_model = main_models.FlightRefundPreCalV2ResponseBodyModuleRefundReasonOptionDTOS()
                self.refund_reason_option_dtos.append(temp_model.from_map(k1))

        if m.get('service_charge_fee') is not None:
            self.service_charge_fee = m.get('service_charge_fee')

        return self

class FlightRefundPreCalV2ResponseBodyModuleRefundReasonOptionDTOS(DaraModel):
    def __init__(
        self,
        reason: str = None,
        reason_type: int = None,
        volunteer: bool = None,
    ):
        self.reason = reason
        self.reason_type = reason_type
        self.volunteer = volunteer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['reason'] = self.reason

        if self.reason_type is not None:
            result['reason_type'] = self.reason_type

        if self.volunteer is not None:
            result['volunteer'] = self.volunteer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('reason_type') is not None:
            self.reason_type = m.get('reason_type')

        if m.get('volunteer') is not None:
            self.volunteer = m.get('volunteer')

        return self

class FlightRefundPreCalV2ResponseBodyModuleMultiRefundFeeDTOS(DaraModel):
    def __init__(
        self,
        passenger_id: str = None,
        passenger_name: str = None,
        pre_refund_money: int = None,
        refund_charge_fee: int = None,
    ):
        self.passenger_id = passenger_id
        self.passenger_name = passenger_name
        self.pre_refund_money = pre_refund_money
        self.refund_charge_fee = refund_charge_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.pre_refund_money is not None:
            result['pre_refund_money'] = self.pre_refund_money

        if self.refund_charge_fee is not None:
            result['refund_charge_fee'] = self.refund_charge_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('pre_refund_money') is not None:
            self.pre_refund_money = m.get('pre_refund_money')

        if m.get('refund_charge_fee') is not None:
            self.refund_charge_fee = m.get('refund_charge_fee')

        return self

