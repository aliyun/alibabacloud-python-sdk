# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class MealOrderListQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.MealOrderListQueryResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
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
            temp_model = main_models.MealOrderListQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class MealOrderListQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        order_list: List[main_models.MealOrderListQueryResponseBodyModuleOrderList] = None,
    ):
        self.order_list = order_list

    def validate(self):
        if self.order_list:
            for v1 in self.order_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['order_list'] = []
        if self.order_list is not None:
            for k1 in self.order_list:
                result['order_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_list = []
        if m.get('order_list') is not None:
            for k1 in m.get('order_list'):
                temp_model = main_models.MealOrderListQueryResponseBodyModuleOrderList()
                self.order_list.append(temp_model.from_map(k1))

        return self

class MealOrderListQueryResponseBodyModuleOrderList(DaraModel):
    def __init__(
        self,
        corp_pay_amount: int = None,
        merchant_name: str = None,
        order_id: str = None,
        order_status: int = None,
        order_type: str = None,
        pay_amount: int = None,
        person_pay_amount: int = None,
        settle_time: str = None,
    ):
        self.corp_pay_amount = corp_pay_amount
        self.merchant_name = merchant_name
        self.order_id = order_id
        self.order_status = order_status
        self.order_type = order_type
        self.pay_amount = pay_amount
        self.person_pay_amount = person_pay_amount
        self.settle_time = settle_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_pay_amount is not None:
            result['corp_pay_amount'] = self.corp_pay_amount

        if self.merchant_name is not None:
            result['merchant_name'] = self.merchant_name

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.order_type is not None:
            result['order_type'] = self.order_type

        if self.pay_amount is not None:
            result['pay_amount'] = self.pay_amount

        if self.person_pay_amount is not None:
            result['person_pay_amount'] = self.person_pay_amount

        if self.settle_time is not None:
            result['settle_time'] = self.settle_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_pay_amount') is not None:
            self.corp_pay_amount = m.get('corp_pay_amount')

        if m.get('merchant_name') is not None:
            self.merchant_name = m.get('merchant_name')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('order_type') is not None:
            self.order_type = m.get('order_type')

        if m.get('pay_amount') is not None:
            self.pay_amount = m.get('pay_amount')

        if m.get('person_pay_amount') is not None:
            self.person_pay_amount = m.get('person_pay_amount')

        if m.get('settle_time') is not None:
            self.settle_time = m.get('settle_time')

        return self

