# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstancesOverviewRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        engine_version: str = None,
        instance_class: str = None,
        instance_ids: str = None,
        instance_status: str = None,
        instance_type: str = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        show_tags: bool = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type
        # The database engine version of the instance. Valid values: **5.0**, **4.4**, **4.2**, **4.0**, and **3.4**.
        self.engine_version = engine_version
        # The instance type. The instance type varies based on the instance architecture. For more information about instance types supported by different instance architectures, see the following references:
        # 
        # *   [Standalone instance types](https://help.aliyun.com/document_detail/311407.html)
        # *   [Replica set instance types](https://help.aliyun.com/document_detail/311410.html)
        # *   [Sharded cluster instance types](https://help.aliyun.com/document_detail/311414.html)
        self.instance_class = instance_class
        # The ID of the instance for which you want to query the overview information.
        # 
        # > 
        # 
        # *   If you do not specify this parameter, the overview information of all instances within this account is queried.
        # 
        # *   Separate the instance IDs with commas (,).
        self.instance_ids = instance_ids
        # The state of the instance. For more information about valid values, see [Instance states](https://help.aliyun.com/document_detail/63870.html).
        self.instance_status = instance_status
        # The architecture of the instance. Valid values:
        # 
        # *   **sharding**: sharded cluster instance
        # *   **replicate**: replica set or standalone instance
        # 
        # > 
        # 
        # *   To query the overview information of a sharded cluster instance, you must set the parameter to **sharding**.
        # 
        # *   If you do not specify this parameter, the overview information of all instances within this account is queried.
        self.instance_type = instance_type
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**: classic network
        # *   **VPC**: Virtual Private Cloud (VPC)
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs. For more information, see [View the basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to display instance tags. Default value: False.
        self.show_tags = show_tags
        # The ID of the vSwitch to which the instance is connected.
        self.v_switch_id = v_switch_id
        # The ID of the VPC in which the instance is deployed.
        self.vpc_id = vpc_id
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.show_tags is not None:
            result['ShowTags'] = self.show_tags

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ShowTags') is not None:
            self.show_tags = m.get('ShowTags')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

