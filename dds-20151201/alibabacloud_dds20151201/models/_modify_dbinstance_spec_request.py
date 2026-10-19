# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceSpecRequest(DaraModel):
    def __init__(
        self,
        align_primary_zone: bool = None,
        auto_pay: bool = None,
        business_info: str = None,
        coupon_no: str = None,
        dbinstance_class: str = None,
        dbinstance_id: str = None,
        dbinstance_storage: str = None,
        effective_time: str = None,
        extra_param: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        readonly_replicas: str = None,
        replication_factor: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        search_node_class: str = None,
        search_node_count: int = None,
        search_node_storage: int = None,
        target_hidden_zone_id: str = None,
        target_secondary_zone_id: str = None,
        target_vswitch_id: str = None,
        target_zone_id: str = None,
    ):
        # Specifies whether to automatically align the primary node to the primary zone for a multi-zone instance after operations such as configuration changes. If you choose not to align the node, one primary/secondary switchover (transient disconnection) is avoided. Default value: true (aligned).
        self.align_primary_zone = align_primary_zone
        # Specifies whether to enable automatic payment for the instance. Valid values:
        # - **true**: enables automatic payment. This is the default value. Make sure that your account has sufficient balance.
        # <props="china">- **false**: disables automatic payment. You must manually pay for the order in the console. Log on to the ApsaraDB for MongoDB console. In the upper-right corner of the page, choose **Expenses** > **Expenses and Costs**. In the left-side navigation pane, choose **Orders** > **My Orders**. On the **Orders** tab, find the order and complete the payment.
        # <props="intl">- **false**: disables automatic payment. You must manually pay for the order in the console. Log on to the ApsaraDB for MongoDB console. In the upper-right corner of the page, choose **Expenses** > **Expenses and Costs**. In the left-side navigation pane, click **Order Management**. On the **Orders** page, find the order and complete the payment.
        self.auto_pay = auto_pay
        # The business information.
        self.business_info = business_info
        # Specifies whether to use a coupon. Valid values:
        # - **default** or **null**: uses a coupon. This is the default value.
        # - **youhuiquan_promotion_option_id_for_blank**: does not use a coupon.
        self.coupon_no = coupon_no
        # The instance type. <props="intl"><ph>For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html). You can also call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/149719.html) operation to query instance types.</ph>
        # <props="china">
        # - For standalone instances and replica set instances, this parameter specifies the instance type. For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html). You can also call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/149719.html) operation to query the instance types of standalone instances and replica set instances.
        # - For serverless instances, this parameter specifies the compute specifications of the instance. Valid values: 100 to 8000.
        # 
        # 
        # > You must specify at least one of the **DBInstanceClass** and **DBInstanceStorage** parameters.
        self.dbinstance_class = dbinstance_class
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Instance storage space of the instance. <props="intl"><ph>Valid values: 10 to 3000. Unit: GB. The step size is 10 GB. The valid values are subject to the instance type. For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html).</ph>
        # 
        # <props="china">
        # - For standalone instances and replica set instances, valid values are 10 to 3000. Unit: GB. The step size is 10 GB. The valid values are subject to the instance type. For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        # - For serverless instances, valid values are 1 to 100. Unit: GB. The step size is 1 GB.
        # 
        # 
        # > - You must specify at least one of the **DBInstanceStorage** and **DBInstanceClass** parameters.
        # > - You cannot downgrade instance storage space.
        self.dbinstance_storage = dbinstance_storage
        # The time when the configuration change takes effect. Valid values:
        # - **Immediately**: takes effect immediately. This is the default value.
        # - **MaintainTime**: takes effect during the maintenance window of the instance.
        self.effective_time = effective_time
        # The additional parameter. Valid values:
        # 
        # - **async**: returns the result after the configuration change order is created.
        # - **sync**: returns the result when the configuration change is delivered after the order is created.
        self.extra_param = extra_param
        # The type of configuration change. Valid values:
        # - **UPGRADE**: upgrades the configurations. This is the default value.
        # - **DOWNGRADE**: downgrades the configurations.
        # 
        # > You can specify this parameter only when the instance uses the subscription billing method.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of read-only nodes. Valid values: **0** to **5**.
        # 
        # If the instance is connected only over the **classic network** and a **VPC**, you must enable Internet access or release the classic network before you can change the **number of read-only nodes**.
        # > You can log on to the ApsaraDB for MongoDB console and view the enabled network types on the **Database Connections** page.
        self.readonly_replicas = readonly_replicas
        # The number of nodes in the instance. Default value: 3.
        # - For a replica set instance, valid values are **3**, **5**, and **7**.
        # - For a standalone instance, the value is fixed to **1**.
        # - For a replica set instance that uses shared storage (supported only on the Alibaba Cloud China site), the value is fixed to **2**.
        # 
        # > You do not need to specify this parameter for a serverless instance (supported only on the Alibaba Cloud China site).
        self.replication_factor = replication_factor
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The specifications of the search node for the configuration change.
        self.search_node_class = search_node_class
        # The number of search nodes for the configuration change.
        self.search_node_count = search_node_count
        # The storage capacity of the search node for the configuration change.
        self.search_node_storage = search_node_storage
        # The destination zone for the hidden node when you cloud disk instance across zones and change its configurations at the same time.
        # >Notice: This parameter is supported only for instances that use cloud disks.</notice>
        # >Notice: The value of this parameter cannot be the same as the value of the TargetZoneId or TargetSecondaryZoneId parameter.</notice>
        # 
        # > 
        # > - You must specify this parameter only when you cloud disk instance across zones and change its configurations at the same time.
        # > - This parameter is available only for multi-zone migration.
        # > - The destination zone and the current zone of the instance must be in the same region.
        # > - You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query zone IDs.
        self.target_hidden_zone_id = target_hidden_zone_id
        # The destination zone for the secondary node when you cloud disk instance across zones and change its configurations at the same time.
        # >Notice: This parameter is supported only for instances that use cloud disks.</notice>
        # >Notice: The value of this parameter cannot be the same as the value of the TargetZoneId or TargetHiddenZoneId parameter.</notice>
        # > 
        # > - You must specify this parameter only when you cloud disk instance across zones and change its configurations at the same time.
        # > - This parameter is available only for multi-zone migration.
        # > - The destination zone and the current zone of the instance must be in the same region.
        # > - You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query zone IDs.
        self.target_secondary_zone_id = target_secondary_zone_id
        # The ID of the destination vSwitch when you cloud disk instance across zones and change its configurations at the same time.
        # >Notice: This parameter is supported only for instances that use cloud disks.</notice>
        # > 
        # > - You must specify this parameter only when you cloud disk instance across zones and change its configurations at the same time.
        self.target_vswitch_id = target_vswitch_id
        # The destination zone for instance migration when you migrate the instance across zones and change its configurations at the same time.
        # >Notice: This parameter is supported only for cloud disk instances.</notice>
        # >Notice: The value of this parameter cannot be the same as the value of the TargetSecondaryZoneId or TargetHiddenZoneId parameter.</notice>
        # > - You must specify this parameter only when you migrate the instance across zones and change its configurations at the same time.
        # > - The destination zone and the current zone of the instance must be in the same region.
        # > - You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query zone IDs.
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

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.extra_param is not None:
            result['ExtraParam'] = self.extra_param

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas

        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.search_node_class is not None:
            result['SearchNodeClass'] = self.search_node_class

        if self.search_node_count is not None:
            result['SearchNodeCount'] = self.search_node_count

        if self.search_node_storage is not None:
            result['SearchNodeStorage'] = self.search_node_storage

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

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('ExtraParam') is not None:
            self.extra_param = m.get('ExtraParam')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')

        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SearchNodeClass') is not None:
            self.search_node_class = m.get('SearchNodeClass')

        if m.get('SearchNodeCount') is not None:
            self.search_node_count = m.get('SearchNodeCount')

        if m.get('SearchNodeStorage') is not None:
            self.search_node_storage = m.get('SearchNodeStorage')

        if m.get('TargetHiddenZoneId') is not None:
            self.target_hidden_zone_id = m.get('TargetHiddenZoneId')

        if m.get('TargetSecondaryZoneId') is not None:
            self.target_secondary_zone_id = m.get('TargetSecondaryZoneId')

        if m.get('TargetVswitchId') is not None:
            self.target_vswitch_id = m.get('TargetVswitchId')

        if m.get('TargetZoneId') is not None:
            self.target_zone_id = m.get('TargetZoneId')

        return self

