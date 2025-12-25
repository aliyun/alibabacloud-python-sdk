# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCClustersResponseBody(DaraModel):
    def __init__(
        self,
        clusters: List[main_models.DescribeRCClustersResponseBodyClusters] = None,
        request_id: str = None,
    ):
        # The information about the clusters.
        self.clusters = clusters
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.clusters:
            for v1 in self.clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Clusters'] = []
        if self.clusters is not None:
            for k1 in self.clusters:
                result['Clusters'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k1 in m.get('Clusters'):
                temp_model = main_models.DescribeRCClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRCClustersResponseBodyClusters(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        create_time: str = None,
        profile: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The time when the cluster was created.
        self.create_time = create_time
        self.profile = profile
        # The cluster status. Valid values:
        # 
        # *   **Pending**
        # *   **Running**
        # *   **Starting**
        # *   **Stopping**
        # *   **Stopped**
        self.status = status
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

