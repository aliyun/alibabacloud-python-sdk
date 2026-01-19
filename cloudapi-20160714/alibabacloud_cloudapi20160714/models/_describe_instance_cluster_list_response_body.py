# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceClusterListResponseBody(DaraModel):
    def __init__(
        self,
        instance_clusters: main_models.DescribeInstanceClusterListResponseBodyInstanceClusters = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The instance cluster list.
        self.instance_clusters = instance_clusters
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instance_clusters:
            self.instance_clusters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_clusters is not None:
            result['InstanceClusters'] = self.instance_clusters.to_map()

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
        if m.get('InstanceClusters') is not None:
            temp_model = main_models.DescribeInstanceClusterListResponseBodyInstanceClusters()
            self.instance_clusters = temp_model.from_map(m.get('InstanceClusters'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceClusterListResponseBodyInstanceClusters(DaraModel):
    def __init__(
        self,
        instance_cluster: List[main_models.DescribeInstanceClusterListResponseBodyInstanceClustersInstanceCluster] = None,
    ):
        self.instance_cluster = instance_cluster

    def validate(self):
        if self.instance_cluster:
            for v1 in self.instance_cluster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceCluster'] = []
        if self.instance_cluster is not None:
            for k1 in self.instance_cluster:
                result['InstanceCluster'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_cluster = []
        if m.get('InstanceCluster') is not None:
            for k1 in m.get('InstanceCluster'):
                temp_model = main_models.DescribeInstanceClusterListResponseBodyInstanceClustersInstanceCluster()
                self.instance_cluster.append(temp_model.from_map(k1))

        return self

class DescribeInstanceClusterListResponseBodyInstanceClustersInstanceCluster(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        instance_cluster_id: str = None,
        instance_cluster_name: str = None,
        instance_cluster_status: str = None,
        instance_cluster_type: str = None,
        modified_time: str = None,
        region_id: str = None,
    ):
        # The time when the cluster was created. The time is displayed in UTC.
        self.created_time = created_time
        # The cluster description.
        self.description = description
        # The cluster ID.
        self.instance_cluster_id = instance_cluster_id
        # The cluster name.
        self.instance_cluster_name = instance_cluster_name
        # The cluster status.
        self.instance_cluster_status = instance_cluster_status
        # The cluster type.
        self.instance_cluster_type = instance_cluster_type
        # The time when the cluster was last modified. The time is displayed in UTC.
        self.modified_time = modified_time
        # The region ID of the cluster.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_cluster_id is not None:
            result['InstanceClusterId'] = self.instance_cluster_id

        if self.instance_cluster_name is not None:
            result['InstanceClusterName'] = self.instance_cluster_name

        if self.instance_cluster_status is not None:
            result['InstanceClusterStatus'] = self.instance_cluster_status

        if self.instance_cluster_type is not None:
            result['InstanceClusterType'] = self.instance_cluster_type

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceClusterId') is not None:
            self.instance_cluster_id = m.get('InstanceClusterId')

        if m.get('InstanceClusterName') is not None:
            self.instance_cluster_name = m.get('InstanceClusterName')

        if m.get('InstanceClusterStatus') is not None:
            self.instance_cluster_status = m.get('InstanceClusterStatus')

        if m.get('InstanceClusterType') is not None:
            self.instance_cluster_type = m.get('InstanceClusterType')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

