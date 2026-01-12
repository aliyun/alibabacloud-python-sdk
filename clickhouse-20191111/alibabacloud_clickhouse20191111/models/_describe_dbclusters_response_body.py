# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClustersResponseBody(DaraModel):
    def __init__(
        self,
        dbclusters: main_models.DescribeDBClustersResponseBodyDBClusters = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The clusters.
        self.dbclusters = dbclusters
        # The total number of returned pages.
        self.page_number = page_number
        # The number of entries returned per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries that are returned.
        self.total_count = total_count

    def validate(self):
        if self.dbclusters:
            self.dbclusters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbclusters is not None:
            result['DBClusters'] = self.dbclusters.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusters') is not None:
            temp_model = main_models.DescribeDBClustersResponseBodyDBClusters()
            self.dbclusters = temp_model.from_map(m.get('DBClusters'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDBClustersResponseBodyDBClusters(DaraModel):
    def __init__(
        self,
        dbcluster: List[main_models.DescribeDBClustersResponseBodyDBClustersDBCluster] = None,
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
                temp_model = main_models.DescribeDBClustersResponseBodyDBClustersDBCluster()
                self.dbcluster.append(temp_model.from_map(k1))

        return self

class DescribeDBClustersResponseBodyDBClustersDBCluster(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        bid: str = None,
        category: str = None,
        commodity_code: str = None,
        connection_string: str = None,
        control_version: str = None,
        create_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_network_type: str = None,
        dbcluster_status: str = None,
        dbnode_class: str = None,
        dbnode_count: int = None,
        dbnode_storage: int = None,
        db_version: str = None,
        expire_time: str = None,
        ext_storage_size: int = None,
        ext_storage_type: str = None,
        is_expired: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        pay_type: str = None,
        port: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        scale_out_disable_write_windows: str = None,
        scale_out_status: main_models.DescribeDBClustersResponseBodyDBClustersDBClusterScaleOutStatus = None,
        storage_type: str = None,
        tags: main_models.DescribeDBClustersResponseBodyDBClustersDBClusterTags = None,
        v_switch_id: str = None,
        vpc_cloud_instance_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The site ID. Valid values:
        # 
        # *   **26842**: the China site (aliyun.com)
        # *   **26888**: the international site (alibabacloud.com)
        self.bid = bid
        # The edition of the cluster. Valid values:
        # 
        # *   **Basic**: Single-replica Edition
        # *   **HighAvailability**: Double-replica Edition
        self.category = category
        # The commodity code of the cluster.
        self.commodity_code = commodity_code
        # The VPC endpoint of the cluster.
        self.connection_string = connection_string
        # The version number of the backend management system of ApsaraDB for ClickHouse. Valid values:
        # 
        # *   **v1**
        # *   **v2**
        self.control_version = control_version
        # The time when the cluster was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.create_time = create_time
        # The description of the cluster.
        self.dbcluster_description = dbcluster_description
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The network type of the cluster. Only VPC is supported.
        self.dbcluster_network_type = dbcluster_network_type
        # The state of the cluster. Valid values:
        # 
        # *   **Preparing**: The cluster is being prepared.
        # *   **Creating**: The cluster is being created.
        # *   **Running**: The cluster is running.
        # *   **Deleting**: The cluster is being deleted.
        # *   **SCALING_OUT**: The storage capacity of the cluster is being expanded.
        self.dbcluster_status = dbcluster_status
        # The specifications of the cluster.
        # 
        # *   Valid values when the cluster is of Single-replica Edition: -**S4**: 4 CPU cores and 16 GB of memory -**S8**: 8 CPU cores and 32 GB of memory
        # 
        #     *   **S16**: 16 CPU cores and 64 GB of memory
        #     *   **S32**: 32 CPU cores and 128 GB of memory
        #     *   **S64**: 64 CPU cores and 256 GB of memory
        #     *   **S104**: 104 CPU cores and 384 GB of memory
        # 
        # *   Valid values when the cluster is of Double-replica Edition: -**C4**: 4 CPU cores and 16 GB of memory -**C8**: 8 CPU cores and 32 GB of memory -**C16**: 16 CPU cores and 64 GB of memory -**C32**: 32 CPU cores and 128 GB of memory -**C64**: 64 CPU cores and 256 GB of memory -**C104**: 104 CPU cores and 384 GB of memory
        self.dbnode_class = dbnode_class
        # The number of nodes.
        # 
        # *   Valid values when the cluster is of Single-replica Edition: 1 to 48.
        # *   Valid values when the cluster is of Double-replica Edition: 1 to 24.
        self.dbnode_count = dbnode_count
        # The storage capacity of each node. Valid values: 100 to 32000. Unit: GB.
        # 
        # >  This value is a multiple of 100.
        self.dbnode_storage = dbnode_storage
        # The engine version of the cluster.
        self.db_version = db_version
        # The time when the cluster expired. The time is in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # >  Pay-as-you-go clusters never expire. If the cluster is a pay-as-you-go cluster, an empty string is returned for this parameter.
        self.expire_time = expire_time
        # The extended storage space.
        self.ext_storage_size = ext_storage_size
        # The extended storage type. Valid values:
        # 
        # *   **CloudSSD**: standard SSD.
        # *   **CloudESSD**: The cluster uses an enhanced SSD (ESSD) of performance level (PL) 1.
        # *   **CloudESSD_PL2**: The cluster uses an ESSD of PL 2.
        # *   **CloudESSD_PL3**: The cluster uses an ESSD of PL 3.
        # *   **CloudEfficiency**: The cluster uses an ultra disk.
        self.ext_storage_type = ext_storage_type
        # Indicates whether the cluster has expired. Valid values:
        # 
        # *   **true**: The cluster has expired.
        # *   **false**: The cluster has not expired.
        self.is_expired = is_expired
        # The lock mode of the cluster. Valid values:
        # 
        # *   **Unlock**: The cluster is not locked.
        # *   **ManualLock**: The cluster is manually locked.
        # *   **LockByExpiration**: The cluster is automatically locked due to cluster expiration.
        # *   **LockByRestoration**: The cluster is automatically locked because the cluster is about to be rolled back.
        # *   **LockByDiskQuota**: The cluster is automatically locked because the disk space is exhausted.
        self.lock_mode = lock_mode
        # The cause why the cluster was locked.
        # 
        # >  If the value of the LockMode parameter is Unlock, an empty string is returned for this parameter.
        self.lock_reason = lock_reason
        # The billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: The cluster uses the pay-as-you-go billing method.
        # *   **Prepaid**: The cluster uses the subscription billing method.
        self.pay_type = pay_type
        # The HTTP port number.
        self.port = port
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group to which the cluster belongs.
        self.resource_group_id = resource_group_id
        # The time window during which write operations are stopped for specification changes.
        self.scale_out_disable_write_windows = scale_out_disable_write_windows
        # The status of a data migration task.
        self.scale_out_status = scale_out_status
        # The storage type of the cluster. Valid values:
        # 
        # *   **CloudESSD**: The cluster uses an enhanced SSD (ESSD) of performance level (PL) 1.
        # *   **CloudESSD_PL2**: The cluster uses an ESSD of PL 2.
        # *   **CloudESSD_PL3**: The cluster uses an ESSD of PL 3.
        # *   **CloudEfficiency**: The cluster uses an ultra disk.
        self.storage_type = storage_type
        # The tags.
        self.tags = tags
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the VPC in which the cluster is deployed.
        self.vpc_cloud_instance_id = vpc_cloud_instance_id
        # The ID of the virtual private cloud (VPC) in which the cluster is deployed.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.scale_out_status:
            self.scale_out_status.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.bid is not None:
            result['Bid'] = self.bid

        if self.category is not None:
            result['Category'] = self.category

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.control_version is not None:
            result['ControlVersion'] = self.control_version

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

        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count

        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage

        if self.db_version is not None:
            result['DbVersion'] = self.db_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.ext_storage_size is not None:
            result['ExtStorageSize'] = self.ext_storage_size

        if self.ext_storage_type is not None:
            result['ExtStorageType'] = self.ext_storage_type

        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scale_out_disable_write_windows is not None:
            result['ScaleOutDisableWriteWindows'] = self.scale_out_disable_write_windows

        if self.scale_out_status is not None:
            result['ScaleOutStatus'] = self.scale_out_status.to_map()

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('ControlVersion') is not None:
            self.control_version = m.get('ControlVersion')

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

        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')

        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')

        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExtStorageSize') is not None:
            self.ext_storage_size = m.get('ExtStorageSize')

        if m.get('ExtStorageType') is not None:
            self.ext_storage_type = m.get('ExtStorageType')

        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScaleOutDisableWriteWindows') is not None:
            self.scale_out_disable_write_windows = m.get('ScaleOutDisableWriteWindows')

        if m.get('ScaleOutStatus') is not None:
            temp_model = main_models.DescribeDBClustersResponseBodyDBClustersDBClusterScaleOutStatus()
            self.scale_out_status = temp_model.from_map(m.get('ScaleOutStatus'))

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDBClustersResponseBodyDBClustersDBClusterTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBClustersResponseBodyDBClustersDBClusterTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeDBClustersResponseBodyDBClustersDBClusterTagsTag] = None,
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
                temp_model = main_models.DescribeDBClustersResponseBodyDBClustersDBClusterTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDBClustersResponseBodyDBClustersDBClusterTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag name.
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

class DescribeDBClustersResponseBodyDBClustersDBClusterScaleOutStatus(DaraModel):
    def __init__(
        self,
        progress: str = None,
        ratio: str = None,
    ):
        # The progress of the data migration task in percentage.
        # 
        # >  This parameter is returned only when the cluster is in the SCALING_OUT state.
        self.progress = progress
        # The progress of the data migration task. This value is displayed in the following format: Data volume that has been migrated/Total data volume.
        # 
        # >  This parameter is returned only when the cluster is in the SCALING_OUT state.
        self.ratio = ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.progress is not None:
            result['Progress'] = self.progress

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        return self

