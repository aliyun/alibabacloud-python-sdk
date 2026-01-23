# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IssueCouponForCustomerRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        application_reason: str = None,
        coupon_template_id: int = None,
        is_use_benefit: bool = None,
        uidlist: str = None,
    ):
        self.accept_language = accept_language
        self.application_reason = application_reason
        # This parameter is required.
        self.coupon_template_id = coupon_template_id
        self.is_use_benefit = is_use_benefit
        # This parameter is required.
        self.uidlist = uidlist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.application_reason is not None:
            result['ApplicationReason'] = self.application_reason

        if self.coupon_template_id is not None:
            result['CouponTemplateId'] = self.coupon_template_id

        if self.is_use_benefit is not None:
            result['IsUseBenefit'] = self.is_use_benefit

        if self.uidlist is not None:
            result['Uidlist'] = self.uidlist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ApplicationReason') is not None:
            self.application_reason = m.get('ApplicationReason')

        if m.get('CouponTemplateId') is not None:
            self.coupon_template_id = m.get('CouponTemplateId')

        if m.get('IsUseBenefit') is not None:
            self.is_use_benefit = m.get('IsUseBenefit')

        if m.get('Uidlist') is not None:
            self.uidlist = m.get('Uidlist')

        return self

