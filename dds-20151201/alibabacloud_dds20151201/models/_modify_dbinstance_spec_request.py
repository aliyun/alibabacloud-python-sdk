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
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true** (default): enables automatic payment. Make sure that your Alibaba Cloud account has a sufficient balance.
        # *   **false**: disables automatic payment. You can perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the upper-right corner of the page, choose **Expenses** > **User Center**. In the left-side navigation pane, choose **Order Management** > **Order**. On the **Orders for Services** tab, find the order and pay for the order.
        self.auto_pay = auto_pay
        # The business information.
        self.business_info = business_info
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The instance type. For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html). You can also call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/149719.html) operation to view instance types.
        # 
        # > You must specify at least one of the DBInstanceClass and **DBInstanceStorage** parameters.
        self.dbinstance_class = dbinstance_class
        # The ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The storage capacity of the instance. Valid values: 10 to 3000. The value must be a multiple of 10. Unit: GB. The values that can be specified for this parameter are subject to the instance types. For more information, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        # 
        # > 
        # 
        # *   You must specify at least one of the DBInstanceStorage and **DBInstanceClass** parameters.
        # 
        # *   Storage capacity can be scaled down only for pay-as-you-go replica set instances. The new storage capacity you specify must be greater than the used storage capacity.
        self.dbinstance_storage = dbinstance_storage
        # The time when the changed configurations take effect. Valid values:
        # 
        # *   **Immediately** (default): The configurations immediately take effect.
        # *   **MaintainTime**: The configurations take effect during the maintenance window of the instance.
        self.effective_time = effective_time
        # The additional parameter.
        # 
        # Valid values:
        # 
        # *   async
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   sync
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.extra_param = extra_param
        # The type of the configuration change. Valid values:
        # 
        # *   **UPGRADE**
        # *   **DOWNGRADE** (default)
        # 
        # >  This parameter can be configured only when the billing method of the instance is subscription.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of read-only nodes. Valid values: **0** to **5**.
        # 
        # If your instance has only **Classic Network** and **VPC** endpoints, you must apply for a public endpoint or release the classic network endpoint for the instance before you can change the **Read-only Nodes** value.
        # 
        # > You can go to the **Database Connections** page to view the types of networks that are enabled.
        self.readonly_replicas = readonly_replicas
        # The number of nodes in the instance.
        # 
        # *   Valid values for replica set instances: **3**, **5**, and **7**
        # *   Valid values for standalone instances: **1**
        # 
        # >  This parameter is not required for a serverless instance which is only available on the China site (aliyun.com).
        self.replication_factor = replication_factor
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.search_node_class = search_node_class
        self.search_node_count = search_node_count
        self.search_node_storage = search_node_storage
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

