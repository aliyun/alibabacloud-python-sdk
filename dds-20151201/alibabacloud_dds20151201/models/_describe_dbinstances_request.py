# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancesRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        connection_domain: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_status: str = None,
        dbinstance_type: str = None,
        dbnode_type: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        expired: str = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        replication_factor: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.DescribeDBInstancesRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type
        # The endpoint of the node. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/62010.html) operation to query the endpoint of the node.
        self.connection_domain = connection_domain
        # The instance type. For more information about valid values, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        self.dbinstance_class = dbinstance_class
        # The name of the instance. The name must meet the following requirements:
        # 
        # *   The name must start with a letter.
        # *   It can contain digits, letters, underscores (_), and hyphens (-).
        # *   It must be 2 to 256 characters in length.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The state of the instance. For more information about valid values, see [Instance states](https://help.aliyun.com/document_detail/63870.html).
        self.dbinstance_status = dbinstance_status
        # The architecture of the instance. Valid values:
        # 
        # *   **sharding**: sharded cluster instance
        # *   **replicate**: replica set or standalone instance
        self.dbinstance_type = dbinstance_type
        # The type of the node in the instance. This parameter is used to filter standard or test instance.
        # 
        # 1.  Valid value for a standalone or DBFS instance.
        # 2.  Valid value for a standard instance that comes in the replica set or sharded cluster architecture: standard
        # 3.  Valid value when all instances are displayed: default
        self.dbnode_type = dbnode_type
        # The database engine of the instance. Set the value to **MongoDB**.
        self.engine = engine
        # The database engine version of the instance.
        # 
        # *   **6.0**
        # *   **5.0**
        # *   **4.4**
        # *   **4.2**
        # *   **4.0**
        # *   **3.4**
        self.engine_version = engine_version
        # The time when the instance expires.
        self.expire_time = expire_time
        # Specifies whether the instance has expired. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.expired = expired
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**
        # *   **VPC**
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. The value of this parameter must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the most recent region list.
        self.region_id = region_id
        # The number of nodes in the replica set instance. Valid values:
        # 
        # *   **3**
        # *   **5**
        # *   **7**
        self.replication_factor = replication_factor
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags of the instance.
        self.tag = tag
        # The vSwitch ID of the instance.
        self.v_switch_id = v_switch_id
        # The VPC ID of the instance.
        self.vpc_id = vpc_id
        # The zone ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        if self.dbnode_type is not None:
            result['DBNodeType'] = self.dbnode_type

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

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

        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        if m.get('DBNodeType') is not None:
            self.dbnode_type = m.get('DBNodeType')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDBInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance. Valid values of N: **1** to **20**.
        # 
        # *   The key cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # *   It can be up to 64 characters in length.
        # *   It cannot be an empty string.
        self.key = key
        # The tag value of the instance. Valid values of N: **1** to **20**.
        # 
        # *   The value cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # *   The value can be up to 128 characters in length.
        # *   It can be an empty string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

