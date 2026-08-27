# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class GetBillingOverviewResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetBillingOverviewResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetBillingOverviewResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetBillingOverviewResponseBodyData(DaraModel):
    def __init__(
        self,
        currency: str = None,
        groups: List[main_models.GetBillingOverviewResponseBodyDataGroups] = None,
        pretax_amount: str = None,
        tax_amount: str = None,
        total_amount: str = None,
    ):
        self.currency = currency
        self.groups = groups
        self.pretax_amount = pretax_amount
        self.tax_amount = tax_amount
        self.total_amount = total_amount

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['currency'] = self.currency

        result['groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['groups'].append(k1.to_map() if k1 else None)

        if self.pretax_amount is not None:
            result['pretaxAmount'] = self.pretax_amount

        if self.tax_amount is not None:
            result['taxAmount'] = self.tax_amount

        if self.total_amount is not None:
            result['totalAmount'] = self.total_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currency') is not None:
            self.currency = m.get('currency')

        self.groups = []
        if m.get('groups') is not None:
            for k1 in m.get('groups'):
                temp_model = main_models.GetBillingOverviewResponseBodyDataGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('pretaxAmount') is not None:
            self.pretax_amount = m.get('pretaxAmount')

        if m.get('taxAmount') is not None:
            self.tax_amount = m.get('taxAmount')

        if m.get('totalAmount') is not None:
            self.total_amount = m.get('totalAmount')

        return self

class GetBillingOverviewResponseBodyDataGroups(DaraModel):
    def __init__(
        self,
        amount: str = None,
        article_codes: List[str] = None,
        key: str = None,
        name: str = None,
        percentage: str = None,
    ):
        self.amount = amount
        self.article_codes = article_codes
        self.key = key
        self.name = name
        self.percentage = percentage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.article_codes is not None:
            result['articleCodes'] = self.article_codes

        if self.key is not None:
            result['key'] = self.key

        if self.name is not None:
            result['name'] = self.name

        if self.percentage is not None:
            result['percentage'] = self.percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('articleCodes') is not None:
            self.article_codes = m.get('articleCodes')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('percentage') is not None:
            self.percentage = m.get('percentage')

        return self

