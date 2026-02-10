# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeContainerGroupedFieldDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeContainerGroupedFieldDetailResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeContainerGroupedFieldDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeContainerGroupedFieldDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        alarm_count: int = None,
        app_name: str = None,
        cluster_current_version: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_state: str = None,
        cluster_type: str = None,
        container_count: int = None,
        create_time: int = None,
        instance_count: int = None,
        namespace: str = None,
        node_name: str = None,
        pod: str = None,
        pod_count: int = None,
        pod_ip: str = None,
        region_id: str = None,
        vul_count: int = None,
    ):
        # The number of alerts.
        self.alarm_count = alarm_count
        # The name of the application.
        self.app_name = app_name
        # The version of the current online server in the cluster.
        self.cluster_current_version = cluster_current_version
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The status of the cluster. Valid values:
        # 
        # *   STARTING: The cluster is being started.
        # *   START_FAILED: The cluster fails to be started.
        # *   BOOTSTRAPPING: The bootstrap action is being performed for the cluster.
        # *   RUNNING: The cluster is running.
        # *   TERMINATING: The cluster is being terminated.
        # *   TERMINATED: The cluster is terminated.
        # *   TERMINATED_WITH_ERRORS: The cluster is terminated due to an exception.
        # *   TERMINATE_FAILED: The cluster fails to be terminated.
        self.cluster_state = cluster_state
        # The type of the cluster. Valid values:
        # 
        # *   **Kubernetes**: dedicated Kubernetes cluster.
        # *   **ManagedKubernetes**: standard managed cluster (edge cluster).
        # *   **Ask**: serverless Kubernetes (ASK) cluster.
        self.cluster_type = cluster_type
        # The number of containers.
        self.container_count = container_count
        # The creation time.
        self.create_time = create_time
        # The number of instances.
        self.instance_count = instance_count
        # The namespace.
        self.namespace = namespace
        # The name of the node.
        self.node_name = node_name
        # The name of the pod.
        self.pod = pod
        # The number of pods.
        self.pod_count = pod_count
        # The IP address of the pod.
        self.pod_ip = pod_ip
        # The ID of the region.
        self.region_id = region_id
        # The number of vulnerabilities.
        self.vul_count = vul_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_count is not None:
            result['AlarmCount'] = self.alarm_count

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_current_version is not None:
            result['ClusterCurrentVersion'] = self.cluster_current_version

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.container_count is not None:
            result['ContainerCount'] = self.container_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.pod_count is not None:
            result['PodCount'] = self.pod_count

        if self.pod_ip is not None:
            result['PodIp'] = self.pod_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmCount') is not None:
            self.alarm_count = m.get('AlarmCount')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterCurrentVersion') is not None:
            self.cluster_current_version = m.get('ClusterCurrentVersion')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterState') is not None:
            self.cluster_state = m.get('ClusterState')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('ContainerCount') is not None:
            self.container_count = m.get('ContainerCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('PodCount') is not None:
            self.pod_count = m.get('PodCount')

        if m.get('PodIp') is not None:
            self.pod_ip = m.get('PodIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        return self

