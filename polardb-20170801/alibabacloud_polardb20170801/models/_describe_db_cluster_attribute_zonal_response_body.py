# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDbClusterAttributeZonalResponseBody(DaraModel):
    def __init__(
        self,
        ai_creating_time: str = None,
        ai_type: str = None,
        architecture: str = None,
        auto_upgrade_minor_version: str = None,
        blktag_total: int = None,
        blktag_used: int = None,
        bursting_enabled: str = None,
        category: str = None,
        compress_storage_mode: str = None,
        compress_storage_used: int = None,
        creation_time: str = None,
        dbcluster_class: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_network_type: str = None,
        dbcluster_status: str = None,
        dbnodes: List[main_models.DescribeDbClusterAttributeZonalResponseBodyDBNodes] = None,
        dbtype: str = None,
        dbversion: str = None,
        dbversion_status: str = None,
        data_level_1backup_chain_size: int = None,
        data_sync_mode: str = None,
        deletion_lock: int = None,
        engine: str = None,
        expire_time: str = None,
        expired: str = None,
        has_complete_standby_res: bool = None,
        hot_standby_cluster: str = None,
        imci_auto_index: str = None,
        imperceptible_switch: str = None,
        inode_total: int = None,
        inode_used: int = None,
        is_latest_version: bool = None,
        is_proxy_latest_version: bool = None,
        lock_mode: str = None,
        maintain_time: str = None,
        orca: str = None,
        pay_type: str = None,
        provisioned_iops: str = None,
        proxy_cpu_cores: str = None,
        proxy_serverless_type: str = None,
        proxy_standard_cpu_cores: str = None,
        proxy_status: str = None,
        proxy_type: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        restore_data_point: str = None,
        restore_type: str = None,
        row_compression: str = None,
        sqlsize: int = None,
        serverless_type: str = None,
        source_dbcluster: str = None,
        source_region_id: str = None,
        standby_hamode: str = None,
        storage_max: int = None,
        storage_pay_type: str = None,
        storage_space: int = None,
        storage_type: str = None,
        storage_used: int = None,
        strict_consistency: str = None,
        sub_category: str = None,
        support_instant_switch_with_imci: str = None,
        tags: List[main_models.DescribeDbClusterAttributeZonalResponseBodyTags] = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_ids: str = None,
    ):
        self.ai_creating_time = ai_creating_time
        self.ai_type = ai_type
        self.architecture = architecture
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        self.blktag_total = blktag_total
        self.blktag_used = blktag_used
        self.bursting_enabled = bursting_enabled
        self.category = category
        self.compress_storage_mode = compress_storage_mode
        self.compress_storage_used = compress_storage_used
        self.creation_time = creation_time
        self.dbcluster_class = dbcluster_class
        self.dbcluster_description = dbcluster_description
        self.dbcluster_id = dbcluster_id
        self.dbcluster_network_type = dbcluster_network_type
        self.dbcluster_status = dbcluster_status
        self.dbnodes = dbnodes
        self.dbtype = dbtype
        self.dbversion = dbversion
        self.dbversion_status = dbversion_status
        self.data_level_1backup_chain_size = data_level_1backup_chain_size
        self.data_sync_mode = data_sync_mode
        self.deletion_lock = deletion_lock
        self.engine = engine
        self.expire_time = expire_time
        self.expired = expired
        self.has_complete_standby_res = has_complete_standby_res
        self.hot_standby_cluster = hot_standby_cluster
        self.imci_auto_index = imci_auto_index
        self.imperceptible_switch = imperceptible_switch
        self.inode_total = inode_total
        self.inode_used = inode_used
        self.is_latest_version = is_latest_version
        self.is_proxy_latest_version = is_proxy_latest_version
        self.lock_mode = lock_mode
        self.maintain_time = maintain_time
        self.orca = orca
        self.pay_type = pay_type
        self.provisioned_iops = provisioned_iops
        self.proxy_cpu_cores = proxy_cpu_cores
        self.proxy_serverless_type = proxy_serverless_type
        self.proxy_standard_cpu_cores = proxy_standard_cpu_cores
        self.proxy_status = proxy_status
        self.proxy_type = proxy_type
        self.region_id = region_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.restore_data_point = restore_data_point
        self.restore_type = restore_type
        # RowCompression
        self.row_compression = row_compression
        self.sqlsize = sqlsize
        self.serverless_type = serverless_type
        self.source_dbcluster = source_dbcluster
        self.source_region_id = source_region_id
        self.standby_hamode = standby_hamode
        self.storage_max = storage_max
        self.storage_pay_type = storage_pay_type
        self.storage_space = storage_space
        self.storage_type = storage_type
        self.storage_used = storage_used
        self.strict_consistency = strict_consistency
        self.sub_category = sub_category
        self.support_instant_switch_with_imci = support_instant_switch_with_imci
        self.tags = tags
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_ids = zone_ids

    def validate(self):
        if self.dbnodes:
            for v1 in self.dbnodes:
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
        if self.ai_creating_time is not None:
            result['AiCreatingTime'] = self.ai_creating_time

        if self.ai_type is not None:
            result['AiType'] = self.ai_type

        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.auto_upgrade_minor_version is not None:
            result['AutoUpgradeMinorVersion'] = self.auto_upgrade_minor_version

        if self.blktag_total is not None:
            result['BlktagTotal'] = self.blktag_total

        if self.blktag_used is not None:
            result['BlktagUsed'] = self.blktag_used

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.category is not None:
            result['Category'] = self.category

        if self.compress_storage_mode is not None:
            result['CompressStorageMode'] = self.compress_storage_mode

        if self.compress_storage_used is not None:
            result['CompressStorageUsed'] = self.compress_storage_used

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type

        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status

        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k1 in self.dbnodes:
                result['DBNodes'].append(k1.to_map() if k1 else None)

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.dbversion_status is not None:
            result['DBVersionStatus'] = self.dbversion_status

        if self.data_level_1backup_chain_size is not None:
            result['DataLevel1BackupChainSize'] = self.data_level_1backup_chain_size

        if self.data_sync_mode is not None:
            result['DataSyncMode'] = self.data_sync_mode

        if self.deletion_lock is not None:
            result['DeletionLock'] = self.deletion_lock

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.has_complete_standby_res is not None:
            result['HasCompleteStandbyRes'] = self.has_complete_standby_res

        if self.hot_standby_cluster is not None:
            result['HotStandbyCluster'] = self.hot_standby_cluster

        if self.imci_auto_index is not None:
            result['ImciAutoIndex'] = self.imci_auto_index

        if self.imperceptible_switch is not None:
            result['ImperceptibleSwitch'] = self.imperceptible_switch

        if self.inode_total is not None:
            result['InodeTotal'] = self.inode_total

        if self.inode_used is not None:
            result['InodeUsed'] = self.inode_used

        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version

        if self.is_proxy_latest_version is not None:
            result['IsProxyLatestVersion'] = self.is_proxy_latest_version

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time

        if self.orca is not None:
            result['Orca'] = self.orca

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.proxy_cpu_cores is not None:
            result['ProxyCpuCores'] = self.proxy_cpu_cores

        if self.proxy_serverless_type is not None:
            result['ProxyServerlessType'] = self.proxy_serverless_type

        if self.proxy_standard_cpu_cores is not None:
            result['ProxyStandardCpuCores'] = self.proxy_standard_cpu_cores

        if self.proxy_status is not None:
            result['ProxyStatus'] = self.proxy_status

        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.restore_data_point is not None:
            result['RestoreDataPoint'] = self.restore_data_point

        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type

        if self.row_compression is not None:
            result['RowCompression'] = self.row_compression

        if self.sqlsize is not None:
            result['SQLSize'] = self.sqlsize

        if self.serverless_type is not None:
            result['ServerlessType'] = self.serverless_type

        if self.source_dbcluster is not None:
            result['SourceDBCluster'] = self.source_dbcluster

        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id

        if self.standby_hamode is not None:
            result['StandbyHAMode'] = self.standby_hamode

        if self.storage_max is not None:
            result['StorageMax'] = self.storage_max

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

        if self.support_instant_switch_with_imci is not None:
            result['SupportInstantSwitchWithImci'] = self.support_instant_switch_with_imci

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiCreatingTime') is not None:
            self.ai_creating_time = m.get('AiCreatingTime')

        if m.get('AiType') is not None:
            self.ai_type = m.get('AiType')

        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('AutoUpgradeMinorVersion') is not None:
            self.auto_upgrade_minor_version = m.get('AutoUpgradeMinorVersion')

        if m.get('BlktagTotal') is not None:
            self.blktag_total = m.get('BlktagTotal')

        if m.get('BlktagUsed') is not None:
            self.blktag_used = m.get('BlktagUsed')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CompressStorageMode') is not None:
            self.compress_storage_mode = m.get('CompressStorageMode')

        if m.get('CompressStorageUsed') is not None:
            self.compress_storage_used = m.get('CompressStorageUsed')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')

        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')

        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k1 in m.get('DBNodes'):
                temp_model = main_models.DescribeDbClusterAttributeZonalResponseBodyDBNodes()
                self.dbnodes.append(temp_model.from_map(k1))

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('DBVersionStatus') is not None:
            self.dbversion_status = m.get('DBVersionStatus')

        if m.get('DataLevel1BackupChainSize') is not None:
            self.data_level_1backup_chain_size = m.get('DataLevel1BackupChainSize')

        if m.get('DataSyncMode') is not None:
            self.data_sync_mode = m.get('DataSyncMode')

        if m.get('DeletionLock') is not None:
            self.deletion_lock = m.get('DeletionLock')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('HasCompleteStandbyRes') is not None:
            self.has_complete_standby_res = m.get('HasCompleteStandbyRes')

        if m.get('HotStandbyCluster') is not None:
            self.hot_standby_cluster = m.get('HotStandbyCluster')

        if m.get('ImciAutoIndex') is not None:
            self.imci_auto_index = m.get('ImciAutoIndex')

        if m.get('ImperceptibleSwitch') is not None:
            self.imperceptible_switch = m.get('ImperceptibleSwitch')

        if m.get('InodeTotal') is not None:
            self.inode_total = m.get('InodeTotal')

        if m.get('InodeUsed') is not None:
            self.inode_used = m.get('InodeUsed')

        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')

        if m.get('IsProxyLatestVersion') is not None:
            self.is_proxy_latest_version = m.get('IsProxyLatestVersion')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')

        if m.get('Orca') is not None:
            self.orca = m.get('Orca')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('ProxyCpuCores') is not None:
            self.proxy_cpu_cores = m.get('ProxyCpuCores')

        if m.get('ProxyServerlessType') is not None:
            self.proxy_serverless_type = m.get('ProxyServerlessType')

        if m.get('ProxyStandardCpuCores') is not None:
            self.proxy_standard_cpu_cores = m.get('ProxyStandardCpuCores')

        if m.get('ProxyStatus') is not None:
            self.proxy_status = m.get('ProxyStatus')

        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RestoreDataPoint') is not None:
            self.restore_data_point = m.get('RestoreDataPoint')

        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')

        if m.get('RowCompression') is not None:
            self.row_compression = m.get('RowCompression')

        if m.get('SQLSize') is not None:
            self.sqlsize = m.get('SQLSize')

        if m.get('ServerlessType') is not None:
            self.serverless_type = m.get('ServerlessType')

        if m.get('SourceDBCluster') is not None:
            self.source_dbcluster = m.get('SourceDBCluster')

        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')

        if m.get('StandbyHAMode') is not None:
            self.standby_hamode = m.get('StandbyHAMode')

        if m.get('StorageMax') is not None:
            self.storage_max = m.get('StorageMax')

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

        if m.get('SupportInstantSwitchWithImci') is not None:
            self.support_instant_switch_with_imci = m.get('SupportInstantSwitchWithImci')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeDbClusterAttributeZonalResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')

        return self

class DescribeDbClusterAttributeZonalResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

class DescribeDbClusterAttributeZonalResponseBodyDBNodes(DaraModel):
    def __init__(
        self,
        added_cpu_cores: str = None,
        cpu_cores: str = None,
        creation_time: str = None,
        dbnode_class: str = None,
        dbnode_description: str = None,
        dbnode_id: str = None,
        dbnode_role: str = None,
        dbnode_status: str = None,
        failover_priority: int = None,
        hot_replica_mode: str = None,
        imci_switch: str = None,
        master_id: str = None,
        max_connections: int = None,
        max_iops: int = None,
        memory_size: str = None,
        mirror_ins_name: str = None,
        multi_master_local_standby: str = None,
        multi_master_primary_node: str = None,
        orca: str = None,
        remote_memory_size: str = None,
        scc_mode: str = None,
        server_weight: str = None,
        serverless_type: str = None,
        sub_cluster: str = None,
        sub_group_description: str = None,
        zone_id: str = None,
    ):
        self.added_cpu_cores = added_cpu_cores
        self.cpu_cores = cpu_cores
        self.creation_time = creation_time
        self.dbnode_class = dbnode_class
        self.dbnode_description = dbnode_description
        self.dbnode_id = dbnode_id
        self.dbnode_role = dbnode_role
        self.dbnode_status = dbnode_status
        self.failover_priority = failover_priority
        self.hot_replica_mode = hot_replica_mode
        self.imci_switch = imci_switch
        self.master_id = master_id
        self.max_connections = max_connections
        self.max_iops = max_iops
        self.memory_size = memory_size
        self.mirror_ins_name = mirror_ins_name
        # MultiMasterLocalStandby
        self.multi_master_local_standby = multi_master_local_standby
        # MultiMasterPrimaryNode
        self.multi_master_primary_node = multi_master_primary_node
        self.orca = orca
        self.remote_memory_size = remote_memory_size
        # This parameter is required.
        self.scc_mode = scc_mode
        self.server_weight = server_weight
        self.serverless_type = serverless_type
        self.sub_cluster = sub_cluster
        # SubGroupDescription
        self.sub_group_description = sub_group_description
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.added_cpu_cores is not None:
            result['AddedCpuCores'] = self.added_cpu_cores

        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_description is not None:
            result['DBNodeDescription'] = self.dbnode_description

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.dbnode_role is not None:
            result['DBNodeRole'] = self.dbnode_role

        if self.dbnode_status is not None:
            result['DBNodeStatus'] = self.dbnode_status

        if self.failover_priority is not None:
            result['FailoverPriority'] = self.failover_priority

        if self.hot_replica_mode is not None:
            result['HotReplicaMode'] = self.hot_replica_mode

        if self.imci_switch is not None:
            result['ImciSwitch'] = self.imci_switch

        if self.master_id is not None:
            result['MasterId'] = self.master_id

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.mirror_ins_name is not None:
            result['MirrorInsName'] = self.mirror_ins_name

        if self.multi_master_local_standby is not None:
            result['MultiMasterLocalStandby'] = self.multi_master_local_standby

        if self.multi_master_primary_node is not None:
            result['MultiMasterPrimaryNode'] = self.multi_master_primary_node

        if self.orca is not None:
            result['Orca'] = self.orca

        if self.remote_memory_size is not None:
            result['RemoteMemorySize'] = self.remote_memory_size

        if self.scc_mode is not None:
            result['SccMode'] = self.scc_mode

        if self.server_weight is not None:
            result['ServerWeight'] = self.server_weight

        if self.serverless_type is not None:
            result['ServerlessType'] = self.serverless_type

        if self.sub_cluster is not None:
            result['SubCluster'] = self.sub_cluster

        if self.sub_group_description is not None:
            result['SubGroupDescription'] = self.sub_group_description

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddedCpuCores') is not None:
            self.added_cpu_cores = m.get('AddedCpuCores')

        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeDescription') is not None:
            self.dbnode_description = m.get('DBNodeDescription')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('DBNodeRole') is not None:
            self.dbnode_role = m.get('DBNodeRole')

        if m.get('DBNodeStatus') is not None:
            self.dbnode_status = m.get('DBNodeStatus')

        if m.get('FailoverPriority') is not None:
            self.failover_priority = m.get('FailoverPriority')

        if m.get('HotReplicaMode') is not None:
            self.hot_replica_mode = m.get('HotReplicaMode')

        if m.get('ImciSwitch') is not None:
            self.imci_switch = m.get('ImciSwitch')

        if m.get('MasterId') is not None:
            self.master_id = m.get('MasterId')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('MirrorInsName') is not None:
            self.mirror_ins_name = m.get('MirrorInsName')

        if m.get('MultiMasterLocalStandby') is not None:
            self.multi_master_local_standby = m.get('MultiMasterLocalStandby')

        if m.get('MultiMasterPrimaryNode') is not None:
            self.multi_master_primary_node = m.get('MultiMasterPrimaryNode')

        if m.get('Orca') is not None:
            self.orca = m.get('Orca')

        if m.get('RemoteMemorySize') is not None:
            self.remote_memory_size = m.get('RemoteMemorySize')

        if m.get('SccMode') is not None:
            self.scc_mode = m.get('SccMode')

        if m.get('ServerWeight') is not None:
            self.server_weight = m.get('ServerWeight')

        if m.get('ServerlessType') is not None:
            self.serverless_type = m.get('ServerlessType')

        if m.get('SubCluster') is not None:
            self.sub_cluster = m.get('SubCluster')

        if m.get('SubGroupDescription') is not None:
            self.sub_group_description = m.get('SubGroupDescription')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

