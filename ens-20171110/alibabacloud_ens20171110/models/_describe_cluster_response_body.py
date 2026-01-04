# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterResponseBody(DaraModel):
    def __init__(
        self,
        clusters: List[main_models.DescribeClusterResponseBodyClusters] = None,
        request_id: str = None,
    ):
        # An array that consists of the information about clusters.
        self.clusters = clusters
        # The ID of the request.
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
                temp_model = main_models.DescribeClusterResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClusterResponseBodyClusters(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        current_version: str = None,
        name: str = None,
        next_version: str = None,
        status: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The version of the cluster.
        self.current_version = current_version
        # The cluster name.
        self.name = name
        # The next version of the cluster.
        self.next_version = next_version
        # The health status of the instance.
        # 
        # Valid values:
        # 
        # *   healthy
        # *   unhealthy
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.name is not None:
            result['Name'] = self.name

        if self.next_version is not None:
            result['NextVersion'] = self.next_version

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextVersion') is not None:
            self.next_version = m.get('NextVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

