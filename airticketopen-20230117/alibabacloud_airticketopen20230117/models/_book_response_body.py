# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class BookResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.BookResponseBodyData = None,
        error_code: str = None,
        error_data: main_models.BookResponseBodyErrorData = None,
        error_msg: str = None,
        status: int = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The data returned for a successful request.
        self.data = data
        # The business error code.
        self.error_code = error_code
        # The data returned with the error.
        self.error_data = error_data
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code. The value is always 200 for successful HTTP requests.
        self.status = status
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.error_data:
            self.error_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['error_code'] = self.error_code

        if self.error_data is not None:
            result['error_data'] = self.error_data.to_map()

        if self.error_msg is not None:
            result['error_msg'] = self.error_msg

        if self.status is not None:
            result['status'] = self.status

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('data') is not None:
            temp_model = main_models.BookResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')

        if m.get('error_data') is not None:
            temp_model = main_models.BookResponseBodyErrorData()
            self.error_data = temp_model.from_map(m.get('error_data'))

        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class BookResponseBodyErrorData(DaraModel):
    def __init__(
        self,
        order_list: List[main_models.BookResponseBodyErrorDataOrderList] = None,
    ):
        # The list of order information. If you call the Book operation again with the same parameters after a successful booking, the order number is returned.
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
                temp_model = main_models.BookResponseBodyErrorDataOrderList()
                self.order_list.append(temp_model.from_map(k1))

        return self

class BookResponseBodyErrorDataOrderList(DaraModel):
    def __init__(
        self,
        order_attribute: main_models.BookResponseBodyErrorDataOrderListOrderAttribute = None,
        order_num: int = None,
    ):
        self.order_attribute = order_attribute
        # The order number.
        self.order_num = order_num

    def validate(self):
        if self.order_attribute:
            self.order_attribute.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_attribute is not None:
            result['order_attribute'] = self.order_attribute.to_map()

        if self.order_num is not None:
            result['order_num'] = self.order_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_attribute') is not None:
            temp_model = main_models.BookResponseBodyErrorDataOrderListOrderAttribute()
            self.order_attribute = temp_model.from_map(m.get('order_attribute'))

        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        return self

class BookResponseBodyErrorDataOrderListOrderAttribute(DaraModel):
    def __init__(
        self,
        aba_pay_lock_rate_info: main_models.BookResponseBodyErrorDataOrderListOrderAttributeAbaPayLockRateInfo = None,
    ):
        self.aba_pay_lock_rate_info = aba_pay_lock_rate_info

    def validate(self):
        if self.aba_pay_lock_rate_info:
            self.aba_pay_lock_rate_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aba_pay_lock_rate_info is not None:
            result['aba_pay_lock_rate_info'] = self.aba_pay_lock_rate_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aba_pay_lock_rate_info') is not None:
            temp_model = main_models.BookResponseBodyErrorDataOrderListOrderAttributeAbaPayLockRateInfo()
            self.aba_pay_lock_rate_info = temp_model.from_map(m.get('aba_pay_lock_rate_info'))

        return self

class BookResponseBodyErrorDataOrderListOrderAttributeAbaPayLockRateInfo(DaraModel):
    def __init__(
        self,
        pay_intended_amount: str = None,
        pay_intended_currency_code: str = None,
        quotation_currency_code: str = None,
        to_pay_currency_rate: str = None,
    ):
        self.pay_intended_amount = pay_intended_amount
        self.pay_intended_currency_code = pay_intended_currency_code
        self.quotation_currency_code = quotation_currency_code
        self.to_pay_currency_rate = to_pay_currency_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pay_intended_amount is not None:
            result['pay_intended_amount'] = self.pay_intended_amount

        if self.pay_intended_currency_code is not None:
            result['pay_intended_currency_code'] = self.pay_intended_currency_code

        if self.quotation_currency_code is not None:
            result['quotation_currency_code'] = self.quotation_currency_code

        if self.to_pay_currency_rate is not None:
            result['to_pay_currency_rate'] = self.to_pay_currency_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pay_intended_amount') is not None:
            self.pay_intended_amount = m.get('pay_intended_amount')

        if m.get('pay_intended_currency_code') is not None:
            self.pay_intended_currency_code = m.get('pay_intended_currency_code')

        if m.get('quotation_currency_code') is not None:
            self.quotation_currency_code = m.get('quotation_currency_code')

        if m.get('to_pay_currency_rate') is not None:
            self.to_pay_currency_rate = m.get('to_pay_currency_rate')

        return self

class BookResponseBodyData(DaraModel):
    def __init__(
        self,
        order_list: List[main_models.BookResponseBodyDataOrderList] = None,
    ):
        # The list of order information.
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
                temp_model = main_models.BookResponseBodyDataOrderList()
                self.order_list.append(temp_model.from_map(k1))

        return self

class BookResponseBodyDataOrderList(DaraModel):
    def __init__(
        self,
        order_attribute: main_models.BookResponseBodyDataOrderListOrderAttribute = None,
        order_num: int = None,
    ):
        self.order_attribute = order_attribute
        # The order number.
        self.order_num = order_num

    def validate(self):
        if self.order_attribute:
            self.order_attribute.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_attribute is not None:
            result['order_attribute'] = self.order_attribute.to_map()

        if self.order_num is not None:
            result['order_num'] = self.order_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_attribute') is not None:
            temp_model = main_models.BookResponseBodyDataOrderListOrderAttribute()
            self.order_attribute = temp_model.from_map(m.get('order_attribute'))

        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        return self

class BookResponseBodyDataOrderListOrderAttribute(DaraModel):
    def __init__(
        self,
        aba_pay_lock_rate_info: main_models.BookResponseBodyDataOrderListOrderAttributeAbaPayLockRateInfo = None,
    ):
        self.aba_pay_lock_rate_info = aba_pay_lock_rate_info

    def validate(self):
        if self.aba_pay_lock_rate_info:
            self.aba_pay_lock_rate_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aba_pay_lock_rate_info is not None:
            result['aba_pay_lock_rate_info'] = self.aba_pay_lock_rate_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aba_pay_lock_rate_info') is not None:
            temp_model = main_models.BookResponseBodyDataOrderListOrderAttributeAbaPayLockRateInfo()
            self.aba_pay_lock_rate_info = temp_model.from_map(m.get('aba_pay_lock_rate_info'))

        return self

class BookResponseBodyDataOrderListOrderAttributeAbaPayLockRateInfo(DaraModel):
    def __init__(
        self,
        pay_intended_amount: str = None,
        pay_intended_currency_code: str = None,
        quotation_currency_code: str = None,
        to_pay_currency_rate: str = None,
    ):
        self.pay_intended_amount = pay_intended_amount
        self.pay_intended_currency_code = pay_intended_currency_code
        self.quotation_currency_code = quotation_currency_code
        self.to_pay_currency_rate = to_pay_currency_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pay_intended_amount is not None:
            result['pay_intended_amount'] = self.pay_intended_amount

        if self.pay_intended_currency_code is not None:
            result['pay_intended_currency_code'] = self.pay_intended_currency_code

        if self.quotation_currency_code is not None:
            result['quotation_currency_code'] = self.quotation_currency_code

        if self.to_pay_currency_rate is not None:
            result['to_pay_currency_rate'] = self.to_pay_currency_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pay_intended_amount') is not None:
            self.pay_intended_amount = m.get('pay_intended_amount')

        if m.get('pay_intended_currency_code') is not None:
            self.pay_intended_currency_code = m.get('pay_intended_currency_code')

        if m.get('quotation_currency_code') is not None:
            self.quotation_currency_code = m.get('quotation_currency_code')

        if m.get('to_pay_currency_rate') is not None:
            self.to_pay_currency_rate = m.get('to_pay_currency_rate')

        return self

