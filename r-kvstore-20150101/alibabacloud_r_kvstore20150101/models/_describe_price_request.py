# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePriceRequest(DaraModel):
    def __init__(
        self,
        business_info: str = None,
        capacity: int = None,
        charge_type: str = None,
        coupon_no: str = None,
        engine_version: str = None,
        force_upgrade: bool = None,
        instance_class: str = None,
        instance_id: str = None,
        instances: str = None,
        node_type: str = None,
        order_param_out: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        quantity: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secondary_zone_id: str = None,
        security_token: str = None,
        shard_count: int = None,
        zone_id: str = None,
    ):
        # The extended information such as the promotional event ID and business information.
        self.business_info = business_info
        # The storage capacity used to specify the instance type, in MB. This parameter is used only to query Redis Community Edition instances in classic deployment mode. We recommend that you use the **InstanceClass** parameter to specify an exact instance type.
        # > After you specify the **InstanceClass** parameter, you do not need to specify this parameter.
        self.capacity = capacity
        # The billing method. Valid values:
        # * **PostPaid** (default): pay-as-you-go.
        # * **PrePaid**: subscription.
        self.charge_type = charge_type
        # The coupon code. Default value: youhuiquan_promotion_option_id_for_blank, which indicates that no coupon code is used.
        self.coupon_no = coupon_no
        # <props="china">Database engine version of the Redis instance. Valid values: **2.8**, **4.0**, **5.0**, and **6.0**.
        # 
        # <props="intl">Database engine version of the Redis instance. Valid values: **2.8**, **4.0**, and **5.0**.
        # 
        # <props="partner">Database engine version of the Redis instance. Valid values: **2.8**, **4.0**, and **5.0**.
        self.engine_version = engine_version
        # Specifies whether to forcibly change the configuration. Valid values:
        # * **false**: yes.
        # * **true** (default): no.
        self.force_upgrade = force_upgrade
        # The instance type specified by using the **InstanceClass** code. To find the **InstanceClass** code:
        # 1. In the [instance type navigation](https://help.aliyun.com/document_detail/26350.html), select the desired instance type and click the value in the **Architecture** column to open the specification document.
        # 2. In the instance type table of the specification document, find the desired instance type and locate the code in the **InstanceClass** column.
        # 
        # > The following example describes the parameters required for querying the price of a new instance. In addition to other key parameters, specify at least the following parameters:
        # > * Classic Edition instance: specify this parameter.
        # > * Cloud-native Edition standard architecture instance: specify this parameter.
        # > * Cloud-native Edition cluster architecture instance: specify this parameter and the **ShardCount** parameter.
        # > * Cloud-native Edition read/write splitting architecture instance: specify this parameter and the **Instances** parameter.
        # > * Multiple instances of different types, or Tair ESSD-based instances (custom storage type and storage capacity): specify the Instances parameter (this parameter is not required).
        self.instance_class = instance_class
        # The instance ID.
        # > This parameter is required when **OrderType** is set to **UPGRADE** or **RENEW**.
        self.instance_id = instance_id
        # If you want to query the price of cloud-native read/write splitting architecture instances, Tair ESSD-based instances, or multiple instances of different types, specify this parameter. The value is a JSON-formatted string. For more information, see **Additional description of the Instances parameter** below.
        self.instances = instances
        # The node type. Valid values:
        # - **STAND_ALONE**: standalone (single replica).
        # - **MASTER_SLAVE** (default): high availability (dual replicas).
        self.node_type = node_type
        # Specifies whether to return order parameters. Valid values:
        # * **false** (default): does not return order parameters.
        # * **true**: returns order parameters.
        self.order_param_out = order_param_out
        # The order type. Valid values:
        # * **BUY**: new purchase.
        # * **UPGRADE**: configuration change.
        # * **RENEW**: renewal.
        # * **CONVERT**: billing method conversion.
        # 
        # This parameter is required.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration, in months. Valid values: **1** to **9**, **12**, **24**, and **36**.
        self.period = period
        # The number of instances to purchase. Valid values: **1** to **30**. Default value: **1**.
        self.quantity = quantity
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) to query available regions.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The secondary zone ID. You can call [DescribeZones](https://help.aliyun.com/document_detail/473764.html) to query available zones.
        # > The value of this parameter must be different from the value of the ZoneId parameter.
        self.secondary_zone_id = secondary_zone_id
        self.security_token = security_token
        # The number of data shard nodes in a cloud-native cluster instance.
        self.shard_count = shard_count
        # The zone ID. You can call [DescribeZones](https://help.aliyun.com/document_detail/473764.html) to query available zones.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.force_upgrade is not None:
            result['ForceUpgrade'] = self.force_upgrade

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instances is not None:
            result['Instances'] = self.instances

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.order_param_out is not None:
            result['OrderParamOut'] = self.order_param_out

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ForceUpgrade') is not None:
            self.force_upgrade = m.get('ForceUpgrade')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Instances') is not None:
            self.instances = m.get('Instances')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OrderParamOut') is not None:
            self.order_param_out = m.get('OrderParamOut')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

