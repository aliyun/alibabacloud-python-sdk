# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceSpecRequest(DaraModel):
    def __init__(
        self,
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
        # Specifies whether to enable automatic payment for the instance. Valid values:
        # 
        # - **true**: enables automatic payment. Make sure that your account has a sufficient balance. This is the default value.
        # 
        # <props="china">
        # 
        # - **false**: disables automatic payment. You can log on to the ApsaraDB for MongoDB console to pay for the instance. In the upper-right corner of the page, choose **Billing Management** > **Billing Management**. In the left-side navigation pane, choose **Orders** > **My Orders**. On the **Product Orders** tab, find the order and complete the payment.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # - **false**: disables automatic payment. You can log on to the ApsaraDB for MongoDB console to pay for the instance. In the upper-right corner of the page, choose **Billing Management** > **Billing Management**. In the left-side navigation pane, click **Orders**. On the **Product Orders** page, find the order and complete the payment.
        self.auto_pay = auto_pay
        # The business information.
        self.business_info = business_info
        # Specifies whether to use a coupon. Valid values:
        # 
        # - **default** or **null** (default): A coupon is used.
        # 
        # - **youhuiquan_promotion_option_id_for_blank**: No coupon is used.
        self.coupon_no = coupon_no
        # The instance type. <props="intl">For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html). You can also call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/149719.html) operation to query instance types.<props="china">
        # 
        # - For a standalone instance or a replica set instance, this parameter specifies the instance type. For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html). You can also call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/149719.html) operation to query the instance types of standalone and replica set instances.
        # 
        # - For a serverless instance, this parameter specifies the computing capacity of the instance. Valid values: 100 to 8000.
        # 
        # > You must configure one of the **DBInstanceStorage** and DBInstanceClass parameters.
        self.dbinstance_class = dbinstance_class
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The storage capacity of the instance. <props="intl">The value must be an integer that is greater than or equal to 10. The value increases in increments of 10. Unit: GB. The values that can be specified for this parameter are subject to the instance type. For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        # 
        # <props="china">
        # 
        # - The storage capacity of a standalone instance or a replica set instance must be a multiple of 10. The valid values are 10 to 3000. Unit: GB. The values that can be specified for this parameter are subject to the instance type. For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        # 
        # - The storage capacity of a serverless instance must be a multiple of 1. The valid values are 1 to 100. Unit: GB.
        # 
        # 
        # 
        # > - You must configure one of the **DBInstanceClass** and DBInstanceStorage parameters.
        # >
        # > - You cannot decrease the storage capacity of an instance.
        self.dbinstance_storage = dbinstance_storage
        # The effective time of the configuration change. Valid values:
        # 
        # - **Immediately**: The configuration change immediately takes effect. This is the default value.
        # 
        # - **MaintainTime**: The configuration change takes effect during the maintenance window of the instance.
        self.effective_time = effective_time
        # Additional parameters. Valid values:
        # 
        # - **async**: The result is returned after the specification change order is created.
        # 
        # - **sync**: The result is returned after the instance specification change is delivered.
        self.extra_param = extra_param
        # The specification change type. Valid values:
        # 
        # - **UPGRADE**: upgrades the specifications. This is the default value.
        # 
        # - **DOWNGRADE**: downgrades the specifications.
        # 
        # > This parameter is available only for subscription instances.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of read-only nodes. Valid values: **0** to **5**.
        # 
        # If the network type of the instance is set to only **classic network** and **VPC**, you need to enable public access or release the classic network endpoint before you can change the **number of read-only nodes**.
        # 
        # > You can log on to the ApsaraDB for MongoDB console and go to the **Database Connections** page to view the network types that have been enabled.
        self.readonly_replicas = readonly_replicas
        # The number of nodes in the instance. Default value: 3.
        # 
        # - Valid values for replica set instances: **3**, **5**, and **7**.
        # 
        # - The value for standalone instances is fixed at **1**.
        # 
        # - The value for replica set instances with shared storage (available only in the China site) is fixed at **2**.
        # 
        # > This parameter is not required for serverless instances (available only in the China site).
        self.replication_factor = replication_factor
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The specifications of the Search node to be changed.
        self.search_node_class = search_node_class
        # The number of Search nodes to be changed.
        self.search_node_count = search_node_count
        # The capacity of the Search node to be changed.
        self.search_node_storage = search_node_storage
        # The destination zone for the hidden node when you change the specifications and migrate the instance across zones.
        # >Notice: This parameter applies only to cloud disk instances.
        # >Notice: The value of this parameter cannot be the same as the value of the TargetZoneId or TargetSecondaryZoneId parameter.
        # 
        # > - You must specify this parameter only when you change the specifications and migrate the instance across zones.
        # >
        # > - This parameter is available only for multi-zone migration.
        # >
        # > - The destination zone and the current zone must be in the same region.
        # >
        # > - You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query zone IDs.
        self.target_hidden_zone_id = target_hidden_zone_id
        # The destination secondary zone for the secondary node when you change the specifications and migrate the instance across zones.
        # >Notice: This parameter applies only to cloud disk instances.
        # >Notice: The value of this parameter cannot be the same as the value of the TargetZoneId or TargetHiddenZoneId parameter.
        # 
        # > - You must specify this parameter only when you change the specifications and migrate the instance across zones.
        # >
        # > - This parameter is available only for multi-zone migration.
        # >
        # > - The destination zone and the current zone must be in the same region.
        # >
        # > - You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query zone IDs.
        self.target_secondary_zone_id = target_secondary_zone_id
        # The destination vSwitch ID when you change the specifications and migrate the instance across zones.
        # >Notice: This parameter applies only to cloud disk instances.
        # 
        # > - You must specify this parameter only when you change the specifications and migrate the instance across zones.
        self.target_vswitch_id = target_vswitch_id
        # The destination zone to which you want to migrate the instance when you change the specifications and migrate the instance across zones.
        # >Notice: This parameter applies only to cloud disk instances.
        # >Notice: The value of this parameter cannot be the same as the value of the TargetSecondaryZoneId or TargetHiddenZoneId parameter.
        # 
        # > - You must specify this parameter only when you change the specifications and migrate the instance across zones.
        # >
        # > - The destination zone and the current zone must be in the same region.
        # >
        # > - You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query zone IDs.
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

