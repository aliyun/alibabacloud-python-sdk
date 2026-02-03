# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterMemberInfoResponseBody(DaraModel):
    def __init__(
        self,
        cluster_children: List[main_models.DescribeClusterMemberInfoResponseBodyClusterChildren] = None,
        request_id: str = None,
    ):
        # Details about data nodes in the cluster instance.
        self.cluster_children = cluster_children
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cluster_children:
            for v1 in self.cluster_children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterChildren'] = []
        if self.cluster_children is not None:
            for k1 in self.cluster_children:
                result['ClusterChildren'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_children = []
        if m.get('ClusterChildren') is not None:
            for k1 in m.get('ClusterChildren'):
                temp_model = main_models.DescribeClusterMemberInfoResponseBodyClusterChildren()
                self.cluster_children.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClusterMemberInfoResponseBodyClusterChildren(DaraModel):
    def __init__(
        self,
        band_width: int = None,
        binlog_retention_days: int = None,
        biz_type: str = None,
        capacity: int = None,
        class_code: str = None,
        connections: int = None,
        current_band_width: int = None,
        disk_size_mb: int = None,
        id: int = None,
        name: str = None,
        replica_size: int = None,
        resource_group_name: str = None,
        service: str = None,
        service_version: str = None,
        user_id: str = None,
    ):
        # The maximum bandwidth of the node. Unit: MB/s.
        # 
        # > This parameter is returned only if the return value of **Service** is **redis**, which indicates a data node.
        self.band_width = band_width
        # The retention period of binlogs.
        self.binlog_retention_days = binlog_retention_days
        # The type of workload. The return value is **ALIYUN**.
        self.biz_type = biz_type
        # The maximum memory capacity per data node. Unit: MB.
        # 
        # > This parameter is returned only if the return value of **Service** is **redis**, which indicates a data node.
        self.capacity = capacity
        # The specifications of the data node. For more information, see [Community Edition instances that use cloud disks](https://help.aliyun.com/document_detail/164477.html).
        self.class_code = class_code
        # The maximum number of connections supported by the data node.
        self.connections = connections
        # The current bandwidth of the data node, which is the sum of the default bandwidth and any extra bandwidth that is purchased. Unit: Mbit/s.
        self.current_band_width = current_band_width
        # The storage capacity of the [enhanced SSD (ESSD)](https://help.aliyun.com/document_detail/122389.html) that is used by the data node. Unit: MB.
        # 
        # > The ESSD is used only to store system operating data, such as Persistent Memory (PMEM). It is not used as a medium to write and read data.
        self.disk_size_mb = disk_size_mb
        # The ID of the replica set in the node.
        self.id = id
        # The name of the data node.
        self.name = name
        # The number of replica nodes.
        self.replica_size = replica_size
        # The name of the resource group to which the node belongs.
        self.resource_group_name = resource_group_name
        # The node type. Valid values:
        # 
        # *   **redis**: data node
        # *   **redis_cs**: config server
        self.service = service
        # The major version of the node.
        self.service_version = service_version
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.band_width is not None:
            result['BandWidth'] = self.band_width

        if self.binlog_retention_days is not None:
            result['BinlogRetentionDays'] = self.binlog_retention_days

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.connections is not None:
            result['Connections'] = self.connections

        if self.current_band_width is not None:
            result['CurrentBandWidth'] = self.current_band_width

        if self.disk_size_mb is not None:
            result['DiskSizeMB'] = self.disk_size_mb

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.replica_size is not None:
            result['ReplicaSize'] = self.replica_size

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.service is not None:
            result['Service'] = self.service

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')

        if m.get('BinlogRetentionDays') is not None:
            self.binlog_retention_days = m.get('BinlogRetentionDays')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('Connections') is not None:
            self.connections = m.get('Connections')

        if m.get('CurrentBandWidth') is not None:
            self.current_band_width = m.get('CurrentBandWidth')

        if m.get('DiskSizeMB') is not None:
            self.disk_size_mb = m.get('DiskSizeMB')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ReplicaSize') is not None:
            self.replica_size = m.get('ReplicaSize')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

