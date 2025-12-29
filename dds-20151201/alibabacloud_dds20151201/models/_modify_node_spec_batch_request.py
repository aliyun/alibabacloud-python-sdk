# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNodeSpecBatchRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        business_info: str = None,
        client_token: str = None,
        coupon_no: str = None,
        dbinstance_id: str = None,
        effective_time: str = None,
        nodes_info: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        target_hidden_zone_id: str = None,
        target_secondary_zone_id: str = None,
        target_vswitch_id: str = None,
        target_zone_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true**: enables automatic payment. Make sure that you have sufficient balance within your account.
        # *   **false**: disables automatic payment. You can perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the upper-right corner of the page, click **Expenses** to go to the **Billing Management** console. In the left-side navigation pane, click **Orders**. On the **Orders** page, find the order and complete the payment.
        # 
        # Default value: **true**.
        self.auto_pay = auto_pay
        # The business information.
        self.business_info = business_info
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The ID of the instance whose configurations you want to change.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The time when the changed configurations take effect. Valid values:
        # 
        # *   **Immediately**: The configurations immediately take effect.
        # *   **MaintainTime**: The configurations take effect during the maintenance window of the instance.
        # 
        # > 
        # 
        # *   You can call the [ModifyDBInstanceMaintainTime](https://help.aliyun.com/document_detail/62008.html) operation to modify the maintenance window of an instance.
        # 
        # *   You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/62010.html) operation to view the maintenance window of an instance.
        # 
        # Default value: **Immediately**.
        self.effective_time = effective_time
        # The configuration information of the mongos nodes or shard nodes whose configurations you want to change. For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        # 
        # This parameter is required.
        self.nodes_info = nodes_info
        # The type of configuration changes. Valid values:
        # 
        # *   **UPGRADE**
        # *   **DOWNGRADE**
        # 
        # > This parameter is only applicable to instances whose billing method is subscription.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.target_hidden_zone_id = target_hidden_zone_id
        self.target_secondary_zone_id = target_secondary_zone_id
        self.target_vswitch_id = target_vswitch_id
        self.target_zone_id = target_zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.nodes_info is not None:
            result['NodesInfo'] = self.nodes_info

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.target_hidden_zone_id is not None:
            result['TargetHiddenZoneId'] = self.target_hidden_zone_id

        if self.target_secondary_zone_id is not None:
            result['TargetSecondaryZoneId'] = self.target_secondary_zone_id

        if self.target_vswitch_id is not None:
            result['TargetVswitchId'] = self.target_vswitch_id

        if self.target_zone_id is not None:
            result['TargetZoneId'] = self.target_zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('NodesInfo') is not None:
            self.nodes_info = m.get('NodesInfo')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TargetHiddenZoneId') is not None:
            self.target_hidden_zone_id = m.get('TargetHiddenZoneId')

        if m.get('TargetSecondaryZoneId') is not None:
            self.target_secondary_zone_id = m.get('TargetSecondaryZoneId')

        if m.get('TargetVswitchId') is not None:
            self.target_vswitch_id = m.get('TargetVswitchId')

        if m.get('TargetZoneId') is not None:
            self.target_zone_id = m.get('TargetZoneId')

        return self

