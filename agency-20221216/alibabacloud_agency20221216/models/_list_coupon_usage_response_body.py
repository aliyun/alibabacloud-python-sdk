# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class ListCouponUsageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListCouponUsageResponseBodyData] = None,
        message: str = None,
        page_info: main_models.ListCouponUsageResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListCouponUsageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListCouponUsageResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCouponUsageResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page = page
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListCouponUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        account: str = None,
        amount: float = None,
        balance: float = None,
        coupon_id: str = None,
        coupon_template_id: int = None,
        eff_date: str = None,
        publish_date: str = None,
        status: str = None,
        uid: int = None,
    ):
        self.account = account
        self.amount = amount
        self.balance = balance
        self.coupon_id = coupon_id
        self.coupon_template_id = coupon_template_id
        self.eff_date = eff_date
        self.publish_date = publish_date
        self.status = status
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.amount is not None:
            result['Amount'] = self.amount

        if self.balance is not None:
            result['Balance'] = self.balance

        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id

        if self.coupon_template_id is not None:
            result['CouponTemplateId'] = self.coupon_template_id

        if self.eff_date is not None:
            result['EffDate'] = self.eff_date

        if self.publish_date is not None:
            result['PublishDate'] = self.publish_date

        if self.status is not None:
            result['Status'] = self.status

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Balance') is not None:
            self.balance = m.get('Balance')

        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')

        if m.get('CouponTemplateId') is not None:
            self.coupon_template_id = m.get('CouponTemplateId')

        if m.get('EffDate') is not None:
            self.eff_date = m.get('EffDate')

        if m.get('PublishDate') is not None:
            self.publish_date = m.get('PublishDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

