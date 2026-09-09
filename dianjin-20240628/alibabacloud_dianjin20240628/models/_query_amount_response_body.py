# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class QueryAmountResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryAmountResponseBodyData = None,
        message: str = None,
        retry_able: bool = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.retry_able = retry_able
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.retry_able is not None:
            result['retryAble'] = self.retry_able

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.QueryAmountResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('retryAble') is not None:
            self.retry_able = m.get('retryAble')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class QueryAmountResponseBodyData(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        items: List[main_models.QueryAmountResponseBodyDataItems] = None,
        scope_note: str = None,
        start_date: str = None,
        total: main_models.QueryAmountResponseBodyDataTotal = None,
    ):
        self.end_date = end_date
        self.items = items
        self.scope_note = scope_note
        self.start_date = start_date
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.total:
            self.total.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['endDate'] = self.end_date

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.scope_note is not None:
            result['scopeNote'] = self.scope_note

        if self.start_date is not None:
            result['startDate'] = self.start_date

        if self.total is not None:
            result['total'] = self.total.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.QueryAmountResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('scopeNote') is not None:
            self.scope_note = m.get('scopeNote')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        if m.get('total') is not None:
            temp_model = main_models.QueryAmountResponseBodyDataTotal()
            self.total = temp_model.from_map(m.get('total'))

        return self

class QueryAmountResponseBodyDataTotal(DaraModel):
    def __init__(
        self,
        amount: str = None,
        list_fee: str = None,
        total_amount: str = None,
    ):
        self.amount = amount
        self.list_fee = list_fee
        self.total_amount = total_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.list_fee is not None:
            result['listFee'] = self.list_fee

        if self.total_amount is not None:
            result['totalAmount'] = self.total_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('listFee') is not None:
            self.list_fee = m.get('listFee')

        if m.get('totalAmount') is not None:
            self.total_amount = m.get('totalAmount')

        return self

class QueryAmountResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        amount: str = None,
        amount_ratio: str = None,
        list_fee: str = None,
        price: str = None,
        tier: str = None,
        total_amount: str = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.amount = amount
        self.amount_ratio = amount_ratio
        self.list_fee = list_fee
        self.price = price
        self.tier = tier
        self.total_amount = total_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_uid is not None:
            result['aliyunUid'] = self.aliyun_uid

        if self.amount is not None:
            result['amount'] = self.amount

        if self.amount_ratio is not None:
            result['amountRatio'] = self.amount_ratio

        if self.list_fee is not None:
            result['listFee'] = self.list_fee

        if self.price is not None:
            result['price'] = self.price

        if self.tier is not None:
            result['tier'] = self.tier

        if self.total_amount is not None:
            result['totalAmount'] = self.total_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunUid') is not None:
            self.aliyun_uid = m.get('aliyunUid')

        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('amountRatio') is not None:
            self.amount_ratio = m.get('amountRatio')

        if m.get('listFee') is not None:
            self.list_fee = m.get('listFee')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('tier') is not None:
            self.tier = m.get('tier')

        if m.get('totalAmount') is not None:
            self.total_amount = m.get('totalAmount')

        return self

