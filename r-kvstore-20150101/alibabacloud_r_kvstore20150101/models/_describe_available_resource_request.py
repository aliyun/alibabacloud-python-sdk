# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAvailableResourceRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        engine: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_scene: str = None,
        node_id: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        product_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        zone_id: str = None,
    ):
        # The display language of the response. Valid values:
        # 
        # *   **zh-CN**: Chinese. This is the default value.
        # *   **en-US**: English.
        self.accept_language = accept_language
        # The database engine of the instance. Valid values:
        # 
        # *   **Redis**
        # *   **Memcache**
        self.engine = engine
        # The billing method. Valid values:
        # 
        # *   **PrePaid** (default): subscription
        # *   **PostPaid**: pay-as-you-go
        self.instance_charge_type = instance_charge_type
        # The ID of the instance.
        # 
        # > This parameter is available and required only if the **OrderType** parameter is set to **UPGRADE** or **DOWNGRADE**.
        self.instance_id = instance_id
        # The edition of the instance. Valid values:
        # 
        # *   **professional**: Standard Edition. This edition supports the standalone, master-replica, read /write splitting, and cluster architectures and provides high scalability.
        self.instance_scene = instance_scene
        # The ID of the data node for which you want to query available resources that can be created. You can call the [DescribeLogicInstanceTopology](https://help.aliyun.com/document_detail/473786.html) operation to query the ID of the data node. Remove the number sign (`#`) and the content that follows the number sign. For example, retain only r-bp10noxlhcoim2\\*\\*\\*\\*-db-0.
        # 
        # > Before you specify this parameter, you must set the **InstanceId** parameter to the ID of an instance that uses the cluster or read/write splitting architecture.
        self.node_id = node_id
        # The order type. Valid values:
        # 
        # *   **BUY** (default): orders that are used to create instances
        # *   **UPGRADE**: orders that are used to upgrade instances
        # *   **DOWNGRADE**: orders that are used to downgrade instances
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The instance type. Default value: Local. Valid values:
        # 
        # *   **Local**: classic Redis Open-Source Edition instance or classic DRAM-based instance
        # *   **Tair_rdb**: cloud-native DRAM-based instance
        # *   **Tair_scm**: persistent memory-optimized instance
        # *   **Tair_essd**: ESSD/SSD-based instance
        # *   **OnECS**: cloud-native Redis Open-Source Edition instance
        # 
        # >  The default value of this parameter is Local. To query disk resources, you must specify the instance type that provides the required disk resources.
        self.product_type = product_type
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs. You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query the IDs of resource groups.
        # 
        # >  You can also query the IDs of resource groups in the Resource Management console. For more information, see [View basic information about a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The zone ID of the instance. You can call the [DescribeZones](https://help.aliyun.com/document_detail/473764.html) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_scene is not None:
            result['InstanceScene'] = self.instance_scene

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceScene') is not None:
            self.instance_scene = m.get('InstanceScene')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

