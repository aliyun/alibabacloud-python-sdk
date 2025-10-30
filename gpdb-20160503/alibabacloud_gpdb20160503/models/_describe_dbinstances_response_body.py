# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancesResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBInstancesResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The queried instances.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeDBInstancesResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDBInstancesResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbinstance: List[main_models.DescribeDBInstancesResponseBodyItemsDBInstance] = None,
    ):
        self.dbinstance = dbinstance

    def validate(self):
        if self.dbinstance:
            for v1 in self.dbinstance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstance'] = []
        if self.dbinstance is not None:
            for k1 in self.dbinstance:
                result['DBInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance = []
        if m.get('DBInstance') is not None:
            for k1 in m.get('DBInstance'):
                temp_model = main_models.DescribeDBInstancesResponseBodyItemsDBInstance()
                self.dbinstance.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesResponseBodyItemsDBInstance(DaraModel):
    def __init__(
        self,
        connection_mode: str = None,
        create_time: str = None,
        dbinstance_category: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_mode: str = None,
        dbinstance_net_type: str = None,
        dbinstance_status: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        instance_deploy_type: str = None,
        instance_network_type: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        master_node_num: int = None,
        pay_type: str = None,
        prod_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        seg_node_num: str = None,
        serverless_mode: str = None,
        storage_size: str = None,
        storage_type: str = None,
        tags: main_models.DescribeDBInstancesResponseBodyItemsDBInstanceTags = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # An invalid parameter. It is no longer returned when you call this operation.
        # 
        # You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/86910.html) operation to query the access mode of an instance.
        self.connection_mode = connection_mode
        # The time when the instance was created. The time is displayed in UTC.
        self.create_time = create_time
        # The edition of the instance. Valid values:
        # 
        # *   **Basic**: Basic Edition.
        # *   **HighAvailability**: High-availability Edition.
        # *   **Finance**: Enterprise Edition.
        self.dbinstance_category = dbinstance_category
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The resource type of the instance. Valid values:
        # 
        # *   **Serverless**: Serverless mode.
        # *   **StorageElastic**: elastic storage mode.
        # *   **Classic**: reserved storage mode.
        self.dbinstance_mode = dbinstance_mode
        # The type of the network interface card (NIC) that is used by the instance. Valid values:
        # 
        # *   **0**: Internet.
        # *   **1**: internal network.
        # *   **2**: VPC.
        self.dbinstance_net_type = dbinstance_net_type
        # The status of the instance. For more information, see [Instance statuses](https://help.aliyun.com/document_detail/86944.html).
        self.dbinstance_status = dbinstance_status
        # The database engine of the instance.
        self.engine = engine
        # The database engine version of the instance.
        self.engine_version = engine_version
        # The expiration time of the instance. The time is displayed in UTC.
        # 
        # >  The expiration time of a pay-as-you-go instance is `2999-09-08T16:00:00Z`.
        self.expire_time = expire_time
        # The resource type of the instance. Valid values:
        # 
        # *   **cluster**: Serverless mode or elastic storage mode.
        # *   **replicaSet**: reserved storage mode.
        self.instance_deploy_type = instance_deploy_type
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**: classic network.
        # *   **VPC**: VPC.
        self.instance_network_type = instance_network_type
        # The lock mode of the instance. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked due to instance restoration.
        # *   **LockByDiskQuota**: The instance is automatically locked due to exhausted storage.
        # *   **LockReadInstanceByDiskQuota**: The instance is a read-only instance and is automatically locked when the disk space is full.
        self.lock_mode = lock_mode
        # The reason why the instance is locked. Valid values:
        # 
        # *   **0**: The instance is not locked.
        # *   **1**: The instance is manually locked.
        # *   **2**: The instance is automatically locked due to instance expiration.
        # *   **3**: The instance is automatically locked due to instance restoration.
        # *   **4**: The instance is automatically locked due to exhausted storage.
        # 
        # >  If the instance is in reserved storage mode and is not locked, null is returned.
        self.lock_reason = lock_reason
        # The number of coordinator nodes.
        self.master_node_num = master_node_num
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.pay_type = pay_type
        # product type
        self.prod_type = prod_type
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The number of compute nodes.
        self.seg_node_num = seg_node_num
        # The type of the Serverless mode. Valid values:
        # 
        # *   **Manual**: manual scheduling.
        # *   **Auto**: automatic scheduling.
        # 
        # >  This parameter is returned only for instances in Serverless mode.
        self.serverless_mode = serverless_mode
        # The storage capacity of the instance. Unit: GB.
        self.storage_size = storage_size
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_essd**: enhanced SSD (ESSD).
        # *   **cloud_efficiency**: ultra disk.
        self.storage_type = storage_type
        # The tags that are added to the instance.
        self.tags = tags
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID of the instance.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode

        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_deploy_type is not None:
            result['InstanceDeployType'] = self.instance_deploy_type

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.prod_type is not None:
            result['ProdType'] = self.prod_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num

        if self.serverless_mode is not None:
            result['ServerlessMode'] = self.serverless_mode

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')

        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceDeployType') is not None:
            self.instance_deploy_type = m.get('InstanceDeployType')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('ProdType') is not None:
            self.prod_type = m.get('ProdType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')

        if m.get('ServerlessMode') is not None:
            self.serverless_mode = m.get('ServerlessMode')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDBInstancesResponseBodyItemsDBInstanceTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstancesResponseBodyItemsDBInstanceTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag] = None,
    ):
        self.tag = tag

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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
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

