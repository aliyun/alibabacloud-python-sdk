# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class MealOrderDetailQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.MealOrderDetailQueryResponseBodyModule = None,
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
            temp_model = main_models.MealOrderDetailQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class MealOrderDetailQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        apply_id: int = None,
        corp_code_order_id: str = None,
        corp_id: str = None,
        corp_pay_amount: int = None,
        corp_refund_amount: int = None,
        meal_reason: str = None,
        merchant_name: str = None,
        order_id: str = None,
        order_status: int = None,
        order_sub_status: int = None,
        order_type: str = None,
        pay_amount: int = None,
        pay_type: int = None,
        person_pay_amount: int = None,
        person_refund_amount: int = None,
        refund_amount: int = None,
        scene_name: str = None,
        settle_time: str = None,
        third_part_apply_id: str = None,
        user_alipay_id: str = None,
        user_id: str = None,
    ):
        self.apply_id = apply_id
        self.corp_code_order_id = corp_code_order_id
        self.corp_id = corp_id
        self.corp_pay_amount = corp_pay_amount
        self.corp_refund_amount = corp_refund_amount
        self.meal_reason = meal_reason
        self.merchant_name = merchant_name
        self.order_id = order_id
        self.order_status = order_status
        self.order_sub_status = order_sub_status
        self.order_type = order_type
        self.pay_amount = pay_amount
        self.pay_type = pay_type
        self.person_pay_amount = person_pay_amount
        self.person_refund_amount = person_refund_amount
        self.refund_amount = refund_amount
        self.scene_name = scene_name
        self.settle_time = settle_time
        self.third_part_apply_id = third_part_apply_id
        self.user_alipay_id = user_alipay_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.corp_code_order_id is not None:
            result['corp_code_order_id'] = self.corp_code_order_id

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.corp_pay_amount is not None:
            result['corp_pay_amount'] = self.corp_pay_amount

        if self.corp_refund_amount is not None:
            result['corp_refund_amount'] = self.corp_refund_amount

        if self.meal_reason is not None:
            result['meal_reason'] = self.meal_reason

        if self.merchant_name is not None:
            result['merchant_name'] = self.merchant_name

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.order_sub_status is not None:
            result['order_sub_status'] = self.order_sub_status

        if self.order_type is not None:
            result['order_type'] = self.order_type

        if self.pay_amount is not None:
            result['pay_amount'] = self.pay_amount

        if self.pay_type is not None:
            result['pay_type'] = self.pay_type

        if self.person_pay_amount is not None:
            result['person_pay_amount'] = self.person_pay_amount

        if self.person_refund_amount is not None:
            result['person_refund_amount'] = self.person_refund_amount

        if self.refund_amount is not None:
            result['refund_amount'] = self.refund_amount

        if self.scene_name is not None:
            result['scene_name'] = self.scene_name

        if self.settle_time is not None:
            result['settle_time'] = self.settle_time

        if self.third_part_apply_id is not None:
            result['third_part_apply_id'] = self.third_part_apply_id

        if self.user_alipay_id is not None:
            result['user_alipay_id'] = self.user_alipay_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('corp_code_order_id') is not None:
            self.corp_code_order_id = m.get('corp_code_order_id')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('corp_pay_amount') is not None:
            self.corp_pay_amount = m.get('corp_pay_amount')

        if m.get('corp_refund_amount') is not None:
            self.corp_refund_amount = m.get('corp_refund_amount')

        if m.get('meal_reason') is not None:
            self.meal_reason = m.get('meal_reason')

        if m.get('merchant_name') is not None:
            self.merchant_name = m.get('merchant_name')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('order_sub_status') is not None:
            self.order_sub_status = m.get('order_sub_status')

        if m.get('order_type') is not None:
            self.order_type = m.get('order_type')

        if m.get('pay_amount') is not None:
            self.pay_amount = m.get('pay_amount')

        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')

        if m.get('person_pay_amount') is not None:
            self.person_pay_amount = m.get('person_pay_amount')

        if m.get('person_refund_amount') is not None:
            self.person_refund_amount = m.get('person_refund_amount')

        if m.get('refund_amount') is not None:
            self.refund_amount = m.get('refund_amount')

        if m.get('scene_name') is not None:
            self.scene_name = m.get('scene_name')

        if m.get('settle_time') is not None:
            self.settle_time = m.get('settle_time')

        if m.get('third_part_apply_id') is not None:
            self.third_part_apply_id = m.get('third_part_apply_id')

        if m.get('user_alipay_id') is not None:
            self.user_alipay_id = m.get('user_alipay_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

