# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterBasicInfoResponseBody(DaraModel):
    def __init__(
        self,
        cluster_info: main_models.DescribeClusterBasicInfoResponseBodyClusterInfo = None,
        request_id: str = None,
    ):
        # The detailed information about the cluster.
        self.cluster_info = cluster_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.cluster_info:
            self.cluster_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterInfo') is not None:
            temp_model = main_models.DescribeClusterBasicInfoResponseBodyClusterInfo()
            self.cluster_info = temp_model.from_map(m.get('ClusterInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClusterBasicInfoResponseBodyClusterInfo(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        create_time: int = None,
        current_version: str = None,
        instance_count: int = None,
        region_id: str = None,
        state: str = None,
        target_result: bool = None,
    ):
        # The ID of cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The type of the cluster. Valid values:
        # 
        # *   **ManagedKubernetes**: managed Kubernetes cluster
        # *   **NotManagedKubernetes**: non-managed Kubernetes cluster
        # *   **PrivateKubernetes**: private cluster
        # *   **kubernetes**: dedicated Kubernetes cluster
        # *   **ask**: dedicated ASK cluster
        self.cluster_type = cluster_type
        # The timestamp when the cluster was created. Unit: milliseconds.
        self.create_time = create_time
        # The version of the cluster.
        self.current_version = current_version
        # The number of instances in the cluster.
        self.instance_count = instance_count
        # The ID of the region in which the cluster is deployed.
        self.region_id = region_id
        # The status of the cluster. Valid values:
        # 
        # *   **unavailable**
        # *   **Available**
        # *   **Creating**
        # *   **CreateFailed**
        self.state = state
        # Indicates whether the cluster is enabled. Valid values:
        # 
        # *   **true**: The cluster is enabled.
        # *   **false**: The cluster is disabled.
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

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

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TargetResult') is not None:
            self.target_result = m.get('TargetResult')

        return self

