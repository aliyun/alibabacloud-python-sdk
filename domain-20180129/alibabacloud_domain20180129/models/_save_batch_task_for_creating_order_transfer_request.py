# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class SaveBatchTaskForCreatingOrderTransferRequest(DaraModel):
    def __init__(
        self,
        coupon_no: str = None,
        lang: str = None,
        order_transfer_param: List[main_models.SaveBatchTaskForCreatingOrderTransferRequestOrderTransferParam] = None,
        promotion_no: str = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        # Coupon number.
        self.coupon_no = coupon_no
        # Language of the error message returned by the API. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        # 
        # Default value is **en**.
        self.lang = lang
        # List of job details.
        # 
        # This parameter is required.
        self.order_transfer_param = order_transfer_param
        # Coupon number.
        self.promotion_no = promotion_no
        # Is a coupon used? Valid values:
        # 
        # - **false**: No.
        # - **true**: Yes.
        self.use_coupon = use_coupon
        # Whether to use a coupon. Valid values:
        # - **false**: Do not use.
        # - **true**: Use.
        self.use_promotion = use_promotion
        # User IP address, which can be set to **127.0.0.1**.
        self.user_client_ip = user_client_ip

    def validate(self):
        if self.order_transfer_param:
            for v1 in self.order_transfer_param:
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

        result['OrderTransferParam'] = []
        if self.order_transfer_param is not None:
            for k1 in self.order_transfer_param:
                result['OrderTransferParam'].append(k1.to_map() if k1 else None)

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

        self.order_transfer_param = []
        if m.get('OrderTransferParam') is not None:
            for k1 in m.get('OrderTransferParam'):
                temp_model = main_models.SaveBatchTaskForCreatingOrderTransferRequestOrderTransferParam()
                self.order_transfer_param.append(temp_model.from_map(k1))

        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')

        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')

        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

class SaveBatchTaskForCreatingOrderTransferRequestOrderTransferParam(DaraModel):
    def __init__(
        self,
        authorization_code: str = None,
        domain_name: str = None,
        permit_premium_transfer: bool = None,
        registrant_profile_id: int = None,
    ):
        # Domain name transfer-in password. If multiple domain names are involved, pass the passwords as a list.
        self.authorization_code = authorization_code
        # Domain name. If multiple domain names are involved, pass them as a list.
        self.domain_name = domain_name
        # Is transfer-in of premium domain names allowed? Valid values:
        # 
        # - **false**: Allowed.
        # - **true**: Not allowed.
        # 
        # Default value: **false**.
        self.permit_premium_transfer = permit_premium_transfer
        # ID of an identity-verified domain name registrant profile. You can obtain this ID by invoking the [QueryRegistrantProfileRealNameVerificationInfo](https://help.aliyun.com/document_detail/69359.htm?spm=a2c4g.11186623.0.0.5096253c12PfdB) API.
        self.registrant_profile_id = registrant_profile_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_code is not None:
            result['AuthorizationCode'] = self.authorization_code

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.permit_premium_transfer is not None:
            result['PermitPremiumTransfer'] = self.permit_premium_transfer

        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationCode') is not None:
            self.authorization_code = m.get('AuthorizationCode')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PermitPremiumTransfer') is not None:
            self.permit_premium_transfer = m.get('PermitPremiumTransfer')

        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')

        return self

