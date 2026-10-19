# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstancesRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: str = None,
        business_info: str = None,
        coupon_no: str = None,
        engine_version: str = None,
        instances: str = None,
        owner_account: str = None,
        owner_id: int = None,
        rebuild_instance: bool = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        token: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # * **true**: enables automatic payment. This is the default value.
        # * **false**: disables automatic payment. You must manually pay for the order. In the top navigation bar of the console, choose **Billing** > **Renewal Management**. In the left-side navigation pane, choose **Order Management** > **My Orders**, find the order, and then complete the payment.
        # 
        # > This parameter is available only when the **ChargeType** parameter in the **Instances** array is set to **PrePaid**.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Valid values:
        # * **true**: enables auto-renewal.
        # * **false**: disables auto-renewal. This is the default value.
        # 
        # > This parameter is available only when the **ChargeType** parameter in the **Instances** array is set to **PrePaid**.
        self.auto_renew = auto_renew
        # The extended business information.
        self.business_info = business_info
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The Redis-compatible engine version of the instance. Valid values: **4.0** and **5.0**.
        # > Default value: **5.0**.
        self.engine_version = engine_version
        # The configuration information of the new instances. The value must be in JSON format. For more information, see the supplementary description of the Instances parameter.
        # 
        # This parameter is required.
        self.instances = instances
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to rebuild and restore the source instance from the recycle bin. Valid values:
        # * **true**: yes.
        # * **false**: no. This is the default value.
        # 
        # > This parameter is available only when the **SrcDBInstanceId** parameter is specified in the **Instances** array.
        self.rebuild_instance = rebuild_instance
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token is case-sensitive and can be up to 64 ASCII characters in length.
        self.token = token

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

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instances is not None:
            result['Instances'] = self.instances

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.rebuild_instance is not None:
            result['RebuildInstance'] = self.rebuild_instance

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('Instances') is not None:
            self.instances = m.get('Instances')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RebuildInstance') is not None:
            self.rebuild_instance = m.get('RebuildInstance')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

