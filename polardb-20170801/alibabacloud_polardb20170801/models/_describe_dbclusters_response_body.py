# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClustersResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBClustersResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The information about the clusters.
        self.items = items
        # The number of the page to return.
        self.page_number = page_number
        # The number of clusters returned per page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
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
            temp_model = main_models.DescribeDBClustersResponseBodyItems()
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

class DescribeDBClustersResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbcluster: List[main_models.DescribeDBClustersResponseBodyItemsDBCluster] = None,
    ):
        self.dbcluster = dbcluster

    def validate(self):
        if self.dbcluster:
            for v1 in self.dbcluster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBCluster'] = []
        if self.dbcluster is not None:
            for k1 in self.dbcluster:
                result['DBCluster'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbcluster = []
        if m.get('DBCluster') is not None:
            for k1 in m.get('DBCluster'):
                temp_model = main_models.DescribeDBClustersResponseBodyItemsDBCluster()
                self.dbcluster.append(temp_model.from_map(k1))

        return self

class DescribeDBClustersResponseBodyItemsDBCluster(DaraModel):
    def __init__(
        self,
        ai_type: str = None,
        category: str = None,
        cpu_cores: str = None,
        create_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_network_type: str = None,
        dbcluster_status: str = None,
        dbnode_class: str = None,
        dbnode_number: int = None,
        dbnodes: main_models.DescribeDBClustersResponseBodyItemsDBClusterDBNodes = None,
        dbtype: str = None,
        dbversion: str = None,
        deletion_lock: int = None,
        engine: str = None,
        expire_time: str = None,
        expired: str = None,
        hot_standby_cluster: str = None,
        lock_mode: str = None,
        memory_size: str = None,
        pay_type: str = None,
        region_id: str = None,
        remote_memory_size: str = None,
        resource_group_id: str = None,
        search_storage_used: int = None,
        serverless_type: str = None,
        storage_pay_type: str = None,
        storage_space: int = None,
        storage_type: str = None,
        storage_used: int = None,
        strict_consistency: str = None,
        sub_category: str = None,
        tags: main_models.DescribeDBClustersResponseBodyItemsDBClusterTags = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # The type of the AI node. Valid values:
        # 
        # *   SearchNode: search node
        # *   DLNode: AI node
        # 
        # Enumeration values:
        # 
        # *   SearchNode | DLNode: both
        # *   DLNode: AI node
        # *   SearchNode: search node
        self.ai_type = ai_type
        # The edition of the cluster. Valid values:
        # 
        # *   **Normal**: Cluster Edition
        # *   **Basic**: Single Node Edition
        # *   **Archive**: X-Engine Edition
        # *   **NormalMultimaster**: Multi-master Cluster (Database/Table) Edition
        self.category = category
        # The number of CPU cores.
        self.cpu_cores = cpu_cores
        # The time when the cluster was created.
        self.create_time = create_time
        # The description of the cluster.
        self.dbcluster_description = dbcluster_description
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The network type of the cluster.
        self.dbcluster_network_type = dbcluster_network_type
        # The state of the cluster.
        self.dbcluster_status = dbcluster_status
        # The specifications of the node.
        self.dbnode_class = dbnode_class
        # The number of nodes.
        self.dbnode_number = dbnode_number
        # The information about the nodes.
        self.dbnodes = dbnodes
        # The type of the database engine.
        self.dbtype = dbtype
        # The version of the database engine.
        self.dbversion = dbversion
        # Indicates whether the cluster is protected from deletion. Valid values:
        # 
        # *   **0**: The cluster is not protected from deletion.
        # *   **1**: The cluster is protected from deletion.
        # 
        # >  You cannot delete clusters that are protected from deletion.
        self.deletion_lock = deletion_lock
        # The database engine of the cluster.
        self.engine = engine
        # The expiration time of the cluster.
        # 
        # >  A specific value is returned only for subscription (**Prepaid**) clusters. For pay-as-you-go (**Postpaid**) clusters, no value is returned.
        self.expire_time = expire_time
        # Indicates whether the cluster has expired. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  A specific value is returned only for subscription (**Prepaid**) clusters.
        self.expired = expired
        # Indicates whether the hot standby storage cluster feature is enabled. Valid values:
        # 
        # *   ON
        # *   OFF
        self.hot_standby_cluster = hot_standby_cluster
        # The lock state of the cluster. Valid values:
        # 
        # *   **Unlock**: The cluster is unlocked.
        # *   **ManualLock**: The cluster is manually locked.
        # *   **LockByExpiration**: The cluster is locked due to cluster expiration.
        self.lock_mode = lock_mode
        # The memory size for local operations. Unit: MB.
        self.memory_size = memory_size
        # The billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        self.pay_type = pay_type
        # The region ID of the cluster.
        self.region_id = region_id
        # The memory size for distributed operations. Unit: MB.
        self.remote_memory_size = remote_memory_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.search_storage_used = search_storage_used
        # Indicates whether the cluster is a serverless cluster. **AgileServerless** indicates the cluster is a serverless cluster. No value is returned for a common cluster.
        self.serverless_type = serverless_type
        # The storage billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        self.storage_pay_type = storage_pay_type
        # The storage that is billed based on the subscription billing method. Unit: bytes.
        self.storage_space = storage_space
        # The storage type.
        self.storage_type = storage_type
        # The used storage. Unit: bytes.
        self.storage_used = storage_used
        # Indicates whether multi-zone data consistency is enabled for the cluster. Valid values:
        # 
        # *   **ON**: Multi-zone data consistency is enabled. For Standard Edition clusters of Multi-zone Edition, this value is returned.
        # *   **OFF**: Multi-zone data consistency is disabled.
        self.strict_consistency = strict_consistency
        # The specification type of the compute node. Valid values:
        # 
        # *   **Exclusive**: dedicated.
        # *   **General**: general-purpose.
        self.sub_category = sub_category
        # The information about the tags.
        self.tags = tags
        # The virtual private cloud (VPC) ID of the cluster.
        self.vpc_id = vpc_id
        # The vSwitch ID of the cluster.
        self.vswitch_id = vswitch_id
        # The zone ID of the cluster.
        self.zone_id = zone_id

    def validate(self):
        if self.dbnodes:
            self.dbnodes.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_type is not None:
            result['AiType'] = self.ai_type

        if self.category is not None:
            result['Category'] = self.category

        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type

        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_number is not None:
            result['DBNodeNumber'] = self.dbnode_number

        if self.dbnodes is not None:
            result['DBNodes'] = self.dbnodes.to_map()

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.deletion_lock is not None:
            result['DeletionLock'] = self.deletion_lock

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.hot_standby_cluster is not None:
            result['HotStandbyCluster'] = self.hot_standby_cluster

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remote_memory_size is not None:
            result['RemoteMemorySize'] = self.remote_memory_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.search_storage_used is not None:
            result['SearchStorageUsed'] = self.search_storage_used

        if self.serverless_type is not None:
            result['ServerlessType'] = self.serverless_type

        if self.storage_pay_type is not None:
            result['StoragePayType'] = self.storage_pay_type

        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used

        if self.strict_consistency is not None:
            result['StrictConsistency'] = self.strict_consistency

        if self.sub_category is not None:
            result['SubCategory'] = self.sub_category

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiType') is not None:
            self.ai_type = m.get('AiType')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')

        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeNumber') is not None:
            self.dbnode_number = m.get('DBNodeNumber')

        if m.get('DBNodes') is not None:
            temp_model = main_models.DescribeDBClustersResponseBodyItemsDBClusterDBNodes()
            self.dbnodes = temp_model.from_map(m.get('DBNodes'))

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('DeletionLock') is not None:
            self.deletion_lock = m.get('DeletionLock')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('HotStandbyCluster') is not None:
            self.hot_standby_cluster = m.get('HotStandbyCluster')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemoteMemorySize') is not None:
            self.remote_memory_size = m.get('RemoteMemorySize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SearchStorageUsed') is not None:
            self.search_storage_used = m.get('SearchStorageUsed')

        if m.get('ServerlessType') is not None:
            self.serverless_type = m.get('ServerlessType')

        if m.get('StoragePayType') is not None:
            self.storage_pay_type = m.get('StoragePayType')

        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')

        if m.get('StrictConsistency') is not None:
            self.strict_consistency = m.get('StrictConsistency')

        if m.get('SubCategory') is not None:
            self.sub_category = m.get('SubCategory')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDBClustersResponseBodyItemsDBClusterTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBClustersResponseBodyItemsDBClusterTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeDBClustersResponseBodyItemsDBClusterTagsTag] = None,
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
                temp_model = main_models.DescribeDBClustersResponseBodyItemsDBClusterTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDBClustersResponseBodyItemsDBClusterTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

class DescribeDBClustersResponseBodyItemsDBClusterDBNodes(DaraModel):
    def __init__(
        self,
        dbnode: List[main_models.DescribeDBClustersResponseBodyItemsDBClusterDBNodesDBNode] = None,
    ):
        self.dbnode = dbnode

    def validate(self):
        if self.dbnode:
            for v1 in self.dbnode:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBNode'] = []
        if self.dbnode is not None:
            for k1 in self.dbnode:
                result['DBNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbnode = []
        if m.get('DBNode') is not None:
            for k1 in m.get('DBNode'):
                temp_model = main_models.DescribeDBClustersResponseBodyItemsDBClusterDBNodesDBNode()
                self.dbnode.append(temp_model.from_map(k1))

        return self

class DescribeDBClustersResponseBodyItemsDBClusterDBNodesDBNode(DaraModel):
    def __init__(
        self,
        dbnode_class: str = None,
        dbnode_id: str = None,
        dbnode_role: str = None,
        hot_replica_mode: str = None,
        imci_switch: str = None,
        region_id: str = None,
        serverless: str = None,
        zone_id: str = None,
    ):
        # The specifications of the node.
        self.dbnode_class = dbnode_class
        # The ID of the node.
        self.dbnode_id = dbnode_id
        # The role of the node. Valid values:
        # 
        # *   **Writer**: primary node
        # *   **Reader**: read-only node
        # *   **ColumnReader**: column store read-only node
        # *   **AI**: AI node
        self.dbnode_role = dbnode_role
        # Indicates whether the hot standby feature is enabled. Valid values:
        # 
        # *   **ON**
        # *   **OFF**
        self.hot_replica_mode = hot_replica_mode
        # Indicates whether the In-Memory Column Index (IMCI) feature is enabled. Valid values:
        # 
        # *   **ON**
        # *   **OFF**
        self.imci_switch = imci_switch
        # The region ID of the cluster.
        self.region_id = region_id
        # Indicates whether the serverless feature is enabled for the node.
        # 
        # *   **ON** indicates that the serverless feature is enabled.
        # *   No value is returned if the serverless feature is disabled.
        self.serverless = serverless
        # The zone ID of the cluster.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.dbnode_role is not None:
            result['DBNodeRole'] = self.dbnode_role

        if self.hot_replica_mode is not None:
            result['HotReplicaMode'] = self.hot_replica_mode

        if self.imci_switch is not None:
            result['ImciSwitch'] = self.imci_switch

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.serverless is not None:
            result['Serverless'] = self.serverless

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('DBNodeRole') is not None:
            self.dbnode_role = m.get('DBNodeRole')

        if m.get('HotReplicaMode') is not None:
            self.hot_replica_mode = m.get('HotReplicaMode')

        if m.get('ImciSwitch') is not None:
            self.imci_switch = m.get('ImciSwitch')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Serverless') is not None:
            self.serverless = m.get('Serverless')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

