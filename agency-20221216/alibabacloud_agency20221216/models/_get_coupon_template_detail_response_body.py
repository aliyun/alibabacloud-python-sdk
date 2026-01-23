# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class GetCouponTemplateDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCouponTemplateDetailResponseBodyData = None,
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
            temp_model = main_models.GetCouponTemplateDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCouponTemplateDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        applicable_products: str = None,
        cost_bearer: str = None,
        coupon_description: str = None,
        created_time: str = None,
        denomination: float = None,
        limit_per_person: int = None,
        purchase_type: str = None,
        reason_for_application: str = None,
        status: str = None,
        template_id: int = None,
        template_name: str = None,
        valid_until: str = None,
        valid_until_type: str = None,
    ):
        self.applicable_products = applicable_products
        self.cost_bearer = cost_bearer
        self.coupon_description = coupon_description
        self.created_time = created_time
        self.denomination = denomination
        self.limit_per_person = limit_per_person
        self.purchase_type = purchase_type
        self.reason_for_application = reason_for_application
        self.status = status
        self.template_id = template_id
        self.template_name = template_name
        self.valid_until = valid_until
        self.valid_until_type = valid_until_type

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

        if self.coupon_description is not None:
            result['CouponDescription'] = self.coupon_description

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.denomination is not None:
            result['Denomination'] = self.denomination

        if self.limit_per_person is not None:
            result['LimitPerPerson'] = self.limit_per_person

        if self.purchase_type is not None:
            result['PurchaseType'] = self.purchase_type

        if self.reason_for_application is not None:
            result['ReasonForApplication'] = self.reason_for_application

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.valid_until is not None:
            result['ValidUntil'] = self.valid_until

        if self.valid_until_type is not None:
            result['ValidUntilType'] = self.valid_until_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicableProducts') is not None:
            self.applicable_products = m.get('ApplicableProducts')

        if m.get('CostBearer') is not None:
            self.cost_bearer = m.get('CostBearer')

        if m.get('CouponDescription') is not None:
            self.coupon_description = m.get('CouponDescription')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Denomination') is not None:
            self.denomination = m.get('Denomination')

        if m.get('LimitPerPerson') is not None:
            self.limit_per_person = m.get('LimitPerPerson')

        if m.get('PurchaseType') is not None:
            self.purchase_type = m.get('PurchaseType')

        if m.get('ReasonForApplication') is not None:
            self.reason_for_application = m.get('ReasonForApplication')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('ValidUntil') is not None:
            self.valid_until = m.get('ValidUntil')

        if m.get('ValidUntilType') is not None:
            self.valid_until_type = m.get('ValidUntilType')

        return self

