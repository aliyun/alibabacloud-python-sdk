# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveSingleTaskForCreatingOrderRenewRequest(DaraModel):
    def __init__(
        self,
        coupon_no: str = None,
        current_expiration_date: int = None,
        domain_name: str = None,
        lang: str = None,
        permit_premium_renew: bool = None,
        promotion_no: str = None,
        subscription_duration: int = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        # The coupon number.
        self.coupon_no = coupon_no
        # The current expiration date of the domain name. This value is a Unix timestamp in milliseconds, representing the time elapsed since 00:00:00 UTC on January 1, 1970.
        # 
        # This parameter is required.
        self.current_expiration_date = current_expiration_date
        # The domain name to renew.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The language of error messages returned by the API. Valid values:
        # 
        # - **zh**: Chinese.
        # 
        # - **en**: English.
        # 
        # The default value is **en**.
        self.lang = lang
        self.permit_premium_renew = permit_premium_renew
        # The promotion number.
        self.promotion_no = promotion_no
        # The renewal period, in years. The value must be an integer from **1** to **10**.
        # 
        # This parameter is required.
        self.subscription_duration = subscription_duration
        # Specifies whether to use a coupon. Valid values:
        # 
        # - **false**: Do not use a coupon.
        # 
        # - **true**: Use a coupon.
        self.use_coupon = use_coupon
        # Specifies whether to use a promotion. Valid values:
        # 
        # - **false**: Do not use a promotion.
        # 
        # - **true**: Use a promotion.
        self.use_promotion = use_promotion
        # The user\\"s IP address. You can set this parameter to **127.0.0.1**.
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

        if self.permit_premium_renew is not None:
            result['PermitPremiumRenew'] = self.permit_premium_renew

        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no

        if self.subscription_duration is not None:
            result['SubscriptionDuration'] = self.subscription_duration

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

        if m.get('PermitPremiumRenew') is not None:
            self.permit_premium_renew = m.get('PermitPremiumRenew')

        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')

        if m.get('SubscriptionDuration') is not None:
            self.subscription_duration = m.get('SubscriptionDuration')

        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')

        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

