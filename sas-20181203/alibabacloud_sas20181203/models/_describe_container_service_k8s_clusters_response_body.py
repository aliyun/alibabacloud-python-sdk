# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeContainerServiceK8sClustersResponseBody(DaraModel):
    def __init__(
        self,
        k_8s_clusters: List[main_models.DescribeContainerServiceK8sClustersResponseBodyK8sClusters] = None,
        request_id: str = None,
    ):
        # The information about the clusters.
        self.k_8s_clusters = k_8s_clusters
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.k_8s_clusters:
            for v1 in self.k_8s_clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['K8sClusters'] = []
        if self.k_8s_clusters is not None:
            for k1 in self.k_8s_clusters:
                result['K8sClusters'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.k_8s_clusters = []
        if m.get('K8sClusters') is not None:
            for k1 in m.get('K8sClusters'):
                temp_model = main_models.DescribeContainerServiceK8sClustersResponseBodyK8sClusters()
                self.k_8s_clusters.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeContainerServiceK8sClustersResponseBodyK8sClusters(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        name: str = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

