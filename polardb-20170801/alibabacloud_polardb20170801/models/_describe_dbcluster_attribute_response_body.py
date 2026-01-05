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
        bursting_enabled: str = None,
        category: str = None,
        compress_storage_mode: str = None,
        compress_storage_used: int = None,
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
        # Start time for free AI activation
        self.ai_creating_time = ai_creating_time
        # Types of AI nodes. Values include:
        # 
        # - **SearchNode**: Search node.
        # - **DLNode**: AI node.
        self.ai_type = ai_type
        # CPU architecture. Available options are:
        # - **X86**
        # - **ARM**
        self.architecture = architecture
        # The minor version upgrade method.
        # 
        # *   Auto
        # *   Manual
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        # Maximum number of blktags in the file system.
        self.blktag_total = blktag_total
        # Current blktag usage.
        self.blktag_used = blktag_used
        self.bursting_enabled = bursting_enabled
        # [Product Series](https://help.aliyun.com/document_detail/183258.html), with values as follows:
        # * **Normal**: Cluster Edition
        # * **Basic**: Single Node
        # * **Archive**: High Compression Engine (X-Engine)
        # * **NormalMultimaster**: Multi-Master Cluster Edition
        # * **SENormal**: Standard Edition
        # 
        # > * PolarDB PostgreSQL version 11 does not support single-node.
        # >* PolarDB MySQL versions 8.0 and 5.7, and PolarDB PostgreSQL version 14 support the Standard Edition.
        # >* PolarDB MySQL version 8.0 supports High Compression Engine (X-Engine) and Multi-Master Cluster Edition.
        self.category = category
        # Whether storage compression is enabled. Values are as follows:
        # - ON: Enabled
        # - OFF: Disabled
        self.compress_storage_mode = compress_storage_mode
        # Compressed storage data size.
        # > This parameter is supported only when the cluster\\"s storage compression feature is enabled.
        self.compress_storage_used = compress_storage_used
        # Cluster creation time.
        self.creation_time = creation_time
        # Cluster description.
        self.dbcluster_description = dbcluster_description
        # Cluster ID.
        self.dbcluster_id = dbcluster_id
        # Network type of the cluster.
        self.dbcluster_network_type = dbcluster_network_type
        # Cluster status. For the full list of values, refer to [Cluster Status Table](https://help.aliyun.com/document_detail/99286.html).
        self.dbcluster_status = dbcluster_status
        # The information about the nodes.
        self.dbnodes = dbnodes
        # Database engine type.
        self.dbtype = dbtype
        # Database engine version.
        self.dbversion = dbversion
        # The status of the minor version. Valid values:
        # 
        # *   **Stable**: The minor version is stable.
        # *   **Old**: The minor version is outdated. We recommend that you update it to the latest version.
        # *   **HighRisk**: The minor version has critical defects. We recommend that you immediately update it to the latest version.
        # *   **Beta**: The minor version is a Beta version.
        # 
        # >  For information about how to update the minor version, see [Minor version update](https://help.aliyun.com/document_detail/158572.html).
        self.dbversion_status = dbversion_status
        # Total size of Level 1 backups (snapshots), in bytes.
        self.data_level_1backup_chain_size = data_level_1backup_chain_size
        # Data replication relationship mode. Values are as follows:
        # - **AsyncSync**: Asynchronous
        # - **SemiSync**: Semi-synchronous
        self.data_sync_mode = data_sync_mode
        # Lock status for cluster deletion, with values as follows:
        # * **0**: Unlocked, cluster can be deleted.
        # * **1**: Locked, cluster cannot be deleted.
        self.deletion_lock = deletion_lock
        # Cluster engine.
        self.engine = engine
        # Cluster expiration time.
        # 
        # > Only clusters with **Prepaid** (subscription) payment methods return specific parameter values; **Postpaid** (pay-as-you-go) clusters return empty values.
        self.expire_time = expire_time
        # Whether the cluster has expired.
        # > This parameter is only supported for clusters with **Prepaid** (Subscription) payment methods.
        self.expired = expired
        # Whether to replenish resources for the new primary after cross-AZ switch. Values are as follows:
        # - **true**: Yes
        # - **false**: No
        self.has_complete_standby_res = has_complete_standby_res
        # Whether to enable storage hot backup cluster (and Standby compute nodes). Values are as follows:
        # - **StandbyClusterON**: Enable storage hot backup/Enable storage hot backup and Standby compute nodes.
        # - **StandbyClusterOFF**: Disable storage hot backup/Disable storage hot backup and Standby compute nodes.
        self.hot_standby_cluster = hot_standby_cluster
        # Indicates whether the automatic IMCI-based query acceleration feature is enabled. Valid values:
        # 
        # *   `ON`: enabled
        # *   `OFF`: disabled
        self.imci_auto_index = imci_auto_index
        # Indicates whether failover with hot replica is enabled. Valid values:
        # 
        # *   `true`
        # *   `false` (default)
        self.imperceptible_switch = imperceptible_switch
        # Maximum number of inodes in the file system.
        self.inode_total = inode_total
        # Current inode usage.
        self.inode_used = inode_used
        # Indicates whether it is the latest kernel version. Values are as follows:
        # 
        # - **true**: Yes
        # 
        # - **false**: No
        self.is_latest_version = is_latest_version
        # Indicates whether it is the latest version of the database proxy, with possible values as follows:
        # 
        # - **true**: Yes
        # - **false**: No
        self.is_proxy_latest_version = is_proxy_latest_version
        # Lock mode. Possible values are as follows:
        # 
        # - **Unlock**: Unlocked.
        # - **ManualLock**: Manually triggered lock.
        # - **LockByExpiration**: Automatic cluster lock upon expiration.
        self.lock_mode = lock_mode
        # The maintenance window for the cluster, formatted as `HH:mmZ-HH:mmZ` (UTC time). For example, `16:00Z-17:00Z` indicates that routine maintenance can be performed from 0:00 to 1:00 (UTC+08:00).
        self.maintain_time = maintain_time
        # Orca function with possible values as follows:
        # 
        # - **on**: Enabled
        # 
        # - **off**: Disabled
        self.orca = orca
        # Payment type. Possible values are:
        # 
        # - **Postpaid**: Pay-As-You-Go
        # - **Prepaid**: Prepaid (Subscription).
        self.pay_type = pay_type
        # Describes the preconfigured read and write IOPS for ESSD AutoPL cloud disks. Possible values: 0 to min{50,000, 1000*capacity - baseline performance}.<br>Baseline performance = min{1,800 + 50*capacity, 50000}.<br>Note: This parameter is supported only when StorageType is ESSDAUTOPL.
        self.provisioned_iops = provisioned_iops
        # Number of CPU cores for the database proxy.
        self.proxy_cpu_cores = proxy_cpu_cores
        # Serverless type for the database proxy. Currently, the value is fixed to AgileServerless.
        self.proxy_serverless_type = proxy_serverless_type
        # Standard configuration CPU cores for the database proxy.
        self.proxy_standard_cpu_cores = proxy_standard_cpu_cores
        # Status of the database proxy. Possible values include:
        # 
        # - **Creating**: Creating
        # - **Running**: Running
        # - **Deleting**: Releasing
        # - **Rebooting**: Restarting
        # - **DBNodeCreating**: Adding nodes
        # - **DBNodeDeleting**: Deleting nodes
        # - **ClassChanging**: Changing node specifications
        # - **NetAddressCreating**: Creating network connections
        # - **NetAddressDeleting**: Deleting network connections
        # - **NetAddressModifying**: Modifying network connections
        # - **Deleted**: Released
        self.proxy_status = proxy_status
        # Database proxy types, with the following values:
        # 
        # - **Exclusive**: Enterprise Exclusive Edition
        # - **General**: Enterprise General Purpose Edition
        self.proxy_type = proxy_type
        # Region ID.
        self.region_id = region_id
        # Request ID.
        self.request_id = request_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # If RestoreType is **RestoreByTime** or **RestoreByTimeOss**, this value represents the recovery time point. If RestoreType is **RestoreByBackupSet** or **RestoreByBackupSetOss**, this value indicates the ID of the backup set on which the recovery is based.
        # <note>Only clusters restored from a backup set or time point after June 1, 2024, support this parameter.</note>
        self.restore_data_point = restore_data_point
        # Cluster recovery method, with possible values:
        # * **RestoreByTime**: Restore from a time point based on primary backup. * **RestoreByBackupSet**: Restore from a backup set based on primary backup. * **RestoreByTimeOss**: Restore from a time point based on secondary backup. * **RestoreByBackupSetOss**: Restore from a backup set based on secondary backup. * **CloneFromSourceCluster**: Clone from the source cluster.
        # <note>This parameter is only supported for clusters restored from a backup set or time point after June 1, 2024.</note>
        self.restore_type = restore_type
        self.row_compression = row_compression
        # Storage amount of SQL, in bytes. If the value is -1, it indicates no data.
        self.sqlsize = sqlsize
        self.search_cluster_status = search_cluster_status
        self.search_compress_storage_used = search_compress_storage_used
        self.search_storage_used = search_storage_used
        # Serverless type. Valid values are as follows:
        # - AgileServerless: Agile - SteadyServerless: Stable
        self.serverless_type = serverless_type
        # Source cluster ID. <note>Clusters restored from backup sets or specific points in time after June 1, 2024, support this parameter.</note>
        self.source_dbcluster = source_dbcluster
        # The region ID of the source cluster.
        # 
        # >  This parameter is returned only if the source cluster ID exists.
        self.source_region_id = source_region_id
        # Cross-AZ disaster recovery mode. Values are as follows:
        # - **ON**: Enable cross-AZ disaster recovery mode.
        # - **OFF**: Disable cross-AZ disaster recovery mode.
        # - **0**: Customer drill mode.
        self.standby_hamode = standby_hamode
        # The maximum storage capacity of the current cluster specification, in bytes.
        self.storage_max = storage_max
        # Storage billing type. Valid values are as follows:
        # - **Postpaid**: Pay-as-you-go (by capacity).
        # - **Prepaid**: Subscription (by space).
        self.storage_pay_type = storage_pay_type
        # Storage space for pay-by-space (subscription) billing. Unit: Byte.
        self.storage_space = storage_space
        # Storage type, with a fixed value of **HighPerformance**.
        self.storage_type = storage_type
        # Amount of used storage space, in bytes.
        self.storage_used = storage_used
        # Indicates whether multi-AZ data strong consistency is enabled for the cluster. The value ranges are as follows:
        # - **ON**: Indicates that multi-AZ data strong consistency is enabled, applicable to the Standard 3AZ scenario.
        # - **OFF**: Indicates that multi-AZ data strong consistency is not enabled.
        self.strict_consistency = strict_consistency
        # Specification type of compute nodes, with possible values as follows:
        # * **Exclusive**: Dedicated specification
        # * **General**: General-purpose specification
        # 
        # > This parameter is supported only for PolarDB MySQL Edition with the product series set to Cluster Edition.
        self.sub_category = sub_category
        # Indicates whether queries based on In-Memory Column Indexes (IMCIs) are supported during and after a failover with hot replica.
        self.support_instant_switch_with_imci = support_instant_switch_with_imci
        # Details of tags.
        self.tags = tags
        # VPC ID.
        self.vpcid = vpcid
        # VSwitch ID.
        self.v_switch_id = v_switch_id
        # Availability Zone IDs.
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
        # Tag key.
        self.key = key
        # Tag value.
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
        # Number of CPU cores for second-level elastic scaling.
        self.added_cpu_cores = added_cpu_cores
        # Number of CPU cores for the node.
        self.cpu_cores = cpu_cores
        # Node creation time.
        self.creation_time = creation_time
        self.dbnode_cxlremote_memory = dbnode_cxlremote_memory
        # Node specification.
        self.dbnode_class = dbnode_class
        self.dbnode_description = dbnode_description
        # Node ID.
        self.dbnode_id = dbnode_id
        # Node role, with possible values as follows:
        # 
        # - **Writer**: Primary node.
        # - **Reader**: Read-only node.
        self.dbnode_role = dbnode_role
        # Node status, with possible values as follows:
        # * **Creating**: Creating
        # * **Running**: Running
        # * **Deleting**: Deleting
        # * **Rebooting**: Rebooting
        # * **DBNodeCreating**: Adding node
        # * **DBNodeDeleting**: Removing node
        # * **ClassChanging**: Modifying node specification
        # * **NetAddressCreating**: Creating network connection
        # * **NetAddressDeleting**: Deleting network connection
        # * **NetAddressModifying**: Modifying network connection
        # * **MinorVersionUpgrading**: Upgrading minor version
        # * **Maintaining**: Instance maintenance
        # * **Switching**: Switching
        self.dbnode_status = dbnode_status
        # Failover priority. Each node has a failover priority, determining the likelihood of being elected as the primary node during a failover. A higher value indicates a higher priority.
        # Range: 1 to 15.
        self.failover_priority = failover_priority
        # Whether hot standby is enabled. Possible values are:
        # 
        # - **ON**: Enabled
        # - **OFF**: Disabled
        self.hot_replica_mode = hot_replica_mode
        # Whether columnar index is enabled. Possible values are:
        # 
        # - **ON**: Enabled
        # - **OFF**: Disabled
        self.imci_switch = imci_switch
        # Primary node ID of the multi-master architecture cluster edition.
        self.master_id = master_id
        # Maximum concurrent connections of the cluster.
        self.max_connections = max_connections
        # Maximum number of I/O requests, that is, IOPS.
        self.max_iops = max_iops
        # Node memory size, in MB.
        self.memory_size = memory_size
        # The name of the hot standby compute node corresponding to the node when the hot standby storage and compute clusters feature is enabled.
        self.mirror_ins_name = mirror_ins_name
        self.multi_master_local_standby = multi_master_local_standby
        self.multi_master_primary_node = multi_master_primary_node
        # Orca feature, valid values are:
        # - on: enabled
        # - off: disabled
        self.orca = orca
        # Remote memory size, in MB.
        self.remote_memory_size = remote_memory_size
        # Whether the node has the global consistency (high-performance mode) feature enabled. Possible values are:
        # 
        # - **ON**: Enabled
        # 
        # - **OFF**: Disabled
        # 
        # This parameter is required.
        self.scc_mode = scc_mode
        # Routing weight.
        # Range: 1~100. Default is 1.
        self.server_weight = server_weight
        # Serverless type. Possible values include:
        # 
        # - **AgileServerless**: Agile
        # - **SteadyServerless**: Steady
        # 
        # > This parameter is only supported by Serverless clusters.
        self.serverless_type = serverless_type
        # Identifies whether the node is in the primary or standby availability zone, primarily used in resource mirroring scenarios.
        # Values include:
        # - **Primary**: Primary Availability Zone
        # - **Standby**: Standby Availability Zone
        self.sub_cluster = sub_cluster
        self.sub_group_description = sub_group_description
        # Availability zone ID.
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

