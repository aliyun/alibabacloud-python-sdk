# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceSpecRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        business_info: str = None,
        client_token: str = None,
        coupon_no: str = None,
        effective_time: str = None,
        force_trans: bool = None,
        force_upgrade: bool = None,
        instance_class: str = None,
        instance_id: str = None,
        major_version: str = None,
        node_type: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        read_only_count: int = None,
        region_id: str = None,
        replica_count: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secondary_zone_id: str = None,
        security_token: str = None,
        shard_count: int = None,
        slave_read_only_count: int = None,
        slave_replica_count: int = None,
        source_biz: str = None,
        storage: int = None,
        storage_type: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # * **true**: Automatic payment is enabled. This is the default value.
        # * **false**: Manual payment is enabled. If this parameter is set to **false**, you must manually renew the instance in the console before the instance expires. For more information, refer to [Manual renewal](https://help.aliyun.com/document_detail/26352.html).
        self.auto_pay = auto_pay
        # The activity ID and business information.
        self.business_info = business_info
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The time when the modification takes effect. Valid values:
        # * **Immediately**: The modification takes effect immediately. This is the default value.
        # * **MaintainTime**: The modification takes effect during the maintenance window of the instance. You can call the [ModifyInstanceMaintainTime](https://help.aliyun.com/document_detail/473775.html) operation to modify the maintenance window.
        self.effective_time = effective_time
        # Specifies whether to enable forced transmission. Valid values:
        # - **false** (default): Before the specification change, the system checks the current minor engine version of the instance. If the minor engine version is too low, an error is reported. You must upgrade the minor engine version and retry.
        # - **true**: The check is skipped, and the system directly executes the specification change.
        self.force_trans = force_trans
        # Specifies whether to forcibly modify the specifications. Valid values:
        # * **false**: No.
        # * **true**: Yes. This is the default value.
        self.force_upgrade = force_upgrade
        # The instance type code after the modification. You can call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/473765.html) operation to query the instance types available for modification in the zone to which the instance belongs.
        # 
        # > For more information about instance types, refer to [Instance type overview](https://help.aliyun.com/document_detail/26350.html).
        self.instance_class = instance_class
        # The instance ID. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/473778.html) operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The major engine version to which you want to upgrade a classic instance. Valid values: **2.8**, **4.0**, and **5.0**.
        # > When you upgrade the major engine version, the **InstanceClass** parameter is required. This indicates that this operation only supports upgrading the major engine version when you update the instance specifications. If you only need to upgrade the major engine version, call the [ModifyInstanceMajorVersion](https://help.aliyun.com/document_detail/473776.html) operation.
        self.major_version = major_version
        # The node type. Valid values:
        # * **MASTER_SLAVE**: high-availability (dual-replica)
        # * **STAND_ALONE**: single-replica
        # * **double**: dual-replica
        # * **single**: single-replica
        # > Select **MASTER_SLAVE** or **STAND_ALONE** for cloud-native instances, and select **double** or **single** for classic instances.
        self.node_type = node_type
        # The modification type. This parameter is required when you modify the specifications of a subscription instance. Valid values:
        # 
        # * **UPGRADE**: Upgrades the configurations. This is the default value.
        # * **DOWNGRADE**: Downgrades the configurations.
        # 
        # > * When you downgrade the configurations of a subscription instance, you must set this parameter to **DOWNGRADE**.
        # > * If the price of the target instance type is higher than that of the current instance type, the configurations are upgraded. Otherwise, the configurations are downgraded. For example, the price of the 8 GB read/write splitting edition (5 read-only nodes) is higher than that of the 16 GB cluster edition. Changing the instance type from the latter to the former is considered an upgrade.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of read-only nodes in the primary zone. This parameter applies only when you create a cloud-native read/write splitting instance.
        # * If the instance uses the standard architecture, valid values are 0 to 9. A value of 0 indicates the shutdown of read/write splitting and an instance switchover to the standard architecture.
        # * If the instance uses the cluster architecture, valid values are 1 to 4, which indicates the number of read-only nodes per shard.
        # > If you create a multi-zone instance, you can use this parameter and the SlaveReadOnlyCount parameter to specify the number of read-only nodes in the primary and secondary zones.
        # > * If the instance uses the standard architecture, the sum of this parameter and SlaveReadOnlyCount cannot be greater than 9.
        # > * If the instance uses the cluster architecture, the sum of this parameter and SlaveReadOnlyCount cannot be greater than 4.
        self.read_only_count = read_only_count
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query the region ID. Use this parameter to specify the region of the instance that you want to modify.
        self.region_id = region_id
        # The number of secondary nodes in the primary zone. This parameter applies only to cloud-native multi-replica cluster instances. You can use this parameter to specify a custom number of secondary nodes. Valid values: 1 to 4.
        # 
        # > If the instance is deployed across multiple zones, you can use this parameter and the SlaveReplicaCount parameter to specify the number of secondary nodes in the primary and secondary zones. The sum of this parameter and the SlaveReplicaCount parameter cannot exceed 4.
        self.replica_count = replica_count
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the secondary zone. This parameter is required when you modify the specifications of a single-zone instance and migrate it to multiple zones. You can call the [DescribeZones](https://help.aliyun.com/document_detail/473764.html) operation to query the zone ID.
        # > The value of this parameter cannot be the same as the value of the ZoneId parameter, and you cannot specify the ID of a multi-zone deployment.
        self.secondary_zone_id = secondary_zone_id
        self.security_token = security_token
        # The number of shards. This parameter applies only to cloud-native cluster instances. You can use this parameter to specify a custom number of shards.
        # 
        # > 
        # > - To change a cloud-native cluster instance to a standard instance, you must explicitly set ShardCount to 1 and specify a standard instance type.
        # > - To change a cloud-native standard instance to a cluster instance, you must explicitly set ShardCount to a value greater than 1 and specify a cluster instance type.
        self.shard_count = shard_count
        # The number of read-only nodes in the secondary zone.
        self.slave_read_only_count = slave_read_only_count
        # The number of secondary nodes in the secondary zone.
        self.slave_replica_count = slave_replica_count
        # The source of the call. This parameter is used only for internal maintenance and does not need to be specified.
        self.source_biz = source_biz
        # The storage capacity of the disk instance. The value range varies based on the instance type. For more information, refer to [Disk instance types](https://help.aliyun.com/document_detail/2527111.html).
        # > This parameter is required only when **InstanceType** is set to **tair_essd** and you create a Tair ESSD instance. When you create a Tair SSD instance, the capacity field is defined as different fixed values based on different instance types, and you do not need to specify this field.
        self.storage = storage
        # The storage type. Valid values: **essd_pl1**, **essd_pl2**, and **essd_pl3**.
        # > This parameter is required only when **InstanceType** is set to **tair_essd** and the instance is a Tair ESSD instance.
        self.storage_type = storage_type

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

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.force_trans is not None:
            result['ForceTrans'] = self.force_trans

        if self.force_upgrade is not None:
            result['ForceUpgrade'] = self.force_upgrade

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.major_version is not None:
            result['MajorVersion'] = self.major_version

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.read_only_count is not None:
            result['ReadOnlyCount'] = self.read_only_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replica_count is not None:
            result['ReplicaCount'] = self.replica_count

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

        if self.slave_read_only_count is not None:
            result['SlaveReadOnlyCount'] = self.slave_read_only_count

        if self.slave_replica_count is not None:
            result['SlaveReplicaCount'] = self.slave_replica_count

        if self.source_biz is not None:
            result['SourceBiz'] = self.source_biz

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

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

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('ForceTrans') is not None:
            self.force_trans = m.get('ForceTrans')

        if m.get('ForceUpgrade') is not None:
            self.force_upgrade = m.get('ForceUpgrade')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReadOnlyCount') is not None:
            self.read_only_count = m.get('ReadOnlyCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicaCount') is not None:
            self.replica_count = m.get('ReplicaCount')

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

        if m.get('SlaveReadOnlyCount') is not None:
            self.slave_read_only_count = m.get('SlaveReadOnlyCount')

        if m.get('SlaveReplicaCount') is not None:
            self.slave_replica_count = m.get('SlaveReplicaCount')

        if m.get('SourceBiz') is not None:
            self.source_biz = m.get('SourceBiz')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

