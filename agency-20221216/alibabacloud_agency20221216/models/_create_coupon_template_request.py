# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateCouponTemplateRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        applicable_products: str = None,
        cost_bearer: str = None,
        coupon_description: str = None,
        expireddate: str = None,
        limit_per_person: str = None,
        product_type: List[str] = None,
        purchase_type: str = None,
        reason_for_application: str = None,
        template_name: str = None,
        vailddate: str = None,
        vaildperioddays: str = None,
        valid_until: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.accept_language = accept_language
        # This parameter is required.
        self.applicable_products = applicable_products
        # This parameter is required.
        self.cost_bearer = cost_bearer
        self.coupon_description = coupon_description
        self.expireddate = expireddate
        # This parameter is required.
        self.limit_per_person = limit_per_person
        self.product_type = product_type
        self.purchase_type = purchase_type
        # This parameter is required.
        self.reason_for_application = reason_for_application
        # This parameter is required.
        self.template_name = template_name
        self.vailddate = vailddate
        self.vaildperioddays = vaildperioddays
        # This parameter is required.
        self.valid_until = valid_until
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products

        if self.cost_bearer is not None:
            result['CostBearer'] = self.cost_bearer

        if self.coupon_description is not None:
            result['CouponDescription'] = self.coupon_description

        if self.expireddate is not None:
            result['Expireddate'] = self.expireddate

        if self.limit_per_person is not None:
            result['LimitPerPerson'] = self.limit_per_person

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.purchase_type is not None:
            result['PurchaseType'] = self.purchase_type

        if self.reason_for_application is not None:
            result['ReasonForApplication'] = self.reason_for_application

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
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ApplicableProducts') is not None:
            self.applicable_products = m.get('ApplicableProducts')

        if m.get('CostBearer') is not None:
            self.cost_bearer = m.get('CostBearer')

        if m.get('CouponDescription') is not None:
            self.coupon_description = m.get('CouponDescription')

        if m.get('Expireddate') is not None:
            self.expireddate = m.get('Expireddate')

        if m.get('LimitPerPerson') is not None:
            self.limit_per_person = m.get('LimitPerPerson')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('PurchaseType') is not None:
            self.purchase_type = m.get('PurchaseType')

        if m.get('ReasonForApplication') is not None:
            self.reason_for_application = m.get('ReasonForApplication')

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

