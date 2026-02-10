# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterInfoListResponseBody(DaraModel):
    def __init__(
        self,
        cluster_list: List[main_models.DescribeClusterInfoListResponseBodyClusterList] = None,
        request_id: str = None,
    ):
        # An array that consists of the information about clusters.
        self.cluster_list = cluster_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.cluster_list:
            for v1 in self.cluster_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterList'] = []
        if self.cluster_list is not None:
            for k1 in self.cluster_list:
                result['ClusterList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_list = []
        if m.get('ClusterList') is not None:
            for k1 in m.get('ClusterList'):
                temp_model = main_models.DescribeClusterInfoListResponseBodyClusterList()
                self.cluster_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClusterInfoListResponseBodyClusterList(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        region_id: str = None,
        state: str = None,
        target_result: bool = None,
    ):
        # The ID of the container cluster.
        self.cluster_id = cluster_id
        # The name of the container cluster.
        self.cluster_name = cluster_name
        # The type of the cluster. Valid values:
        # 
        # *   **ManagedKubernetes**: managed Kubernetes cluster.
        # *   **NotManagedKubernetes**: non-managed Kubernetes cluster.
        # *   **PrivateKubernetes**: private cluster.
        # *   **kubernetes**: dedicated Kubernetes cluster.
        # *   **ask**: dedicated serverless Kubernetes (ASK) cluster.
        self.cluster_type = cluster_type
        # The region in which the cluster resides.
        self.region_id = region_id
        # The status of the cluster. Valid values:
        # 
        # *   **unavailable**: The cluster is unavailable.
        # *   **Available**: The cluster is available.
        # *   **Creating**: The cluster is being created.
        # *   **CreateFailed**: The cluster failed to be created.
        self.state = state
        # Indicates whether container network topology was enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.target_result = target_result

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

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.state is not None:
            result['State'] = self.state

        if self.target_result is not None:
            result['TargetResult'] = self.target_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TargetResult') is not None:
            self.target_result = m.get('TargetResult')

        return self

