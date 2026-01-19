# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        can_upgrade_versions: List[str] = None,
        charge_type: str = None,
        config_pattern_type: str = None,
        create_time: str = None,
        dbcluster_list: List[main_models.DescribeDBInstanceAttributeResponseBodyDBClusterList] = None,
        dbinstance_id: str = None,
        deploy_scheme: str = None,
        description: str = None,
        engine: str = None,
        engine_minor_version: str = None,
        engine_version: str = None,
        expire_time: str = None,
        gmt_modified: str = None,
        lock_mode: int = None,
        lock_reason: str = None,
        maintain_endtime: str = None,
        maintain_starttime: str = None,
        multi_zone: List[main_models.DescribeDBInstanceAttributeResponseBodyMultiZone] = None,
        object_store_size: int = None,
        region_id: str = None,
        request_id: str = None,
        resource_cpu: int = None,
        resource_group_id: str = None,
        sec_group_conn_valid: str = None,
        serverless: bool = None,
        status: str = None,
        storage_size: int = None,
        sub_domain: str = None,
        tags: List[main_models.DescribeDBInstanceAttributeResponseBodyTags] = None,
        v_switch_id: str = None,
        virtual_cluster_list: List[main_models.DescribeDBInstanceAttributeResponseBodyVirtualClusterList] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The information returned.
        self.can_upgrade_versions = can_upgrade_versions
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.charge_type = charge_type
        self.config_pattern_type = config_pattern_type
        # The time when the instance was created.
        self.create_time = create_time
        # The information about each cluster returned.
        self.dbcluster_list = dbcluster_list
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        self.deploy_scheme = deploy_scheme
        # The description of the instance.
        self.description = description
        # The database engine of the instance.
        self.engine = engine
        # The minor kernel version number of the instance.
        self.engine_minor_version = engine_minor_version
        # The database engine version of the instance.
        self.engine_version = engine_version
        # The time when the instance expires.
        self.expire_time = expire_time
        # The time when the instance was last modified, such as when you restarted the instance or applied for a public endpoint for the instance. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        self.gmt_modified = gmt_modified
        # The lock mode of the instance. Set the value to **lock**, which specifies that the instance is locked when it automatically expires or has an overdue payment.
        self.lock_mode = lock_mode
        # The reason why the instance is locked.
        self.lock_reason = lock_reason
        # The end time of the instance maintenance window.
        self.maintain_endtime = maintain_endtime
        # The start time of the instance maintenance window.
        self.maintain_starttime = maintain_starttime
        self.multi_zone = multi_zone
        # The storage capacity of the instance.
        self.object_store_size = object_store_size
        # The Region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The number of CPU cores of the instance.
        self.resource_cpu = resource_cpu
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        self.sec_group_conn_valid = sec_group_conn_valid
        self.serverless = serverless
        # The state of the instance. Valid values:
        # 
        # *   **CREATING**: The instance is being created.
        # *   **ACTIVATION**: The instance is running.
        # *   **RESOURCE_CHANGING**: The resource configuration of the instance is being changed.
        # *   **ORDER_PREPARING**: The order is being confirmed.
        # *   **READONLY_RESOURCE_CHANGING**: The resource configuration of the instance is being changed and the instance is write-locked.
        # *   **DELETING**: The instance is being deleted.
        self.status = status
        # The cache size.
        self.storage_size = storage_size
        # The subdomain zone ID.
        self.sub_domain = sub_domain
        # The tags that are added to the instances. Each tag is a key-value pair that consists of two parts: TagKey and TagValue. Format: `{"key1":"value1"}`.
        self.tags = tags
        self.v_switch_id = v_switch_id
        self.virtual_cluster_list = virtual_cluster_list
        # The VPC ID.
        self.vpc_id = vpc_id
        # The Zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.dbcluster_list:
            for v1 in self.dbcluster_list:
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
        if self.virtual_cluster_list:
            for v1 in self.virtual_cluster_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_upgrade_versions is not None:
            result['CanUpgradeVersions'] = self.can_upgrade_versions

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.config_pattern_type is not None:
            result['ConfigPatternType'] = self.config_pattern_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['DBClusterList'] = []
        if self.dbcluster_list is not None:
            for k1 in self.dbcluster_list:
                result['DBClusterList'].append(k1.to_map() if k1 else None)

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

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.maintain_endtime is not None:
            result['MaintainEndtime'] = self.maintain_endtime

        if self.maintain_starttime is not None:
            result['MaintainStarttime'] = self.maintain_starttime

        result['MultiZone'] = []
        if self.multi_zone is not None:
            for k1 in self.multi_zone:
                result['MultiZone'].append(k1.to_map() if k1 else None)

        if self.object_store_size is not None:
            result['ObjectStoreSize'] = self.object_store_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_cpu is not None:
            result['ResourceCpu'] = self.resource_cpu

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sec_group_conn_valid is not None:
            result['SecGroupConnValid'] = self.sec_group_conn_valid

        if self.serverless is not None:
            result['Serverless'] = self.serverless

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        result['VirtualClusterList'] = []
        if self.virtual_cluster_list is not None:
            for k1 in self.virtual_cluster_list:
                result['VirtualClusterList'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanUpgradeVersions') is not None:
            self.can_upgrade_versions = m.get('CanUpgradeVersions')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ConfigPatternType') is not None:
            self.config_pattern_type = m.get('ConfigPatternType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.dbcluster_list = []
        if m.get('DBClusterList') is not None:
            for k1 in m.get('DBClusterList'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDBClusterList()
                self.dbcluster_list.append(temp_model.from_map(k1))

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

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MaintainEndtime') is not None:
            self.maintain_endtime = m.get('MaintainEndtime')

        if m.get('MaintainStarttime') is not None:
            self.maintain_starttime = m.get('MaintainStarttime')

        self.multi_zone = []
        if m.get('MultiZone') is not None:
            for k1 in m.get('MultiZone'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyMultiZone()
                self.multi_zone.append(temp_model.from_map(k1))

        if m.get('ObjectStoreSize') is not None:
            self.object_store_size = m.get('ObjectStoreSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceCpu') is not None:
            self.resource_cpu = m.get('ResourceCpu')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecGroupConnValid') is not None:
            self.sec_group_conn_valid = m.get('SecGroupConnValid')

        if m.get('Serverless') is not None:
            self.serverless = m.get('Serverless')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        self.virtual_cluster_list = []
        if m.get('VirtualClusterList') is not None:
            for k1 in m.get('VirtualClusterList'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyVirtualClusterList()
                self.virtual_cluster_list.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstanceAttributeResponseBodyVirtualClusterList(DaraModel):
    def __init__(
        self,
        active_cluster_id: str = None,
        active_cluster_name: str = None,
        created_time: str = None,
        db_cluster_id: str = None,
        db_cluster_name: str = None,
        standby_cluster_id: str = None,
        standby_cluster_name: str = None,
        status: str = None,
    ):
        self.active_cluster_id = active_cluster_id
        self.active_cluster_name = active_cluster_name
        self.created_time = created_time
        self.db_cluster_id = db_cluster_id
        self.db_cluster_name = db_cluster_name
        self.standby_cluster_id = standby_cluster_id
        self.standby_cluster_name = standby_cluster_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_cluster_id is not None:
            result['ActiveClusterId'] = self.active_cluster_id

        if self.active_cluster_name is not None:
            result['ActiveClusterName'] = self.active_cluster_name

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id

        if self.db_cluster_name is not None:
            result['DbClusterName'] = self.db_cluster_name

        if self.standby_cluster_id is not None:
            result['StandbyClusterId'] = self.standby_cluster_id

        if self.standby_cluster_name is not None:
            result['StandbyClusterName'] = self.standby_cluster_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveClusterId') is not None:
            self.active_cluster_id = m.get('ActiveClusterId')

        if m.get('ActiveClusterName') is not None:
            self.active_cluster_name = m.get('ActiveClusterName')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')

        if m.get('DbClusterName') is not None:
            self.db_cluster_name = m.get('DbClusterName')

        if m.get('StandbyClusterId') is not None:
            self.standby_cluster_id = m.get('StandbyClusterId')

        if m.get('StandbyClusterName') is not None:
            self.standby_cluster_name = m.get('StandbyClusterName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDBInstanceAttributeResponseBodyTags(DaraModel):
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

class DescribeDBInstanceAttributeResponseBodyMultiZone(DaraModel):
    def __init__(
        self,
        available_ip_count: int = None,
        cidr: str = None,
        v_switch_ids: List[str] = None,
        zone_id: str = None,
    ):
        self.available_ip_count = available_ip_count
        self.cidr = cidr
        self.v_switch_ids = v_switch_ids
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_ip_count is not None:
            result['AvailableIpCount'] = self.available_ip_count

        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIpCount') is not None:
            self.available_ip_count = m.get('AvailableIpCount')

        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstanceAttributeResponseBodyDBClusterList(DaraModel):
    def __init__(
        self,
        cache_storage_size_gb: str = None,
        cache_storage_type: str = None,
        charge_type: str = None,
        cluster_binding: str = None,
        cluster_node_count: int = None,
        cluster_node_type: str = None,
        cpu_cores: int = None,
        created_time: str = None,
        db_cluster_class: str = None,
        db_cluster_id: str = None,
        db_cluster_name: str = None,
        db_instance_name: str = None,
        memory: int = None,
        modified_time: str = None,
        performance_level: str = None,
        scale_max: float = None,
        scale_min: float = None,
        scaling_rules_enable: bool = None,
        start_time: str = None,
        status: str = None,
        sub_domain: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The cache size. Unit: GB.
        self.cache_storage_size_gb = cache_storage_size_gb
        # The cache type.
        self.cache_storage_type = cache_storage_type
        # The billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.charge_type = charge_type
        self.cluster_binding = cluster_binding
        self.cluster_node_count = cluster_node_count
        self.cluster_node_type = cluster_node_type
        # The number of CPU cores.
        self.cpu_cores = cpu_cores
        # The time when the cluster was created.
        self.created_time = created_time
        # The specifications of the cluster. Valid values:
        # 
        # *   **selectdb.xlarge**: 4 CPU cores and 32 GB of memory.
        # *   **selectdb.2xlarge**: 8 CPU cores and 64 GB of memory.
        # *   **selectdb.4xlarge**: 16 CPU cores and 128 GB of memory.
        # *   **selectdb.8xlarge**: 32 CPU cores and 256 GB of memory.
        # *   **selectdb.16xlarge**: 64 CPU cores and 512 GB of memory.
        # *   **selectdb.24xlarge**: 96 CPU cores and 768 GB of memory.
        # *   **selectdb.32xlarge**: 128 CPU cores and 1,024 GB of memory.
        self.db_cluster_class = db_cluster_class
        # The ID of the cluster.
        self.db_cluster_id = db_cluster_id
        # The name of the cluster.
        self.db_cluster_name = db_cluster_name
        # The instance name.
        self.db_instance_name = db_instance_name
        # The memory size.
        self.memory = memory
        # The modified time.
        self.modified_time = modified_time
        # The performance level.
        self.performance_level = performance_level
        self.scale_max = scale_max
        self.scale_min = scale_min
        self.scaling_rules_enable = scaling_rules_enable
        # The time when the cluster started.
        self.start_time = start_time
        # The state of the cluster. Valid values:
        # 
        # *   **CREATING**: The cluster is being created.
        # *   **ACTIVATION**: The cluster is running.
        # *   **RESOURCE_CHANGING**: The resource configuration of the cluster is being changed.
        # *   **ORDER_PREPARING**: The order is being confirmed.
        # *   **READONLY_RESOURCE_CHANGING**: The resource configuration of the cluster is being changed and the cluster is write-locked.
        # *   **DELETING**: The cluster is being deleted.
        self.status = status
        self.sub_domain = sub_domain
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_storage_size_gb is not None:
            result['CacheStorageSizeGB'] = self.cache_storage_size_gb

        if self.cache_storage_type is not None:
            result['CacheStorageType'] = self.cache_storage_type

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_binding is not None:
            result['ClusterBinding'] = self.cluster_binding

        if self.cluster_node_count is not None:
            result['ClusterNodeCount'] = self.cluster_node_count

        if self.cluster_node_type is not None:
            result['ClusterNodeType'] = self.cluster_node_type

        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.db_cluster_class is not None:
            result['DbClusterClass'] = self.db_cluster_class

        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id

        if self.db_cluster_name is not None:
            result['DbClusterName'] = self.db_cluster_name

        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.scaling_rules_enable is not None:
            result['ScalingRulesEnable'] = self.scaling_rules_enable

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheStorageSizeGB') is not None:
            self.cache_storage_size_gb = m.get('CacheStorageSizeGB')

        if m.get('CacheStorageType') is not None:
            self.cache_storage_type = m.get('CacheStorageType')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterBinding') is not None:
            self.cluster_binding = m.get('ClusterBinding')

        if m.get('ClusterNodeCount') is not None:
            self.cluster_node_count = m.get('ClusterNodeCount')

        if m.get('ClusterNodeType') is not None:
            self.cluster_node_type = m.get('ClusterNodeType')

        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DbClusterClass') is not None:
            self.db_cluster_class = m.get('DbClusterClass')

        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')

        if m.get('DbClusterName') is not None:
            self.db_cluster_name = m.get('DbClusterName')

        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('ScalingRulesEnable') is not None:
            self.scaling_rules_enable = m.get('ScalingRulesEnable')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

