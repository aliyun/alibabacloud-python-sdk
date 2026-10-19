# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewAdditionalBandwidthRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        coupon_no: str = None,
        instance_id: str = None,
        order_time_length: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        source_biz: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # * **true**: Automatic payment is enabled. This is the default value.
        # * **false**: Automatic payment is disabled. You must manually pay for the order. On the top menu bar of the console, choose **Expenses** > **Renewal Management**. In the left-side navigation pane, choose **Order Management** > **My Orders**. Find the order and complete the payment.
        self.auto_pay = auto_pay
        # The coupon code.
        self.coupon_no = coupon_no
        # The instance ID. You can call [DescribeInstances](https://help.aliyun.com/document_detail/473778.html) to query the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The purchase duration. Unit: days. Valid values: **1**, **2**, **3**, **7**, **14**, **30**, **60**, **90**, **180**, **365**, **730**, **1095**, and **1825**.
        # 
        # This parameter is required.
        self.order_time_length = order_time_length
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The request source. This parameter is used only for internal maintenance and does not need to be specified.
        self.source_biz = source_biz

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_time_length is not None:
            result['OrderTimeLength'] = self.order_time_length

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.source_biz is not None:
            result['SourceBiz'] = self.source_biz

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderTimeLength') is not None:
            self.order_time_length = m.get('OrderTimeLength')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SourceBiz') is not None:
            self.source_biz = m.get('SourceBiz')

        return self

