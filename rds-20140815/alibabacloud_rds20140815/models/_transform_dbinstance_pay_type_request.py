# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransformDBInstancePayTypeRequest(DaraModel):
    def __init__(
        self,
        auto_renew: str = None,
        auto_use_coupon: bool = None,
        business_info: str = None,
        client_token: str = None,
        dbinstance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        period: str = None,
        promotion_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        used_time: int = None,
    ):
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # * **true**: Enables auto-renewal.
        # * **false**: Disables auto-renewal.
        # 
        # > * This parameter takes effect only when you change the billing method from pay-as-you-go to subscription.
        # > * Any string other than **true** is processed as **false**.
        self.auto_renew = auto_renew
        # Specifies whether to use vouchers to offset fees. Valid values:
        # 
        # - **true**: Uses vouchers.
        # - **false**: Does not use vouchers. This is the default value.
        self.auto_use_coupon = auto_use_coupon
        # The extended business parameters.
        self.business_info = business_info
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Instance ID of the instance. You can call the DescribeDBInstances operation to query instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method to which the instance is changed. Valid values:
        # * **Postpaid**: Pay-as-you-go.
        # * **Prepaid**: Subscription.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The subscription type of the subscription instance. Valid values:
        # * **Year**: Yearly subscription.
        # * **Month**: Monthly subscription.
        # 
        # > This parameter is required if the **PayType** parameter is set to **Prepaid**.
        self.period = period
        # The coupon code.
        self.promotion_code = promotion_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The subscription duration. Valid values:
        # * If the **Period** parameter is set to **Year**, the value of the UsedTime parameter ranges from **1** to **5**.
        # * If the **Period** parameter is set to **Month**, the value of the UsedTime parameter ranges from **1** to **11**.
        # 
        # > This parameter is required if the **PayType** parameter is set to **Prepaid**.
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

