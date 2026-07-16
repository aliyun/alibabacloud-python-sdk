# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class GetRayJobResponseBody(DaraModel):
    def __init__(
        self,
        active_deadline_seconds: int = None,
        backoff_limit: int = None,
        cluster_state: str = None,
        creator_name: str = None,
        cu_hours: float = None,
        dashboard_url: str = None,
        dashboard_url_extra: List[str] = None,
        display_release_version: str = None,
        duration: int = None,
        end_time: int = None,
        entrypoint: str = None,
        entrypoint_memory: str = None,
        entrypoint_num_cpus: str = None,
        entrypoint_num_gpus: str = None,
        entrypoint_resources: str = None,
        extra_param: str = None,
        gu_hours: main_models.GetRayJobResponseBodyGuHours = None,
        head_spec: main_models.GetRayJobResponseBodyHeadSpec = None,
        log_bucket_name: str = None,
        log_path: str = None,
        message: str = None,
        metadata_json: str = None,
        name: str = None,
        network_service_name: str = None,
        request_id: str = None,
        runtime_env_json: str = None,
        shutdown_after_job_finishes: bool = None,
        start_time: int = None,
        status: str = None,
        submission_id: str = None,
        submission_mode: str = None,
        submit_time: int = None,
        tags: List[main_models.Tag] = None,
        task_biz_id: str = None,
        ttl_seconds_after_finished: int = None,
        volume_ids: List[str] = None,
        worker_specs: List[main_models.GetRayJobResponseBodyWorkerSpecs] = None,
        working_dir: str = None,
    ):
        self.active_deadline_seconds = active_deadline_seconds
        self.backoff_limit = backoff_limit
        self.cluster_state = cluster_state
        self.creator_name = creator_name
        self.cu_hours = cu_hours
        self.dashboard_url = dashboard_url
        self.dashboard_url_extra = dashboard_url_extra
        self.display_release_version = display_release_version
        self.duration = duration
        self.end_time = end_time
        self.entrypoint = entrypoint
        self.entrypoint_memory = entrypoint_memory
        self.entrypoint_num_cpus = entrypoint_num_cpus
        self.entrypoint_num_gpus = entrypoint_num_gpus
        self.entrypoint_resources = entrypoint_resources
        self.extra_param = extra_param
        self.gu_hours = gu_hours
        self.head_spec = head_spec
        self.log_bucket_name = log_bucket_name
        self.log_path = log_path
        self.message = message
        self.metadata_json = metadata_json
        self.name = name
        self.network_service_name = network_service_name
        self.request_id = request_id
        self.runtime_env_json = runtime_env_json
        self.shutdown_after_job_finishes = shutdown_after_job_finishes
        self.start_time = start_time
        self.status = status
        self.submission_id = submission_id
        self.submission_mode = submission_mode
        self.submit_time = submit_time
        self.tags = tags
        self.task_biz_id = task_biz_id
        self.ttl_seconds_after_finished = ttl_seconds_after_finished
        self.volume_ids = volume_ids
        self.worker_specs = worker_specs
        self.working_dir = working_dir

    def validate(self):
        if self.gu_hours:
            self.gu_hours.validate()
        if self.head_spec:
            self.head_spec.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.worker_specs:
            for v1 in self.worker_specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_deadline_seconds is not None:
            result['activeDeadlineSeconds'] = self.active_deadline_seconds

        if self.backoff_limit is not None:
            result['backoffLimit'] = self.backoff_limit

        if self.cluster_state is not None:
            result['clusterState'] = self.cluster_state

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.cu_hours is not None:
            result['cuHours'] = self.cu_hours

        if self.dashboard_url is not None:
            result['dashboardUrl'] = self.dashboard_url

        if self.dashboard_url_extra is not None:
            result['dashboardUrlExtra'] = self.dashboard_url_extra

        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version

        if self.duration is not None:
            result['duration'] = self.duration

        if self.end_time is not None:
            result['endTime'] = self.end_time

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

        if self.gu_hours is not None:
            result['guHours'] = self.gu_hours.to_map()

        if self.head_spec is not None:
            result['headSpec'] = self.head_spec.to_map()

        if self.log_bucket_name is not None:
            result['logBucketName'] = self.log_bucket_name

        if self.log_path is not None:
            result['logPath'] = self.log_path

        if self.message is not None:
            result['message'] = self.message

        if self.metadata_json is not None:
            result['metadataJson'] = self.metadata_json

        if self.name is not None:
            result['name'] = self.name

        if self.network_service_name is not None:
            result['networkServiceName'] = self.network_service_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.runtime_env_json is not None:
            result['runtimeEnvJson'] = self.runtime_env_json

        if self.shutdown_after_job_finishes is not None:
            result['shutdownAfterJobFinishes'] = self.shutdown_after_job_finishes

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.submission_id is not None:
            result['submissionId'] = self.submission_id

        if self.submission_mode is not None:
            result['submissionMode'] = self.submission_mode

        if self.submit_time is not None:
            result['submitTime'] = self.submit_time

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.task_biz_id is not None:
            result['taskBizId'] = self.task_biz_id

        if self.ttl_seconds_after_finished is not None:
            result['ttlSecondsAfterFinished'] = self.ttl_seconds_after_finished

        if self.volume_ids is not None:
            result['volumeIds'] = self.volume_ids

        result['workerSpecs'] = []
        if self.worker_specs is not None:
            for k1 in self.worker_specs:
                result['workerSpecs'].append(k1.to_map() if k1 else None)

        if self.working_dir is not None:
            result['workingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeDeadlineSeconds') is not None:
            self.active_deadline_seconds = m.get('activeDeadlineSeconds')

        if m.get('backoffLimit') is not None:
            self.backoff_limit = m.get('backoffLimit')

        if m.get('clusterState') is not None:
            self.cluster_state = m.get('clusterState')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('cuHours') is not None:
            self.cu_hours = m.get('cuHours')

        if m.get('dashboardUrl') is not None:
            self.dashboard_url = m.get('dashboardUrl')

        if m.get('dashboardUrlExtra') is not None:
            self.dashboard_url_extra = m.get('dashboardUrlExtra')

        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

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

        if m.get('guHours') is not None:
            temp_model = main_models.GetRayJobResponseBodyGuHours()
            self.gu_hours = temp_model.from_map(m.get('guHours'))

        if m.get('headSpec') is not None:
            temp_model = main_models.GetRayJobResponseBodyHeadSpec()
            self.head_spec = temp_model.from_map(m.get('headSpec'))

        if m.get('logBucketName') is not None:
            self.log_bucket_name = m.get('logBucketName')

        if m.get('logPath') is not None:
            self.log_path = m.get('logPath')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('metadataJson') is not None:
            self.metadata_json = m.get('metadataJson')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkServiceName') is not None:
            self.network_service_name = m.get('networkServiceName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('runtimeEnvJson') is not None:
            self.runtime_env_json = m.get('runtimeEnvJson')

        if m.get('shutdownAfterJobFinishes') is not None:
            self.shutdown_after_job_finishes = m.get('shutdownAfterJobFinishes')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('submissionId') is not None:
            self.submission_id = m.get('submissionId')

        if m.get('submissionMode') is not None:
            self.submission_mode = m.get('submissionMode')

        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('taskBizId') is not None:
            self.task_biz_id = m.get('taskBizId')

        if m.get('ttlSecondsAfterFinished') is not None:
            self.ttl_seconds_after_finished = m.get('ttlSecondsAfterFinished')

        if m.get('volumeIds') is not None:
            self.volume_ids = m.get('volumeIds')

        self.worker_specs = []
        if m.get('workerSpecs') is not None:
            for k1 in m.get('workerSpecs'):
                temp_model = main_models.GetRayJobResponseBodyWorkerSpecs()
                self.worker_specs.append(temp_model.from_map(k1))

        if m.get('workingDir') is not None:
            self.working_dir = m.get('workingDir')

        return self

class GetRayJobResponseBodyWorkerSpecs(DaraModel):
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
    ):
        self.cpu = cpu
        self.gpu_spec = gpu_spec
        self.group_name = group_name
        self.max_replica = max_replica
        self.memory = memory
        self.min_replica = min_replica
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

        return self

class GetRayJobResponseBodyHeadSpec(DaraModel):
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

class GetRayJobResponseBodyGuHours(DaraModel):
    def __init__(
        self,
        gpu_hours: float = None,
        gpu_spec: str = None,
    ):
        self.gpu_hours = gpu_hours
        self.gpu_spec = gpu_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gpu_hours is not None:
            result['gpuHours'] = self.gpu_hours

        if self.gpu_spec is not None:
            result['gpuSpec'] = self.gpu_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gpuHours') is not None:
            self.gpu_hours = m.get('gpuHours')

        if m.get('gpuSpec') is not None:
            self.gpu_spec = m.get('gpuSpec')

        return self

