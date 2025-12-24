# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeHpcClustersResponseBody(DaraModel):
    def __init__(
        self,
        hpc_clusters: main_models.DescribeHpcClustersResponseBodyHpcClusters = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The name of the HPC cluster.
        self.hpc_clusters = hpc_clusters
        # Details about the HPC clusters. The value is an array that consists of the information of each HPC cluster.
        self.page_number = page_number
        # The page number.
        self.page_size = page_size
        # The total number of HPC clusters.
        self.request_id = request_id
        # The ID of the HPC cluster.
        self.total_count = total_count

    def validate(self):
        if self.hpc_clusters:
            self.hpc_clusters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hpc_clusters is not None:
            result['HpcClusters'] = self.hpc_clusters.to_map()

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
        if m.get('HpcClusters') is not None:
            temp_model = main_models.DescribeHpcClustersResponseBodyHpcClusters()
            self.hpc_clusters = temp_model.from_map(m.get('HpcClusters'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHpcClustersResponseBodyHpcClusters(DaraModel):
    def __init__(
        self,
        hpc_cluster: List[main_models.DescribeHpcClustersResponseBodyHpcClustersHpcCluster] = None,
    ):
        self.hpc_cluster = hpc_cluster

    def validate(self):
        if self.hpc_cluster:
            for v1 in self.hpc_cluster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HpcCluster'] = []
        if self.hpc_cluster is not None:
            for k1 in self.hpc_cluster:
                result['HpcCluster'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hpc_cluster = []
        if m.get('HpcCluster') is not None:
            for k1 in m.get('HpcCluster'):
                temp_model = main_models.DescribeHpcClustersResponseBodyHpcClustersHpcCluster()
                self.hpc_cluster.append(temp_model.from_map(k1))

        return self

class DescribeHpcClustersResponseBodyHpcClustersHpcCluster(DaraModel):
    def __init__(
        self,
        description: str = None,
        hpc_cluster_id: str = None,
        name: str = None,
    ):
        # The description of the HPC cluster.
        self.description = description
        # The description of the HPC cluster.
        self.hpc_cluster_id = hpc_cluster_id
        # The name of the HPC cluster.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

