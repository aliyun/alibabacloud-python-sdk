# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewRCInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: str = None,
        auto_use_coupon: bool = None,
        business_info: str = None,
        client_token: str = None,
        commodity_code: str = None,
        instance_id: str = None,
        owner_id: int = None,
        pay_type: str = None,
        period_align: bool = None,
        promotion_code: str = None,
        region_id: str = None,
        resource: str = None,
        resource_owner_account: str = None,
        time_type: str = None,
        used_time: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true**: enables the feature. You must make sure that your account balance is sufficient.
        # *   **false**: disables the feature. An unpaid order is generated.
        # 
        # >  Default value: true. If your account balance is insufficient, you can set AutoPay to false to generate an unpaid order. Then, you can log on to the ApsaraDB RDS console to complete the payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.auto_renew = auto_renew
        # Specifies whether to use a coupon. Default value: false. Valid values:
        # 
        # *   **true**: uses a coupon.
        # *   **false**: does not use a coupon.
        self.auto_use_coupon = auto_use_coupon
        # The additional information about the order.
        self.business_info = business_info
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The commodity code of the instance.
        # 
        # Default value: **rds_customprepaid_public_intl**.
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        # The ID of the RDS Custom instance.
        self.instance_id = instance_id
        self.owner_id = owner_id
        # The billing method of the instance. Set the value to **PrePaid**, which indicates the subscription billing method.
        self.pay_type = pay_type
        # Specifies whether the instance is a subscription instance. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.period_align = period_align
        # The coupon code.
        self.promotion_code = promotion_code
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resources.
        self.resource = resource
        self.resource_owner_account = resource_owner_account
        # The unit of the renewal period specified by the **UsedTime** parameter. Valid values:
        # 
        # *   **1**: year
        # *   **2** (default): month
        # 
        # This parameter is required.
        self.time_type = time_type
        # The subscription duration of the instance. Valid values:
        # 
        # *   If you set the **TimeType** parameter to **1**, the value of the UsedTime parameter ranges from **1 to 5**. Unit: year.
        # *   If you set the **TimeType** parameter to **2**, the value of the UsedTime parameter ranges from **1 to 11**. Unit: month.
        # 
        # This parameter is required.
        self.used_time = used_time

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

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period_align is not None:
            result['PeriodAlign'] = self.period_align

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PeriodAlign') is not None:
            self.period_align = m.get('PeriodAlign')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

