# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNodeSpecBatchRequest(DaraModel):
    def __init__(
        self,
        align_primary_zone: bool = None,
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
        # Specifies whether to automatically align the primary node to the primary zone after operations such as configuration changes for a multi-zone instance. If you choose not to align the node, one primary/secondary switchover (transient connection) is prevented. Default value: true.
        self.align_primary_zone = align_primary_zone
        # Specifies whether to enable automatic payment. Valid values:
        # - **true**: enables automatic payment. Make sure that your account has sufficient balance.
        # <props="china">- **false**: disables automatic payment. You can log on to the ApsaraDB for MongoDB console, choose **Expenses** > **Expenses and Costs** in the upper-right corner, choose **Orders** > **My Orders** in the left-side navigation pane, and then find the target order on the **Orders** tab to complete the payment.
        # <props="intl">- **false**: disables automatic payment. You can log on to the ApsaraDB for MongoDB console, choose **Expenses** > **Expenses and Costs** in the upper-right corner, click **Order Management** in the left-side navigation pane, and then find the target order on the **Orders** page to complete the payment.
        # 
        # Default value: **true**.
        self.auto_pay = auto_pay
        # The business information.
        self.business_info = business_info
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You can use the client to generate the token, but you must ensure that it is unique among different requests. The token can contain a maximum of 64 ASCII characters and cannot contain non-ASCII characters.
        self.client_token = client_token
        # Specifies whether to use a coupon. Valid values:
        # - **default** or **null**: uses a coupon. This is the default value.
        # - **youhuiquan_promotion_option_id_for_blank**: does not use a coupon.
        self.coupon_no = coupon_no
        # The instance ID of the instance whose configurations you want to modify.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The effective period of the configuration change. Valid values:
        # 
        # - **Immediately**: The configuration change takes effect immediately.
        # - **MaintainTime**: The configuration change takes effect during the maintenance window of the instance.
        # 
        # > - You can invoke the [ModifyDBInstanceMaintainTime](https://help.aliyun.com/document_detail/62008.html) operation to modify the maintenance window of the instance.
        # > - You can invoke the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/62010.html) operation to view the maintenance window of the instance.
        # 
        # Default value: **Immediately**.
        self.effective_time = effective_time
        # The specifications of the Mongos or shard nodes to be modified. For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        # 
        # This parameter is required.
        self.nodes_info = nodes_info
        # The type of the configuration change. Valid values:
        # 
        # - **UPGRADE**: upgrades the configurations.
        # - **DOWNGRADE**: downgrades the configurations.
        # 
        # > This parameter is available only when the billing method of the instance is subscription.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query available regions.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The destination zone of the hidden node when you migrate the instance across zones and change its configurations at the same time.
        # >Notice: This parameter is supported only for cloud disk instances.</notice>
        # >Notice: The value of this parameter cannot be the same as the value of the TargetZoneId or TargetSecondaryZoneId parameter.</notice>
        # 
        # > 
        # > - You must specify this parameter only when you migrate the instance across zones and change its configurations at the same time.
        self.target_hidden_zone_id = target_hidden_zone_id
        # The destination zone of the secondary node when you migrate the instance across zones and change its configurations at the same time.
        # >Notice: This parameter is supported only for cloud disk instances.</notice>
        # >Notice: The value of this parameter cannot be the same as the value of the TargetZoneId or TargetHiddenZoneId parameter.</notice>
        # > 
        # > - You must specify this parameter only when you migrate the instance across zones and change its configurations at the same time.
        self.target_secondary_zone_id = target_secondary_zone_id
        # The ID of the destination vSwitch when you migrate the instance across zones and change its configurations at the same time.
        # >Notice: This parameter is supported only for cloud disk instances.</notice>
        # > 
        # > - You must specify this parameter only when you migrate the instance across zones and change its configurations at the same time.
        self.target_vswitch_id = target_vswitch_id
        # The destination zone of the primary node when you migrate the instance across zones and change its configurations at the same time.
        # >Notice: This parameter is supported only for cloud disk instances.</notice>
        # >Notice: The value of this parameter cannot be the same as the value of the TargetSecondaryZoneId or TargetHiddenZoneId parameter.</notice>
        # > 
        # > - You must specify this parameter only when you migrate the instance across zones and change its configurations at the same time.
        self.target_zone_id = target_zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.align_primary_zone is not None:
            result['AlignPrimaryZone'] = self.align_primary_zone

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
        if m.get('AlignPrimaryZone') is not None:
            self.align_primary_zone = m.get('AlignPrimaryZone')

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

