# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransformInstanceChargeTypeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: str = None,
        business_info: str = None,
        charge_type: str = None,
        coupon_no: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        pricing_cycle: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > Default value: **true**.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > Default value: **false**.
        self.auto_renew = auto_renew
        # The business information. This is an additional parameter.
        self.business_info = business_info
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid:** subscription.
        # *   **PostPaid:** pay-as-you-go.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration of the instance. Unit: months. Valid values: **1, 2, 3, 4, 5, 6, 7, 8, 9******, **12**, **24**, and **36**.
        self.period = period
        # 实例付费时长单位
        # 取值说明：
        # - **Month：** 月
        # -  **Year：** 年
        # 
        # 默认值：Month
        self.pricing_cycle = pricing_cycle
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

