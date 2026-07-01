# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterAttributeResponseBody(DaraModel):
    def __init__(
        self,
        ai_creating_time: str = None,
        ai_type: str = None,
        architecture: str = None,
        auto_upgrade_minor_version: str = None,
        blktag_total: int = None,
        blktag_used: int = None,
        branch: main_models.DescribeDBClusterAttributeResponseBodyBranch = None,
        bursting_enabled: str = None,
        category: str = None,
        column_table: str = None,
        compress_storage_mode: str = None,
        compress_storage_used: int = None,
        connection_resource_quota: int = None,
        connection_resource_used: int = None,
        creation_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_network_type: str = None,
        dbcluster_status: str = None,
        dbnodes: List[main_models.DescribeDBClusterAttributeResponseBodyDBNodes] = None,
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
        search_cluster_status: str = None,
        search_compress_storage_used: int = None,
        search_storage_used: int = None,
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
        tags: List[main_models.DescribeDBClusterAttributeResponseBodyTags] = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_ids: str = None,
    ):
        # The start time of the free AI trial.
        self.ai_creating_time = ai_creating_time
        # The AI node type. Valid values:
        #      
        # - **SearchNode**: search node.
        # - **DLNode**: AI node.
        self.ai_type = ai_type
        # The CPU architecture. Valid values:
        # - **X86**
        # - **ARM**
        self.architecture = architecture
        # The minor version update method. Valid values:
        # 
        # - Auto: automatic update.
        # - Manual: manual update.
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        # The maximum number of blktags in the file system.
        self.blktag_total = blktag_total
        # The current blktag usage.
        self.blktag_used = blktag_used
        self.branch = branch
        # Indicates whether I/O performance burst is enabled for the ESSD AutoPL cloud disk. Valid values:
        # 
        # - **true**: enabled.
        # - **false**: disabled.
        self.bursting_enabled = bursting_enabled
        # The [edition](https://help.aliyun.com/document_detail/183258.html) of the cluster. Valid values:
        # * **Normal**: Cluster Edition
        # * **Basic**: Single Node Edition
        # * **Archive**: PolarDB X-Engine Edition
        # * **NormalMultimaster**: Multi-master Cluster Edition
        # * **SENormal**: PolarDB for MySQL Standard Edition
        # 
        # > * PolarDB for PostgreSQL (PostgreSQL 11) does not support Single Node Edition.
        # >* PolarDB for MySQL 8.0, PolarDB for MySQL 5.7, and PolarDB for PostgreSQL (PostgreSQL 14) support PolarDB for MySQL Standard Edition.
        # >* PolarDB for MySQL 8.0 supports PolarDB X-Engine Edition and Multi-master Cluster Edition.
        self.category = category
        # Indicates whether column store tables are enabled.
        self.column_table = column_table
        # Indicates whether storage compression is enabled. Valid values:
        # - ON: enabled
        # - OFF: disabled
        self.compress_storage_mode = compress_storage_mode
        # The compressed storage data size.
        # >This parameter is returned only when the storage compression feature is enabled for the cluster.
        self.compress_storage_used = compress_storage_used
        self.connection_resource_quota = connection_resource_quota
        self.connection_resource_used = connection_resource_used
        # The time when the cluster was created.
        self.creation_time = creation_time
        # The cluster description.
        self.dbcluster_description = dbcluster_description
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The network type of the cluster.
        self.dbcluster_network_type = dbcluster_network_type
        # The cluster status. For more information, see [Cluster status table](https://help.aliyun.com/document_detail/99286.html).
        self.dbcluster_status = dbcluster_status
        # The details of nodes.
        self.dbnodes = dbnodes
        # The database engine type.
        self.dbtype = dbtype
        # The database engine version.
        self.dbversion = dbversion
        # The status of the current minor engine version. Valid values:
        # * **Stable**: The current version is stable.
        # * **Old**: The current version is outdated. Upgrade to the latest version.
        # * **HighRisk**: The current version has critical defects. Upgrade to the latest version immediately.
        # * **Beta**: The current version is a beta version.
        # 
        # > * For information about how to upgrade the minor engine version, see [Version upgrade](https://help.aliyun.com/document_detail/158572.html).
        # > * This parameter is returned only when the database engine type (**DBType**) is **MySQL**.
        self.dbversion_status = dbversion_status
        # The total size of level-1 backups (snapshots), in bytes.
        self.data_level_1backup_chain_size = data_level_1backup_chain_size
        # The data replication relationship mode. Valid values:
        # - **AsyncSync**: asynchronous
        # - **SemiSync**: semi-synchronous
        self.data_sync_mode = data_sync_mode
        # The lock status for cluster deletion. Valid values:
        # * **0**: Unlocked. The cluster can be deleted.
        # * **1**: Locked. The cluster cannot be deleted.
        self.deletion_lock = deletion_lock
        # The cluster engine.
        self.engine = engine
        # The expiration time of the cluster.
        # 
        # > A specific value is returned only for clusters whose billing method is **Prepaid** (subscription). An empty value is returned for **Postpaid** (pay-as-you-go) clusters.
        self.expire_time = expire_time
        # Indicates whether the cluster has expired.
        # > This parameter is returned only for clusters whose billing method is **Prepaid** (subscription).
        self.expired = expired
        # Indicates whether resources are replenished for the new primary database after a cross-zone failover. Valid values:
        # - **true**: Resources are replenished.
        # - **false**: Resources are not replenished.
        self.has_complete_standby_res = has_complete_standby_res
        # Indicates whether the Hot Standby Cluster (and standby compute nodes) is enabled. Valid values:
        # - **StandbyClusterON**: The Hot Standby Cluster and standby compute nodes are enabled.
        # - **StandbyClusterOFF**: The Hot Standby Cluster and standby compute nodes are disabled.
        self.hot_standby_cluster = hot_standby_cluster
        # The automatic IMCI-based query acceleration feature. Valid values:
        # - `ON`: enabled.
        # - `OFF`: disabled.
        self.imci_auto_index = imci_auto_index
        # The failover with hot replica feature. Valid values:
        # - `true`: enabled.
        # - `false`: disabled.
        self.imperceptible_switch = imperceptible_switch
        # The maximum number of inodes in the file system.
        self.inode_total = inode_total
        # The current inode usage.
        self.inode_used = inode_used
        # Indicates whether the cluster runs the latest Milvus version. Valid values:
        # 
        # - **true**: The cluster runs the latest Milvus version.
        # 
        # - **false**: The cluster does not run the latest Milvus version.
        self.is_latest_version = is_latest_version
        # Indicates whether the database proxy is the latest version. Valid values:
        # 
        # - **true**: The database proxy is the latest version.
        # - **false**: The database proxy is not the latest version.
        self.is_proxy_latest_version = is_proxy_latest_version
        # The lock mode. Valid values: 
        # 
        # - **Unlock**: not locked.
        # - **ManualLock**: manually locked. 
        # - **LockByExpiration**: automatically locked due to cluster expiration.
        self.lock_mode = lock_mode
        # The maintenance window of the cluster, in the `HH:mmZ-HH:mmZ` format (UTC). For example, `16:00Z-17:00Z` indicates that routine maintenance can be performed from 00:00 to 01:00 (UTC+08:00).
        self.maintain_time = maintain_time
        # The Orca feature. Valid values:
        # 
        # - on: enabled.
        # 
        # - off: disabled.
        self.orca = orca
        # The billing method. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go.
        # - **Prepaid**: subscription.
        self.pay_type = pay_type
        # <p id="p_wyg_t4a_glm" props="china" icmsditafragmentmagic=1>The provisioned read/write IOPS of the ESSD AutoPL cloud disk. Valid values: 0 to min{50,000, 1000 × capacity - baseline performance}.</p>
        # <p id="p_6de_jxy_k2g" props="china" icmsditafragmentmagic=1>Baseline performance = min{1,800 + 50 × capacity, 50,000}.</p>
        # <note id="note_7kj_j0o_rgs" props="china" icmsditafragmentmagic=1>This parameter is supported only when StorageType is set to ESSDAUTOPL.</note>
        self.provisioned_iops = provisioned_iops
        # The number of CPU cores of the database proxy.
        self.proxy_cpu_cores = proxy_cpu_cores
        # The serverless type of the database proxy. Valid values:
        # - AgileServerless: agile serverless cluster.
        # - SteadyServerless: steady serverless, which is a cluster with defined specifications (subscription or pay-as-you-go billing).
        self.proxy_serverless_type = proxy_serverless_type
        # The number of CPU cores in the standard configuration of the database proxy.
        self.proxy_standard_cpu_cores = proxy_standard_cpu_cores
        # The status of the database proxy. Valid values:
        # 
        # - **Creating**: being created.
        # - **Running**: running.
        # - **Deleting**: being released.
        # - **Rebooting**: being restarted.
        # - **DBNodeCreating**: adding a node.
        # - **DBNodeDeleting**: deleting a node.
        # - **ClassChanging**: changing node specifications.
        # - **NetAddressCreating**: creating network connectivity.
        # - **NetAddressDeleting**: deleting network connectivity.
        # - **NetAddressModifying**: modifying network connectivity.
        # - **Deleted**: released.
        self.proxy_status = proxy_status
        # The type of the database proxy. Valid values:
        # 
        # - **Exclusive**: Dedicated Enterprise Edition
        # - **General**: Standard Enterprise Edition
        self.proxy_type = proxy_type
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # * If RestoreType is **RestoreByTime** or **RestoreByTimeOss**, this value indicates the point in time to which the cluster is restored.
        # * If RestoreType is **RestoreByBackupSet** or **RestoreByBackupSetOss**, this value indicates the backup set ID used for the restoration.
        # 
        # <note>This parameter is supported only for clusters restored from a backup set or point in time after June 1, 2024.</note>
        self.restore_data_point = restore_data_point
        # The restoration method of the cluster. Valid values:
        # 
        # * **RestoreByTime**: point-in-time restore based on a level-1 backup.
        # * **RestoreByBackupSet**: restore from a level-1 backup set.
        # * **RestoreByTimeOss**: point-in-time restore based on a level-2 backup.
        # * **RestoreByBackupSetOss**: restore from a level-2 backup set.
        # * **CloneFromSourceCluster**: clone from the source cluster.
        # 
        # <note>This parameter is supported only for clusters restored from a backup set or point in time after June 1, 2024.</note>
        self.restore_type = restore_type
        # The row compression setting.
        self.row_compression = row_compression
        # The storage size of SQL statements, in bytes. A value of -1 indicates that no data is available.
        self.sqlsize = sqlsize
        # The running status of the search node.
        self.search_cluster_status = search_cluster_status
        # The compressed storage data size of the search node.
        # >This parameter is returned only when the storage compression feature is enabled for the cluster.
        self.search_compress_storage_used = search_compress_storage_used
        # The storage usage of the search node.
        self.search_storage_used = search_storage_used
        # The serverless type of the cluster. Valid values:
        # 
        # - AgileServerless: agile serverless cluster.
        # - SteadyServerless: steady serverless, which is a cluster with defined specifications that has the serverless feature enabled.
        # 
        # > This parameter is supported only for serverless clusters or clusters with defined specifications that have the serverless feature enabled.
        self.serverless_type = serverless_type
        # The source cluster ID.
        # <note>This parameter is supported only for clusters restored from a backup set or point in time after June 1, 2024.</note>
        self.source_dbcluster = source_dbcluster
        # The region ID of the source cluster.
        # <note>This parameter is returned only when the source cluster ID exists.</note>
        self.source_region_id = source_region_id
        # The cross-zone disaster recovery mode. Valid values:
        # - **ON**: Cross-zone disaster recovery is enabled.
        # - **OFF**: Cross-zone disaster recovery is disabled.
        # - **0**: Customer drill mode.
        self.standby_hamode = standby_hamode
        # The maximum storage capacity for the current cluster specifications, in bytes.
        self.storage_max = storage_max
        # The billing method for storage. Valid values:
        # 
        # - **Postpaid**: pay-by-capacity (pay-as-you-go).
        # - **Prepaid**: pay-by-space (subscription).
        self.storage_pay_type = storage_pay_type
        # The storage space for pay-by-space (subscription) billing. Unit: bytes.
        self.storage_space = storage_space
        # The storage type. The value is fixed as **HighPerformance**.
        self.storage_type = storage_type
        # The storage usage, in bytes.
        self.storage_used = storage_used
        # Indicates whether multi-zone strong data consistency is enabled for the cluster. Valid values:
        # 
        # - **ON**: Multi-zone strong data consistency is enabled. This applies to PolarDB for MySQL Standard Edition with three-zone deployment.
        # 
        # - **OFF**: Multi-zone strong data consistency is not enabled.
        self.strict_consistency = strict_consistency
        # The specification type of compute nodes. Valid values:
        # * **Exclusive**: Dedicated
        # * **General**: General-purpose
        # 
        # > This parameter is returned only for PolarDB for MySQL clusters of the Cluster Edition.
        self.sub_category = sub_category
        # Indicates whether failover with hot replica is supported with IMCI compatibility.
        self.support_instant_switch_with_imci = support_instant_switch_with_imci
        # The details of tags.
        self.tags = tags
        # The VPC ID.
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_ids = zone_ids

    def validate(self):
        if self.branch:
            self.branch.validate()
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

        if self.branch is not None:
            result['Branch'] = self.branch.to_map()

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.category is not None:
            result['Category'] = self.category

        if self.column_table is not None:
            result['ColumnTable'] = self.column_table

        if self.compress_storage_mode is not None:
            result['CompressStorageMode'] = self.compress_storage_mode

        if self.compress_storage_used is not None:
            result['CompressStorageUsed'] = self.compress_storage_used

        if self.connection_resource_quota is not None:
            result['ConnectionResourceQuota'] = self.connection_resource_quota

        if self.connection_resource_used is not None:
            result['ConnectionResourceUsed'] = self.connection_resource_used

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

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

        if self.search_cluster_status is not None:
            result['SearchClusterStatus'] = self.search_cluster_status

        if self.search_compress_storage_used is not None:
            result['SearchCompressStorageUsed'] = self.search_compress_storage_used

        if self.search_storage_used is not None:
            result['SearchStorageUsed'] = self.search_storage_used

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

        if m.get('Branch') is not None:
            temp_model = main_models.DescribeDBClusterAttributeResponseBodyBranch()
            self.branch = temp_model.from_map(m.get('Branch'))

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ColumnTable') is not None:
            self.column_table = m.get('ColumnTable')

        if m.get('CompressStorageMode') is not None:
            self.compress_storage_mode = m.get('CompressStorageMode')

        if m.get('CompressStorageUsed') is not None:
            self.compress_storage_used = m.get('CompressStorageUsed')

        if m.get('ConnectionResourceQuota') is not None:
            self.connection_resource_quota = m.get('ConnectionResourceQuota')

        if m.get('ConnectionResourceUsed') is not None:
            self.connection_resource_used = m.get('ConnectionResourceUsed')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

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
                temp_model = main_models.DescribeDBClusterAttributeResponseBodyDBNodes()
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

        if m.get('SearchClusterStatus') is not None:
            self.search_cluster_status = m.get('SearchClusterStatus')

        if m.get('SearchCompressStorageUsed') is not None:
            self.search_compress_storage_used = m.get('SearchCompressStorageUsed')

        if m.get('SearchStorageUsed') is not None:
            self.search_storage_used = m.get('SearchStorageUsed')

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
                temp_model = main_models.DescribeDBClusterAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')

        return self

class DescribeDBClusterAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class DescribeDBClusterAttributeResponseBodyDBNodes(DaraModel):
    def __init__(
        self,
        added_cpu_cores: str = None,
        cpu_cores: str = None,
        creation_time: str = None,
        dbnode_cxlremote_memory: str = None,
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
        # The number of CPU cores added by second-level rapid scaling.
        self.added_cpu_cores = added_cpu_cores
        # The number of CPU cores of the node.
        self.cpu_cores = cpu_cores
        # The time when the node was created.
        self.creation_time = creation_time
        # The CXL remote memory configuration.
        self.dbnode_cxlremote_memory = dbnode_cxlremote_memory
        # The node specifications.
        self.dbnode_class = dbnode_class
        # The node description.
        self.dbnode_description = dbnode_description
        # The node ID.
        self.dbnode_id = dbnode_id
        # The role of the node. Valid values: 
        # 
        # - **Writer**: read/write node.
        # - **Reader**: read-only node.
        self.dbnode_role = dbnode_role
        # The node status. Valid values:
        # * **Creating**: being created.
        # * **Running**: running.
        # * **Deleting**: being deleted.
        # * **Rebooting**: being restarted.
        # * **DBNodeCreating**: adding a node.
        # * **DBNodeDeleting**: deleting a node.
        # * **ClassChanging**: changing node specifications.
        # * **NetAddressCreating**: creating network connectivity.
        # * **NetAddressDeleting**: deleting network connectivity.
        # * **NetAddressModifying**: modifying network connectivity.
        # * **MinorVersionUpgrading**: performing a minor engine version upgrade.
        # * **Maintaining**: instance under maintenance.
        # * **Switching**: being switched.
        self.dbnode_status = dbnode_status
        # The failover priority. Each node has a failover priority that determines the probability of the node being elected as the primary node during a failover. A higher value indicates a higher priority.
        # Valid values: 1 to 15.
        self.failover_priority = failover_priority
        # Indicates whether hot standby is enabled. Valid values:
        # 
        # - **ON**: enabled.
        # 
        # - **OFF**: disabled.
        self.hot_replica_mode = hot_replica_mode
        # Indicates whether In-Memory Column Index (IMCI) is enabled. Valid values:
        # 
        # - **ON**: enabled.
        # 
        # - **OFF**: disabled.
        self.imci_switch = imci_switch
        # The primary node ID of the Multi-master Cluster Edition.
        self.master_id = master_id
        # The maximum number of concurrent connections to the cluster.
        self.max_connections = max_connections
        # The maximum number of I/O requests per second (IOPS).
        self.max_iops = max_iops
        # The memory size of the node. Unit: MB.
        self.memory_size = memory_size
        # The name of the hot replica compute node that corresponds to the node in the Hot Standby Cluster and compute architecture.
        self.mirror_ins_name = mirror_ins_name
        # The multi-master local standby node.
        self.multi_master_local_standby = multi_master_local_standby
        # The multi-master primary node.
        self.multi_master_primary_node = multi_master_primary_node
        # The Orca feature. Valid values:
        # 
        # - on: enabled.
        # 
        # - off: disabled.
        self.orca = orca
        # The remote memory size. Unit: MB.
        self.remote_memory_size = remote_memory_size
        # Indicates whether the global consistency (high-performance mode) feature is enabled for the node. Valid values:
        # 
        # - **ON**: The feature is enabled.
        # 
        # - **OFF**: The feature is disabled.
        # 
        # This parameter is required.
        self.scc_mode = scc_mode
        # The routing weight.
        # Valid values: 1 to 100. Default value: 1.
        self.server_weight = server_weight
        # The serverless type of the node. Valid values:
        # 
        # - AgileServerless: agile serverless node.
        # - SteadyServerless: steady serverless node, which is a node with defined specifications that has the serverless capability enabled.
        # 
        # > This parameter is supported only for serverless clusters or clusters with defined specifications that have the serverless feature enabled. For more information, see [Serverless](https://help.aliyun.com/document_detail/452274.html).
        self.serverless_type = serverless_type
        # Indicates whether the node is in the primary zone or the secondary zone. This parameter is mainly used for resource-equivalent deployments.
        # Valid values:
        # - Primary: primary zone.
        # - Standby: secondary zone.
        self.sub_cluster = sub_cluster
        # The cluster subgroup description.
        self.sub_group_description = sub_group_description
        # The zone ID.
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

        if self.dbnode_cxlremote_memory is not None:
            result['DBNodeCXLRemoteMemory'] = self.dbnode_cxlremote_memory

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

        if m.get('DBNodeCXLRemoteMemory') is not None:
            self.dbnode_cxlremote_memory = m.get('DBNodeCXLRemoteMemory')

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

class DescribeDBClusterAttributeResponseBodyBranch(DaraModel):
    def __init__(
        self,
        branch_lsn: str = None,
        branch_time: str = None,
        child_branch: List[main_models.DescribeDBClusterAttributeResponseBodyBranchChildBranch] = None,
        parent_ins_name: str = None,
    ):
        self.branch_lsn = branch_lsn
        self.branch_time = branch_time
        self.child_branch = child_branch
        self.parent_ins_name = parent_ins_name

    def validate(self):
        if self.child_branch:
            for v1 in self.child_branch:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_lsn is not None:
            result['BranchLsn'] = self.branch_lsn

        if self.branch_time is not None:
            result['BranchTime'] = self.branch_time

        result['ChildBranch'] = []
        if self.child_branch is not None:
            for k1 in self.child_branch:
                result['ChildBranch'].append(k1.to_map() if k1 else None)

        if self.parent_ins_name is not None:
            result['ParentInsName'] = self.parent_ins_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchLsn') is not None:
            self.branch_lsn = m.get('BranchLsn')

        if m.get('BranchTime') is not None:
            self.branch_time = m.get('BranchTime')

        self.child_branch = []
        if m.get('ChildBranch') is not None:
            for k1 in m.get('ChildBranch'):
                temp_model = main_models.DescribeDBClusterAttributeResponseBodyBranchChildBranch()
                self.child_branch.append(temp_model.from_map(k1))

        if m.get('ParentInsName') is not None:
            self.parent_ins_name = m.get('ParentInsName')

        return self

class DescribeDBClusterAttributeResponseBodyBranchChildBranch(DaraModel):
    def __init__(
        self,
        branch_lsn: str = None,
        branch_time: str = None,
        dbcluster_description: str = None,
        has_child: bool = None,
        ins_name: str = None,
    ):
        self.branch_lsn = branch_lsn
        self.branch_time = branch_time
        self.dbcluster_description = dbcluster_description
        self.has_child = has_child
        self.ins_name = ins_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_lsn is not None:
            result['BranchLsn'] = self.branch_lsn

        if self.branch_time is not None:
            result['BranchTime'] = self.branch_time

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.has_child is not None:
            result['HasChild'] = self.has_child

        if self.ins_name is not None:
            result['InsName'] = self.ins_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchLsn') is not None:
            self.branch_lsn = m.get('BranchLsn')

        if m.get('BranchTime') is not None:
            self.branch_time = m.get('BranchTime')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('HasChild') is not None:
            self.has_child = m.get('HasChild')

        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')

        return self

