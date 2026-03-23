# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class GetRayClusterResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        create_time: int = None,
        creator: str = None,
        creator_name: str = None,
        dashboard_url: str = None,
        description: str = None,
        display_release_version: str = None,
        extra_param: str = None,
        grpc_endpoint: str = None,
        head_spec: main_models.GetRayClusterResponseBodyHeadSpec = None,
        instance_id: str = None,
        instances: List[main_models.GetRayClusterResponseBodyInstances] = None,
        job_url: str = None,
        job_url_inner: str = None,
        message: str = None,
        modified: bool = None,
        modified_time: int = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        network_service_name: str = None,
        request_id: str = None,
        start_time: int = None,
        state: str = None,
        submit_token: str = None,
        user_id: str = None,
        volume_ids: List[str] = None,
        worker_spec: List[main_models.GetRayClusterResponseBodyWorkerSpec] = None,
    ):
        self.cluster_id = cluster_id
        self.create_time = create_time
        self.creator = creator
        self.creator_name = creator_name
        self.dashboard_url = dashboard_url
        self.description = description
        self.display_release_version = display_release_version
        self.extra_param = extra_param
        self.grpc_endpoint = grpc_endpoint
        self.head_spec = head_spec
        self.instance_id = instance_id
        self.instances = instances
        self.job_url = job_url
        self.job_url_inner = job_url_inner
        self.message = message
        self.modified = modified
        self.modified_time = modified_time
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.name = name
        self.network_service_name = network_service_name
        self.request_id = request_id
        self.start_time = start_time
        self.state = state
        self.submit_token = submit_token
        self.user_id = user_id
        self.volume_ids = volume_ids
        self.worker_spec = worker_spec

    def validate(self):
        if self.head_spec:
            self.head_spec.validate()
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()
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

        if self.extra_param is not None:
            result['extraParam'] = self.extra_param

        if self.grpc_endpoint is not None:
            result['grpcEndpoint'] = self.grpc_endpoint

        if self.head_spec is not None:
            result['headSpec'] = self.head_spec.to_map()

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        result['instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['instances'].append(k1.to_map() if k1 else None)

        if self.job_url is not None:
            result['jobUrl'] = self.job_url

        if self.job_url_inner is not None:
            result['jobUrlInner'] = self.job_url_inner

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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.state is not None:
            result['state'] = self.state

        if self.submit_token is not None:
            result['submitToken'] = self.submit_token

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.volume_ids is not None:
            result['volumeIds'] = self.volume_ids

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

        if m.get('extraParam') is not None:
            self.extra_param = m.get('extraParam')

        if m.get('grpcEndpoint') is not None:
            self.grpc_endpoint = m.get('grpcEndpoint')

        if m.get('headSpec') is not None:
            temp_model = main_models.GetRayClusterResponseBodyHeadSpec()
            self.head_spec = temp_model.from_map(m.get('headSpec'))

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        self.instances = []
        if m.get('instances') is not None:
            for k1 in m.get('instances'):
                temp_model = main_models.GetRayClusterResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('jobUrl') is not None:
            self.job_url = m.get('jobUrl')

        if m.get('jobUrlInner') is not None:
            self.job_url_inner = m.get('jobUrlInner')

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

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('submitToken') is not None:
            self.submit_token = m.get('submitToken')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('volumeIds') is not None:
            self.volume_ids = m.get('volumeIds')

        self.worker_spec = []
        if m.get('workerSpec') is not None:
            for k1 in m.get('workerSpec'):
                temp_model = main_models.GetRayClusterResponseBodyWorkerSpec()
                self.worker_spec.append(temp_model.from_map(k1))

        return self

class GetRayClusterResponseBodyWorkerSpec(DaraModel):
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

class GetRayClusterResponseBodyInstances(DaraModel):
    def __init__(
        self,
        container_exit_code: int = None,
        container_state: str = None,
        container_state_message: str = None,
        container_state_reason: str = None,
        create_time: int = None,
        instance_id: str = None,
        message: str = None,
        phase: str = None,
        reason: str = None,
        start_time: int = None,
        type: str = None,
    ):
        self.container_exit_code = container_exit_code
        self.container_state = container_state
        self.container_state_message = container_state_message
        self.container_state_reason = container_state_reason
        self.create_time = create_time
        self.instance_id = instance_id
        self.message = message
        self.phase = phase
        self.reason = reason
        self.start_time = start_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_exit_code is not None:
            result['containerExitCode'] = self.container_exit_code

        if self.container_state is not None:
            result['containerState'] = self.container_state

        if self.container_state_message is not None:
            result['containerStateMessage'] = self.container_state_message

        if self.container_state_reason is not None:
            result['containerStateReason'] = self.container_state_reason

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.message is not None:
            result['message'] = self.message

        if self.phase is not None:
            result['phase'] = self.phase

        if self.reason is not None:
            result['reason'] = self.reason

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containerExitCode') is not None:
            self.container_exit_code = m.get('containerExitCode')

        if m.get('containerState') is not None:
            self.container_state = m.get('containerState')

        if m.get('containerStateMessage') is not None:
            self.container_state_message = m.get('containerStateMessage')

        if m.get('containerStateReason') is not None:
            self.container_state_reason = m.get('containerStateReason')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('phase') is not None:
            self.phase = m.get('phase')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetRayClusterResponseBodyHeadSpec(DaraModel):
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

