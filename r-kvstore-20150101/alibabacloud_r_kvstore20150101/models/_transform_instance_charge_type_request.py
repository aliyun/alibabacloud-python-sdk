# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransformInstanceChargeTypeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: str = None,
        auto_renew_period: int = None,
        charge_type: str = None,
        coupon_no: str = None,
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
        # - **true**: Automatic payment. This is the default value.
        # 
        # - **false**: Manual payment. In the console, choose **Billing Management** > **Renewal Management** in the top navigation bar. In the navigation pane on the left, click **Or\\*\\*rs** > **My Or\\*\\*rs** to find and pay for the or\\*er.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # - **true**: Auto-renewal is enabled.
        # 
        # - **false** (default): Auto-renewal is disabled.
        self.auto_renew = auto_renew
        # The auto-renewal period, in months. Valid values: **1**, **2**, **3**, **6**, and **12**.
        # 
        # > This parameter is required when the **AutoRenew** parameter is set to **true**.
        self.auto_renew_period = auto_renew_period
        # The target billing method. Valid values:
        # 
        # - **PrePaid**: subscription. If you set this parameter to this value, you must also specify the **Period** parameter.
        # 
        # - **PostPaid**: pay-as-you-go.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The coupon ID.
        self.coupon_no = coupon_no
        # The instance ID. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/473778.html) operation to query instance IDs.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration, in months. Valid values: **1** to **9**, **12**, **24**, and **36**.
        # 
        # > This parameter is available and required only when the **ChargeType** parameter is set to **PrePaid**.
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

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

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

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

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

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

