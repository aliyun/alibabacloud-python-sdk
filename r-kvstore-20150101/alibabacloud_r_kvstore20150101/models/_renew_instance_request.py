# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        business_info: str = None,
        capacity: str = None,
        client_token: str = None,
        coupon_no: str = None,
        from_app: str = None,
        instance_class: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # * **true**: enables automatic payment. This is the default value.
        # * **false**: disables automatic payment.
        # 
        # <props="china">If you set this parameter to false, you must log on to the console, choose **Billing** > **Renewal Management** in the top navigation bar, and then choose **Order Management** > **My Orders** in the left-side navigation pane to find and pay for the order.
        # 
        # <props="intl">If you set this parameter to false, you must log on to the console, choose **Billing** > **Renewal Management** in the top navigation bar, and then click **Order Management** in the left-side navigation pane to find and pay for the order.
        # 
        # 
        # 
        # <props="partner">If you set this parameter to false, you must log on to the console, choose **Billing** > **Renewal Management** in the top navigation bar, and then click **Order Management** in the left-side navigation pane to find and pay for the order.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Valid values:
        # * **true**: enables auto-renewal. The instance is renewed for the specified period. For example, if you set the renewal period to 3 months, the instance is automatically renewed for 3 months each time.
        # * **false**: disables auto-renewal. This is the default value.
        self.auto_renew = auto_renew
        # The activity ID and business information.
        self.business_info = business_info
        # **[Deprecated]** You cannot change the storage capacity when you renew an instance. By default, the renewal order is placed based on the current specifications.
        self.capacity = capacity
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token is case-sensitive and can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The source of the request. Default value: **OpenAPI**. You do not need to manually specify this parameter.
        self.from_app = from_app
        # **[Deprecated]** You cannot change the instance type when you renew an instance. By default, the renewal order is placed based on the current specifications.
        self.instance_class = instance_class
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The renewal period. Unit: months. Valid values: **1** to **9**, **12**, **24**, and **36**.
        # >For example, if an instance expires in 3 months and you renew it for 3 months, the instance will expire in 6 months after the renewal.
        # 
        # This parameter is required.
        self.period = period
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

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

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.from_app is not None:
            result['FromApp'] = self.from_app

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

