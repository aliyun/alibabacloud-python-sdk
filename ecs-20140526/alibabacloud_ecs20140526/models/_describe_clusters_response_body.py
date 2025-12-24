# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeClustersResponseBody(DaraModel):
    def __init__(
        self,
        clusters: main_models.DescribeClustersResponseBodyClusters = None,
        request_id: str = None,
    ):
        self.clusters = clusters
        self.request_id = request_id

    def validate(self):
        if self.clusters:
            self.clusters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clusters') is not None:
            temp_model = main_models.DescribeClustersResponseBodyClusters()
            self.clusters = temp_model.from_map(m.get('Clusters'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClustersResponseBodyClusters(DaraModel):
    def __init__(
        self,
        cluster: List[main_models.DescribeClustersResponseBodyClustersCluster] = None,
    ):
        self.cluster = cluster

    def validate(self):
        if self.cluster:
            for v1 in self.cluster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cluster'] = []
        if self.cluster is not None:
            for k1 in self.cluster:
                result['Cluster'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster = []
        if m.get('Cluster') is not None:
            for k1 in m.get('Cluster'):
                temp_model = main_models.DescribeClustersResponseBodyClustersCluster()
                self.cluster.append(temp_model.from_map(k1))

        return self

class DescribeClustersResponseBodyClustersCluster(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        return self

