# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDBInstancesResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The list of instance details.
        self.items = items
        # The number of entries to return per page. Valid values:
        # 
        # - **30** (default value)
        # 
        # - **50**
        # 
        # - **100**
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDBInstancesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDBInstancesResponseBodyItems(DaraModel):
    def __init__(
        self,
        category: str = None,
        charge_type: str = None,
        cluster_count: int = None,
        dbinstance_id: str = None,
        deploy_scheme: str = None,
        description: str = None,
        engine: str = None,
        engine_minor_version: str = None,
        engine_version: str = None,
        expire_time: str = None,
        fecluster_list: List[main_models.DescribeDBInstancesResponseBodyItemsFEClusterList] = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        instance_used_type: str = None,
        is_deleted: bool = None,
        lock_mode: int = None,
        lock_reason: str = None,
        maintain_end_time_str: str = None,
        maintain_endtime: str = None,
        maintain_start_time_str: str = None,
        maintain_starttime: str = None,
        multi_zone: List[main_models.DescribeDBInstancesResponseBodyItemsMultiZone] = None,
        object_store_size: int = None,
        parent_instance: str = None,
        region_id: str = None,
        resource_cpu: int = None,
        resource_group_id: str = None,
        resource_memory: int = None,
        scale_max: int = None,
        scale_min: int = None,
        scale_replica: int = None,
        serverless: bool = None,
        status: str = None,
        storage_size: int = None,
        storage_type: str = None,
        tags: List[main_models.DescribeDBInstancesResponseBodyItemsTags] = None,
        tenant_cluster_id: str = None,
        tenant_token: str = None,
        tenant_user_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
        connection_string: str = None,
    ):
        # The instance edition. The default value is basic.
        self.category = category
        # The billing method of the instance. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go
        # 
        # - **Prepaid**: subscription
        self.charge_type = charge_type
        # The total number of clusters.
        self.cluster_count = cluster_count
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The deployment mode of the instance:
        # 
        # - multi_az: zone-redundant storage.
        # 
        # - single_az: locally redundant storage.
        self.deploy_scheme = deploy_scheme
        # The description of the instance.
        self.description = description
        # The database type.
        self.engine = engine
        # The minor engine version of the instance.
        self.engine_minor_version = engine_minor_version
        # The database version.
        self.engine_version = engine_version
        # The expiration time of the cluster.
        # 
        # > This parameter is returned only for **Prepaid** (subscription) clusters. For **Postpaid** (pay-as-you-go) clusters, this parameter is empty.
        self.expire_time = expire_time
        self.fecluster_list = fecluster_list
        # The time when the task was created (GMT).
        self.gmt_created = gmt_created
        # The time when the task was last modified (GMT).
        self.gmt_modified = gmt_modified
        # The instance usage type.
        self.instance_used_type = instance_used_type
        # Indicates whether the instance is deleted. Valid values:
        # 
        # - **true**: The instance is deleted.
        # 
        # - **false**: The instance is not deleted.
        self.is_deleted = is_deleted
        # The lock mode of the instance.
        self.lock_mode = lock_mode
        # The reason why the instance is locked.
        self.lock_reason = lock_reason
        # The timestamp that indicates the end of the maintenance window.
        self.maintain_end_time_str = maintain_end_time_str
        # The end time of the maintenance window for the instance.
        self.maintain_endtime = maintain_endtime
        # The timestamp that indicates the start of the maintenance window.
        self.maintain_start_time_str = maintain_start_time_str
        # The start time of the maintenance window for the instance.
        self.maintain_starttime = maintain_starttime
        # The multi-zone configuration.
        self.multi_zone = multi_zone
        # The instance storage size. Unit: GB.
        self.object_store_size = object_store_size
        # The creation time.
        self.parent_instance = parent_instance
        # The region ID.
        self.region_id = region_id
        # The allocated CPU for the resource.
        self.resource_cpu = resource_cpu
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The memory size.
        self.resource_memory = resource_memory
        # The maximum number of RDS Capacity Units (RCUs) for the instance.
        self.scale_max = scale_max
        # The minimum number of RDS Capacity Units (RCUs) for the instance.
        self.scale_min = scale_min
        # This field is redundant.
        self.scale_replica = scale_replica
        # Indicates whether the instance is a serverless instance.
        self.serverless = serverless
        # The state of the instance. Valid values:
        # 
        # - **CREATING**: The instance is being created.
        # 
        # - **ACTIVATION**: The instance is running.
        # 
        # - **RESOURCE_CHANGING**: The instance is being upgraded or downgraded.
        # 
        # - **ORDER_PREPARING**: The order is being confirmed.
        # 
        # - **READONLY_RESOURCE_CHANGING**: The instance configuration is being changed, and the instance is write-locked.
        # 
        # - **DELETING**: The instance is being deleted.
        self.status = status
        # The storage capacity.
        self.storage_size = storage_size
        # The storage class of the instance.
        self.storage_type = storage_type
        # The list of tags of the instance.
        self.tags = tags
        # The ID of the Prometheus monitoring cluster.
        self.tenant_cluster_id = tenant_cluster_id
        # The token for connecting to Prometheus monitoring.
        self.tenant_token = tenant_token
        # The user account label for Prometheus monitoring.
        self.tenant_user_id = tenant_user_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vswitch_id = vswitch_id
        # The zone ID.
        self.zone_id = zone_id
        # The connection address.
        self.connection_string = connection_string

    def validate(self):
        if self.fecluster_list:
            for v1 in self.fecluster_list:
                 if v1:
                    v1.validate()
        if self.multi_zone:
            for v1 in self.multi_zone:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.deploy_scheme is not None:
            result['DeployScheme'] = self.deploy_scheme

        if self.description is not None:
            result['Description'] = self.description

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_minor_version is not None:
            result['EngineMinorVersion'] = self.engine_minor_version

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        result['FEClusterList'] = []
        if self.fecluster_list is not None:
            for k1 in self.fecluster_list:
                result['FEClusterList'].append(k1.to_map() if k1 else None)

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.instance_used_type is not None:
            result['InstanceUsedType'] = self.instance_used_type

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.maintain_end_time_str is not None:
            result['MaintainEndTimeStr'] = self.maintain_end_time_str

        if self.maintain_endtime is not None:
            result['MaintainEndtime'] = self.maintain_endtime

        if self.maintain_start_time_str is not None:
            result['MaintainStartTimeStr'] = self.maintain_start_time_str

        if self.maintain_starttime is not None:
            result['MaintainStarttime'] = self.maintain_starttime

        result['MultiZone'] = []
        if self.multi_zone is not None:
            for k1 in self.multi_zone:
                result['MultiZone'].append(k1.to_map() if k1 else None)

        if self.object_store_size is not None:
            result['ObjectStoreSize'] = self.object_store_size

        if self.parent_instance is not None:
            result['ParentInstance'] = self.parent_instance

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_cpu is not None:
            result['ResourceCpu'] = self.resource_cpu

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_memory is not None:
            result['ResourceMemory'] = self.resource_memory

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.scale_replica is not None:
            result['ScaleReplica'] = self.scale_replica

        if self.serverless is not None:
            result['Serverless'] = self.serverless

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tenant_cluster_id is not None:
            result['TenantClusterId'] = self.tenant_cluster_id

        if self.tenant_token is not None:
            result['TenantToken'] = self.tenant_token

        if self.tenant_user_id is not None:
            result['TenantUserId'] = self.tenant_user_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.connection_string is not None:
            result['connectionString'] = self.connection_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DeployScheme') is not None:
            self.deploy_scheme = m.get('DeployScheme')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineMinorVersion') is not None:
            self.engine_minor_version = m.get('EngineMinorVersion')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        self.fecluster_list = []
        if m.get('FEClusterList') is not None:
            for k1 in m.get('FEClusterList'):
                temp_model = main_models.DescribeDBInstancesResponseBodyItemsFEClusterList()
                self.fecluster_list.append(temp_model.from_map(k1))

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('InstanceUsedType') is not None:
            self.instance_used_type = m.get('InstanceUsedType')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MaintainEndTimeStr') is not None:
            self.maintain_end_time_str = m.get('MaintainEndTimeStr')

        if m.get('MaintainEndtime') is not None:
            self.maintain_endtime = m.get('MaintainEndtime')

        if m.get('MaintainStartTimeStr') is not None:
            self.maintain_start_time_str = m.get('MaintainStartTimeStr')

        if m.get('MaintainStarttime') is not None:
            self.maintain_starttime = m.get('MaintainStarttime')

        self.multi_zone = []
        if m.get('MultiZone') is not None:
            for k1 in m.get('MultiZone'):
                temp_model = main_models.DescribeDBInstancesResponseBodyItemsMultiZone()
                self.multi_zone.append(temp_model.from_map(k1))

        if m.get('ObjectStoreSize') is not None:
            self.object_store_size = m.get('ObjectStoreSize')

        if m.get('ParentInstance') is not None:
            self.parent_instance = m.get('ParentInstance')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceCpu') is not None:
            self.resource_cpu = m.get('ResourceCpu')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceMemory') is not None:
            self.resource_memory = m.get('ResourceMemory')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('ScaleReplica') is not None:
            self.scale_replica = m.get('ScaleReplica')

        if m.get('Serverless') is not None:
            self.serverless = m.get('Serverless')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeDBInstancesResponseBodyItemsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TenantClusterId') is not None:
            self.tenant_cluster_id = m.get('TenantClusterId')

        if m.get('TenantToken') is not None:
            self.tenant_token = m.get('TenantToken')

        if m.get('TenantUserId') is not None:
            self.tenant_user_id = m.get('TenantUserId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('connectionString') is not None:
            self.connection_string = m.get('connectionString')

        return self

class DescribeDBInstancesResponseBodyItemsTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeDBInstancesResponseBodyItemsMultiZone(DaraModel):
    def __init__(
        self,
        v_switch_ids: List[str] = None,
        zone_id: str = None,
    ):
        # The list of vSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstancesResponseBodyItemsFEClusterList(DaraModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        node_count: int = None,
        single_node_cpu_cores: int = None,
        single_node_memory_in_gb: int = None,
        status: str = None,
    ):
        self.db_cluster_id = db_cluster_id
        self.node_count = node_count
        self.single_node_cpu_cores = single_node_cpu_cores
        self.single_node_memory_in_gb = single_node_memory_in_gb
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.single_node_cpu_cores is not None:
            result['SingleNodeCpuCores'] = self.single_node_cpu_cores

        if self.single_node_memory_in_gb is not None:
            result['SingleNodeMemoryInGB'] = self.single_node_memory_in_gb

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('SingleNodeCpuCores') is not None:
            self.single_node_cpu_cores = m.get('SingleNodeCpuCores')

        if m.get('SingleNodeMemoryInGB') is not None:
            self.single_node_memory_in_gb = m.get('SingleNodeMemoryInGB')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

