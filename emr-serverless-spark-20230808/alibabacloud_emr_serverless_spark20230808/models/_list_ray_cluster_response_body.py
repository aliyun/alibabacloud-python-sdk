# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListRayClusterResponseBody(DaraModel):
    def __init__(
        self,
        ray_clusters: List[main_models.ListRayClusterResponseBodyRayClusters] = None,
        request_id: str = None,
    ):
        self.ray_clusters = ray_clusters
        self.request_id = request_id

    def validate(self):
        if self.ray_clusters:
            for v1 in self.ray_clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['rayClusters'] = []
        if self.ray_clusters is not None:
            for k1 in self.ray_clusters:
                result['rayClusters'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ray_clusters = []
        if m.get('rayClusters') is not None:
            for k1 in m.get('rayClusters'):
                temp_model = main_models.ListRayClusterResponseBodyRayClusters()
                self.ray_clusters.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListRayClusterResponseBodyRayClusters(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        create_time: int = None,
        creator: str = None,
        creator_name: str = None,
        dashboard_url: str = None,
        description: str = None,
        display_release_version: str = None,
        grpc_endpoint: str = None,
        head_spec: main_models.ListRayClusterResponseBodyRayClustersHeadSpec = None,
        instance_id: str = None,
        message: str = None,
        modified: bool = None,
        modified_time: int = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        network_service_name: str = None,
        start_time: int = None,
        state: str = None,
        user_id: str = None,
        worker_spec: List[main_models.ListRayClusterResponseBodyRayClustersWorkerSpec] = None,
    ):
        self.cluster_id = cluster_id
        self.create_time = create_time
        self.creator = creator
        self.creator_name = creator_name
        self.dashboard_url = dashboard_url
        self.description = description
        self.display_release_version = display_release_version
        self.grpc_endpoint = grpc_endpoint
        self.head_spec = head_spec
        self.instance_id = instance_id
        self.message = message
        self.modified = modified
        self.modified_time = modified_time
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.name = name
        self.network_service_name = network_service_name
        self.start_time = start_time
        self.state = state
        self.user_id = user_id
        self.worker_spec = worker_spec

    def validate(self):
        if self.head_spec:
            self.head_spec.validate()
        if self.worker_spec:
            for v1 in self.worker_spec:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator is not None:
            result['creator'] = self.creator

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.dashboard_url is not None:
            result['dashboardUrl'] = self.dashboard_url

        if self.description is not None:
            result['description'] = self.description

        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version

        if self.grpc_endpoint is not None:
            result['grpcEndpoint'] = self.grpc_endpoint

        if self.head_spec is not None:
            result['headSpec'] = self.head_spec.to_map()

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.message is not None:
            result['message'] = self.message

        if self.modified is not None:
            result['modified'] = self.modified

        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name

        if self.name is not None:
            result['name'] = self.name

        if self.network_service_name is not None:
            result['networkServiceName'] = self.network_service_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.state is not None:
            result['state'] = self.state

        if self.user_id is not None:
            result['userId'] = self.user_id

        result['workerSpec'] = []
        if self.worker_spec is not None:
            for k1 in self.worker_spec:
                result['workerSpec'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('dashboardUrl') is not None:
            self.dashboard_url = m.get('dashboardUrl')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')

        if m.get('grpcEndpoint') is not None:
            self.grpc_endpoint = m.get('grpcEndpoint')

        if m.get('headSpec') is not None:
            temp_model = main_models.ListRayClusterResponseBodyRayClustersHeadSpec()
            self.head_spec = temp_model.from_map(m.get('headSpec'))

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('modified') is not None:
            self.modified = m.get('modified')

        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkServiceName') is not None:
            self.network_service_name = m.get('networkServiceName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        self.worker_spec = []
        if m.get('workerSpec') is not None:
            for k1 in m.get('workerSpec'):
                temp_model = main_models.ListRayClusterResponseBodyRayClustersWorkerSpec()
                self.worker_spec.append(temp_model.from_map(k1))

        return self

class ListRayClusterResponseBodyRayClustersWorkerSpec(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        gpu_spec: str = None,
        group_name: str = None,
        max_replica: int = None,
        memory: str = None,
        min_replica: int = None,
        queue_name: str = None,
        replica: int = None,
        worker_type: str = None,
    ):
        self.cpu = cpu
        self.gpu_spec = gpu_spec
        self.group_name = group_name
        self.max_replica = max_replica
        self.memory = memory
        self.min_replica = min_replica
        self.queue_name = queue_name
        self.replica = replica
        self.worker_type = worker_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.gpu_spec is not None:
            result['gpuSpec'] = self.gpu_spec

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.max_replica is not None:
            result['maxReplica'] = self.max_replica

        if self.memory is not None:
            result['memory'] = self.memory

        if self.min_replica is not None:
            result['minReplica'] = self.min_replica

        if self.queue_name is not None:
            result['queueName'] = self.queue_name

        if self.replica is not None:
            result['replica'] = self.replica

        if self.worker_type is not None:
            result['workerType'] = self.worker_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('gpuSpec') is not None:
            self.gpu_spec = m.get('gpuSpec')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('maxReplica') is not None:
            self.max_replica = m.get('maxReplica')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('minReplica') is not None:
            self.min_replica = m.get('minReplica')

        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')

        if m.get('replica') is not None:
            self.replica = m.get('replica')

        if m.get('workerType') is not None:
            self.worker_type = m.get('workerType')

        return self

class ListRayClusterResponseBodyRayClustersHeadSpec(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        enable_auto_scaling: bool = None,
        gpu_spec: str = None,
        idle_timeout_seconds: int = None,
        memory: str = None,
        queue_name: str = None,
        replica: int = None,
    ):
        self.cpu = cpu
        self.enable_auto_scaling = enable_auto_scaling
        self.gpu_spec = gpu_spec
        self.idle_timeout_seconds = idle_timeout_seconds
        self.memory = memory
        self.queue_name = queue_name
        self.replica = replica

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.enable_auto_scaling is not None:
            result['enableAutoScaling'] = self.enable_auto_scaling

        if self.gpu_spec is not None:
            result['gpuSpec'] = self.gpu_spec

        if self.idle_timeout_seconds is not None:
            result['idleTimeoutSeconds'] = self.idle_timeout_seconds

        if self.memory is not None:
            result['memory'] = self.memory

        if self.queue_name is not None:
            result['queueName'] = self.queue_name

        if self.replica is not None:
            result['replica'] = self.replica

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('enableAutoScaling') is not None:
            self.enable_auto_scaling = m.get('enableAutoScaling')

        if m.get('gpuSpec') is not None:
            self.gpu_spec = m.get('gpuSpec')

        if m.get('idleTimeoutSeconds') is not None:
            self.idle_timeout_seconds = m.get('idleTimeoutSeconds')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')

        if m.get('replica') is not None:
            self.replica = m.get('replica')

        return self

