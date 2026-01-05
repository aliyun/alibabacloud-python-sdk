# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClustersWithBackupsResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBClustersWithBackupsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The details about the cluster.
        self.items = items
        # The total number of returned pages.
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
            temp_model = main_models.DescribeDBClustersWithBackupsResponseBodyItems()
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

class DescribeDBClustersWithBackupsResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbcluster: List[main_models.DescribeDBClustersWithBackupsResponseBodyItemsDBCluster] = None,
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
                temp_model = main_models.DescribeDBClustersWithBackupsResponseBodyItemsDBCluster()
                self.dbcluster.append(temp_model.from_map(k1))

        return self

class DescribeDBClustersWithBackupsResponseBodyItemsDBCluster(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_network_type: str = None,
        dbcluster_status: str = None,
        dbnode_class: str = None,
        dbtype: str = None,
        dbversion: str = None,
        deleted_time: str = None,
        deletion_lock: int = None,
        engine: str = None,
        expire_time: str = None,
        expired: str = None,
        is_deleted: int = None,
        lock_mode: str = None,
        pay_type: str = None,
        region_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The time when the cluster was created.
        self.create_time = create_time
        # The name of the cluster.
        self.dbcluster_description = dbcluster_description
        # The ID of cluster.
        self.dbcluster_id = dbcluster_id
        # The network type of the cluster.
        self.dbcluster_network_type = dbcluster_network_type
        # The status of the cluster. Valid values:
        # 
        # *   Creating: The cluster is being created.
        # *   Running: The cluster is running.
        # *   Deleting: The cluster is being released.
        # *   Rebooting: The cluster is restarting.
        # *   DBNodeCreating: The node is being added.
        # *   DBNodeDeleting: The node is being deleted.
        # *   ClassChanging: The specifications of the node are being changed.
        # *   NetAddressCreating: The network connection is being created.
        # *   NetAddressDeleting: The network connection is being deleted.
        # *   NetAddressModifying: The network connection is being modified.
        # *   Deleted: The cluster has been released.
        self.dbcluster_status = dbcluster_status
        # The specifications of the node.
        self.dbnode_class = dbnode_class
        # The type of the database engine.
        self.dbtype = dbtype
        # The version of the database engine.
        self.dbversion = dbversion
        # The time when the cluster was deleted.
        self.deleted_time = deleted_time
        # Indicates whether the cluster is locked and can be deleted. Valid values:
        # 
        # *   **0**: The cluster is not locked and can be deleted.
        # *   **1**: The cluster is locked and cannot be deleted.
        self.deletion_lock = deletion_lock
        # The type of the database engine.
        self.engine = engine
        # The time when the cluster expires.
        # 
        # > A specific value will be returned only for subscription clusters. For pay-as-you-go clusters, an empty string will be returned.
        self.expire_time = expire_time
        # Indicates whether the cluster has expired.
        # 
        # > A specific value will be returned only for subscription clusters.
        self.expired = expired
        # Indicates whether the cluster was released. Valid values:
        # 
        # *   1: released
        # *   0: not released
        self.is_deleted = is_deleted
        # The state of the cluster lock. Valid values:
        # 
        # *   **Unlock**: The cluster is not locked.
        # *   **ManualLock**: The cluster is manually locked.
        # *   **LockByExpiration**: The cluster is automatically locked after the cluster expires.
        self.lock_mode = lock_mode
        # The billing method. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription
        self.pay_type = pay_type
        # The region ID of the cluster.
        self.region_id = region_id
        # The VPC ID of the cluster.
        self.vpc_id = vpc_id
        # The ID of the zone in which the instance is located.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time

        if self.deletion_lock is not None:
            result['DeletionLock'] = self.deletion_lock

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')

        if m.get('DeletionLock') is not None:
            self.deletion_lock = m.get('DeletionLock')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

