# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class CreateCouponTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateCouponTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateCouponTemplateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateCouponTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        applicable_products: str = None,
        cost_bearer: str = None,
        coupon_template_id: int = None,
        create_time: str = None,
        expireddate: str = None,
        product_type: List[str] = None,
        status: str = None,
        template_name: str = None,
        vailddate: str = None,
        vaildperioddays: str = None,
        valid_until: str = None,
        value: str = None,
    ):
        self.applicable_products = applicable_products
        self.cost_bearer = cost_bearer
        self.coupon_template_id = coupon_template_id
        self.create_time = create_time
        self.expireddate = expireddate
        self.product_type = product_type
        self.status = status
        self.template_name = template_name
        self.vailddate = vailddate
        self.vaildperioddays = vaildperioddays
        self.valid_until = valid_until
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products

        if self.cost_bearer is not None:
            result['CostBearer'] = self.cost_bearer

        if self.coupon_template_id is not None:
            result['CouponTemplateID'] = self.coupon_template_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expireddate is not None:
            result['Expireddate'] = self.expireddate

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.status is not None:
            result['Status'] = self.status

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.vailddate is not None:
            result['Vailddate'] = self.vailddate

        if self.vaildperioddays is not None:
            result['Vaildperioddays'] = self.vaildperioddays

        if self.valid_until is not None:
            result['ValidUntil'] = self.valid_until

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicableProducts') is not None:
            self.applicable_products = m.get('ApplicableProducts')

        if m.get('CostBearer') is not None:
            self.cost_bearer = m.get('CostBearer')

        if m.get('CouponTemplateID') is not None:
            self.coupon_template_id = m.get('CouponTemplateID')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Expireddate') is not None:
            self.expireddate = m.get('Expireddate')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('Vailddate') is not None:
            self.vailddate = m.get('Vailddate')

        if m.get('Vaildperioddays') is not None:
            self.vaildperioddays = m.get('Vaildperioddays')

        if m.get('ValidUntil') is not None:
            self.valid_until = m.get('ValidUntil')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

