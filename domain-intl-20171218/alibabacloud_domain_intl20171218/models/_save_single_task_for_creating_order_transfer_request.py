# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveSingleTaskForCreatingOrderTransferRequest(DaraModel):
    def __init__(
        self,
        authorization_code: str = None,
        coupon_no: str = None,
        domain_name: str = None,
        lang: str = None,
        permit_premium_transfer: bool = None,
        promotion_no: str = None,
        registrant_profile_id: int = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.authorization_code = authorization_code
        self.coupon_no = coupon_no
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.permit_premium_transfer = permit_premium_transfer
        self.promotion_no = promotion_no
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        self.use_coupon = use_coupon
        self.use_promotion = use_promotion
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_code is not None:
            result['AuthorizationCode'] = self.authorization_code

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.permit_premium_transfer is not None:
            result['PermitPremiumTransfer'] = self.permit_premium_transfer

        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no

        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id

        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon

        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationCode') is not None:
            self.authorization_code = m.get('AuthorizationCode')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PermitPremiumTransfer') is not None:
            self.permit_premium_transfer = m.get('PermitPremiumTransfer')

        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')

        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')

        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')

        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

