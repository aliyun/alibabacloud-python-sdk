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
        # \\* **true**: Enables automatic payment. This is the default value.
        # \\* **false**: Disables automatic payment. You must go to the console to complete the payment. In the top navigation bar, choose **Expenses** > **Renewal Management**. In the navigation pane on the left, click **Or*er Management** > **My Or*ers**, find the or*er, and then complete the payment.
        # \\> This parameter is valid only when **ChargeType** is set to **PrePaid** in **Instances**.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # \\* **true**: Enables auto-renewal.
        # \\* **false**: Disables auto-renewal. This is the default value.
        # \\> This parameter is valid only when **ChargeType** is set to **PrePaid** in **Instances**.
        self.auto_renew = auto_renew
        # Additional business information.
        self.business_info = business_info
        # The coupon code. The default value is `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The Redis-compatible engine version for the instance. Valid values: **4.0** and **5.0**. The default value is **5.0**.
        self.engine_version = engine_version
        # The configurations of the new instances, specified in JSON format. For more information, see the details of the Instances parameter.
        # 
        # This parameter is required.
        self.instances = instances
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to rebuild an instance from the recycle bin. Valid values:
        # \\* **true**: Rebuilds the instance.
        # \\* **false**: Does not rebuild the instance. This is the default value.
        # \\> This parameter is valid only when **SrcDBInstanceId** is specified in **Instances**.
        self.rebuild_instance = rebuild_instance
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # A client-generated token to ensure request idempotence. The value must be unique across requests, case-sensitive, and up to 64 ASCII characters long.
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

