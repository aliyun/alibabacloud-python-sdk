# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveSingleTaskForCreatingOrderRedeemRequest(DaraModel):
    def __init__(
        self,
        coupon_no: str = None,
        current_expiration_date: int = None,
        domain_name: str = None,
        lang: str = None,
        promotion_no: str = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        self.coupon_no = coupon_no
        # This parameter is required.
        self.current_expiration_date = current_expiration_date
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.promotion_no = promotion_no
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
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.current_expiration_date is not None:
            result['CurrentExpirationDate'] = self.current_expiration_date

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no

        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon

        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('CurrentExpirationDate') is not None:
            self.current_expiration_date = m.get('CurrentExpirationDate')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')

        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')

        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

