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
        # The language parameter. Default value: none. Valid values:
        # - zh-CN: Chinese.
        # - en-US: English.
        self.accept_language = accept_language
        # The reason for applying for the coupon. The reason can be up to 500 characters in length. Example: Apply for a coupon for Customer XXX.
        self.application_reason = application_reason
        # The ID of the coupon template.
        # 
        # This parameter is required.
        self.coupon_template_id = coupon_template_id
        # Specifies whether to use the POC privilege quota. Valid values:
        # - true: Uses the POC privilege quota. If all submitted accounts are marked as approval-exempt, the current coupon application skips the approval process, and the POC privilege quota in your partner benefit package is deducted.
        # - false: Does not use the POC privilege quota. Regardless of the approval-exempt status of the submitted accounts, your POC coupon benefit quota remains unchanged. In this case, the application follows the standard coupon application approval process.
        self.is_use_benefit = is_use_benefit
        # The list of UIDs. Separate multiple UIDs with commas (,). Example: 111,2222.
        # 
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

