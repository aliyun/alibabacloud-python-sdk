# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class SaveBatchTaskForCreatingOrderRenewRequest(DaraModel):
    def __init__(
        self,
        coupon_no: str = None,
        lang: str = None,
        order_renew_param: List[main_models.SaveBatchTaskForCreatingOrderRenewRequestOrderRenewParam] = None,
        promotion_no: str = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        self.coupon_no = coupon_no
        self.lang = lang
        # This parameter is required.
        self.order_renew_param = order_renew_param
        self.promotion_no = promotion_no
        self.use_coupon = use_coupon
        self.use_promotion = use_promotion
        self.user_client_ip = user_client_ip

    def validate(self):
        if self.order_renew_param:
            for v1 in self.order_renew_param:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.lang is not None:
            result['Lang'] = self.lang

        result['OrderRenewParam'] = []
        if self.order_renew_param is not None:
            for k1 in self.order_renew_param:
                result['OrderRenewParam'].append(k1.to_map() if k1 else None)

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

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        self.order_renew_param = []
        if m.get('OrderRenewParam') is not None:
            for k1 in m.get('OrderRenewParam'):
                temp_model = main_models.SaveBatchTaskForCreatingOrderRenewRequestOrderRenewParam()
                self.order_renew_param.append(temp_model.from_map(k1))

        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')

        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')

        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

class SaveBatchTaskForCreatingOrderRenewRequestOrderRenewParam(DaraModel):
    def __init__(
        self,
        current_expiration_date: int = None,
        domain_name: str = None,
        subscription_duration: int = None,
    ):
        self.current_expiration_date = current_expiration_date
        self.domain_name = domain_name
        self.subscription_duration = subscription_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_expiration_date is not None:
            result['CurrentExpirationDate'] = self.current_expiration_date

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.subscription_duration is not None:
            result['SubscriptionDuration'] = self.subscription_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentExpirationDate') is not None:
            self.current_expiration_date = m.get('CurrentExpirationDate')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('SubscriptionDuration') is not None:
            self.subscription_duration = m.get('SubscriptionDuration')

        return self

