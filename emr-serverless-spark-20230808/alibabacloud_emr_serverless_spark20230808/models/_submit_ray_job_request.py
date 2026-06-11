# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class SubmitRayJobRequest(DaraModel):
    def __init__(
        self,
        active_deadline_seconds: int = None,
        display_release_version: str = None,
        entrypoint: str = None,
        entrypoint_memory: str = None,
        entrypoint_num_cpus: str = None,
        entrypoint_num_gpus: str = None,
        entrypoint_resources: str = None,
        extra_param: str = None,
        head_spec: main_models.SubmitRayJobRequestHeadSpec = None,
        metadata_json: str = None,
        name: str = None,
        network_service_name: str = None,
        runtime_env_json: str = None,
        shutdown_after_job_finishes: bool = None,
        submission_mode: str = None,
        tags: List[main_models.SubmitRayJobRequestTags] = None,
        ttl_seconds_after_finished: int = None,
        volume_ids: List[str] = None,
        worker_spec: List[main_models.SubmitRayJobRequestWorkerSpec] = None,
        working_dir: str = None,
    ):
        self.active_deadline_seconds = active_deadline_seconds
        self.display_release_version = display_release_version
        self.entrypoint = entrypoint
        self.entrypoint_memory = entrypoint_memory
        self.entrypoint_num_cpus = entrypoint_num_cpus
        self.entrypoint_num_gpus = entrypoint_num_gpus
        self.entrypoint_resources = entrypoint_resources
        self.extra_param = extra_param
        self.head_spec = head_spec
        self.metadata_json = metadata_json
        self.name = name
        self.network_service_name = network_service_name
        self.runtime_env_json = runtime_env_json
        self.shutdown_after_job_finishes = shutdown_after_job_finishes
        self.submission_mode = submission_mode
        self.tags = tags
        self.ttl_seconds_after_finished = ttl_seconds_after_finished
        self.volume_ids = volume_ids
        self.worker_spec = worker_spec
        self.working_dir = working_dir

    def validate(self):
        if self.head_spec:
            self.head_spec.validate()
        if self.tags:
            for v1 in self.tags:
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
        if self.active_deadline_seconds is not None:
            result['activeDeadlineSeconds'] = self.active_deadline_seconds

        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version

        if self.entrypoint is not None:
            result['entrypoint'] = self.entrypoint

        if self.entrypoint_memory is not None:
            result['entrypointMemory'] = self.entrypoint_memory

        if self.entrypoint_num_cpus is not None:
            result['entrypointNumCpus'] = self.entrypoint_num_cpus

        if self.entrypoint_num_gpus is not None:
            result['entrypointNumGpus'] = self.entrypoint_num_gpus

        if self.entrypoint_resources is not None:
            result['entrypointResources'] = self.entrypoint_resources

        if self.extra_param is not None:
            result['extraParam'] = self.extra_param

        if self.head_spec is not None:
            result['headSpec'] = self.head_spec.to_map()

        if self.metadata_json is not None:
            result['metadataJson'] = self.metadata_json

        if self.name is not None:
            result['name'] = self.name

        if self.network_service_name is not None:
            result['networkServiceName'] = self.network_service_name

        if self.runtime_env_json is not None:
            result['runtimeEnvJson'] = self.runtime_env_json

        if self.shutdown_after_job_finishes is not None:
            result['shutdownAfterJobFinishes'] = self.shutdown_after_job_finishes

        if self.submission_mode is not None:
            result['submissionMode'] = self.submission_mode

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.ttl_seconds_after_finished is not None:
            result['ttlSecondsAfterFinished'] = self.ttl_seconds_after_finished

        if self.volume_ids is not None:
            result['volumeIds'] = self.volume_ids

        result['workerSpec'] = []
        if self.worker_spec is not None:
            for k1 in self.worker_spec:
                result['workerSpec'].append(k1.to_map() if k1 else None)

        if self.working_dir is not None:
            result['workingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeDeadlineSeconds') is not None:
            self.active_deadline_seconds = m.get('activeDeadlineSeconds')

        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')

        if m.get('entrypoint') is not None:
            self.entrypoint = m.get('entrypoint')

        if m.get('entrypointMemory') is not None:
            self.entrypoint_memory = m.get('entrypointMemory')

        if m.get('entrypointNumCpus') is not None:
            self.entrypoint_num_cpus = m.get('entrypointNumCpus')

        if m.get('entrypointNumGpus') is not None:
            self.entrypoint_num_gpus = m.get('entrypointNumGpus')

        if m.get('entrypointResources') is not None:
            self.entrypoint_resources = m.get('entrypointResources')

        if m.get('extraParam') is not None:
            self.extra_param = m.get('extraParam')

        if m.get('headSpec') is not None:
            temp_model = main_models.SubmitRayJobRequestHeadSpec()
            self.head_spec = temp_model.from_map(m.get('headSpec'))

        if m.get('metadataJson') is not None:
            self.metadata_json = m.get('metadataJson')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkServiceName') is not None:
            self.network_service_name = m.get('networkServiceName')

        if m.get('runtimeEnvJson') is not None:
            self.runtime_env_json = m.get('runtimeEnvJson')

        if m.get('shutdownAfterJobFinishes') is not None:
            self.shutdown_after_job_finishes = m.get('shutdownAfterJobFinishes')

        if m.get('submissionMode') is not None:
            self.submission_mode = m.get('submissionMode')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.SubmitRayJobRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('ttlSecondsAfterFinished') is not None:
            self.ttl_seconds_after_finished = m.get('ttlSecondsAfterFinished')

        if m.get('volumeIds') is not None:
            self.volume_ids = m.get('volumeIds')

        self.worker_spec = []
        if m.get('workerSpec') is not None:
            for k1 in m.get('workerSpec'):
                temp_model = main_models.SubmitRayJobRequestWorkerSpec()
                self.worker_spec.append(temp_model.from_map(k1))

        if m.get('workingDir') is not None:
            self.working_dir = m.get('workingDir')

        return self

class SubmitRayJobRequestWorkerSpec(DaraModel):
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

class SubmitRayJobRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class SubmitRayJobRequestHeadSpec(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        enable_auto_scaling: bool = None,
        gpu_spec: str = None,
        idle_timeout_seconds: int = None,
        memory: str = None,
        queue_name: str = None,
    ):
        self.cpu = cpu
        self.enable_auto_scaling = enable_auto_scaling
        self.gpu_spec = gpu_spec
        self.idle_timeout_seconds = idle_timeout_seconds
        self.memory = memory
        self.queue_name = queue_name

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

        return self

