# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class OrderRefundDetailQueryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        module: main_models.OrderRefundDetailQueryResponseBodyModule = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.module = module
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.OrderRefundDetailQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class OrderRefundDetailQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        refund_details: List[main_models.OrderRefundDetailQueryResponseBodyModuleRefundDetails] = None,
        total_amount: int = None,
    ):
        self.order_id = order_id
        self.refund_details = refund_details
        self.total_amount = total_amount

    def validate(self):
        if self.refund_details:
            for v1 in self.refund_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['order_id'] = self.order_id

        result['refund_details'] = []
        if self.refund_details is not None:
            for k1 in self.refund_details:
                result['refund_details'].append(k1.to_map() if k1 else None)

        if self.total_amount is not None:
            result['total_amount'] = self.total_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        self.refund_details = []
        if m.get('refund_details') is not None:
            for k1 in m.get('refund_details'):
                temp_model = main_models.OrderRefundDetailQueryResponseBodyModuleRefundDetails()
                self.refund_details.append(temp_model.from_map(k1))

        if m.get('total_amount') is not None:
            self.total_amount = m.get('total_amount')

        return self

class OrderRefundDetailQueryResponseBodyModuleRefundDetails(DaraModel):
    def __init__(
        self,
        person_pay_channel: str = None,
        person_refund_id: str = None,
        refund_amount: int = None,
        refund_amount_corp: int = None,
        refund_amount_person: int = None,
        supplier_refund_id: str = None,
    ):
        self.person_pay_channel = person_pay_channel
        self.person_refund_id = person_refund_id
        self.refund_amount = refund_amount
        self.refund_amount_corp = refund_amount_corp
        self.refund_amount_person = refund_amount_person
        self.supplier_refund_id = supplier_refund_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.person_pay_channel is not None:
            result['person_pay_channel'] = self.person_pay_channel

        if self.person_refund_id is not None:
            result['person_refund_id'] = self.person_refund_id

        if self.refund_amount is not None:
            result['refund_amount'] = self.refund_amount

        if self.refund_amount_corp is not None:
            result['refund_amount_corp'] = self.refund_amount_corp

        if self.refund_amount_person is not None:
            result['refund_amount_person'] = self.refund_amount_person

        if self.supplier_refund_id is not None:
            result['supplier_refund_id'] = self.supplier_refund_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('person_pay_channel') is not None:
            self.person_pay_channel = m.get('person_pay_channel')

        if m.get('person_refund_id') is not None:
            self.person_refund_id = m.get('person_refund_id')

        if m.get('refund_amount') is not None:
            self.refund_amount = m.get('refund_amount')

        if m.get('refund_amount_corp') is not None:
            self.refund_amount_corp = m.get('refund_amount_corp')

        if m.get('refund_amount_person') is not None:
            self.refund_amount_person = m.get('refund_amount_person')

        if m.get('supplier_refund_id') is not None:
            self.supplier_refund_id = m.get('supplier_refund_id')

        return self

