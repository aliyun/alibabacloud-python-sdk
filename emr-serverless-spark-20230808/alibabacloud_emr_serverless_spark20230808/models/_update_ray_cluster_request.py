# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class UpdateRayClusterRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_release_version: str = None,
        extra_param: str = None,
        head_spec: main_models.UpdateRayClusterRequestHeadSpec = None,
        name: str = None,
        network_service_name: str = None,
        volume_ids: List[str] = None,
        worker_spec: List[main_models.UpdateRayClusterRequestWorkerSpec] = None,
    ):
        # The description.
        self.description = description
        # The Ray DPI engine version.
        self.display_release_version = display_release_version
        # The extra parameters. The value must be in JSON format.
        self.extra_param = extra_param
        # The Ray cluster head node information.
        self.head_spec = head_spec
        # The Ray cluster name. The name must be 1 to 64 characters in length.
        self.name = name
        # The network connectivity name.
        self.network_service_name = network_service_name
        # The list of managed folder IDs to mount.
        self.volume_ids = volume_ids
        # The Ray cluster worker node information. A maximum of 50 groups are supported.
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
        if self.description is not None:
            result['description'] = self.description

        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version

        if self.extra_param is not None:
            result['extraParam'] = self.extra_param

        if self.head_spec is not None:
            result['headSpec'] = self.head_spec.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.network_service_name is not None:
            result['networkServiceName'] = self.network_service_name

        if self.volume_ids is not None:
            result['volumeIds'] = self.volume_ids

        result['workerSpec'] = []
        if self.worker_spec is not None:
            for k1 in self.worker_spec:
                result['workerSpec'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')

        if m.get('extraParam') is not None:
            self.extra_param = m.get('extraParam')

        if m.get('headSpec') is not None:
            temp_model = main_models.UpdateRayClusterRequestHeadSpec()
            self.head_spec = temp_model.from_map(m.get('headSpec'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkServiceName') is not None:
            self.network_service_name = m.get('networkServiceName')

        if m.get('volumeIds') is not None:
            self.volume_ids = m.get('volumeIds')

        self.worker_spec = []
        if m.get('workerSpec') is not None:
            for k1 in m.get('workerSpec'):
                temp_model = main_models.UpdateRayClusterRequestWorkerSpec()
                self.worker_spec.append(temp_model.from_map(k1))

        return self

class UpdateRayClusterRequestWorkerSpec(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        display_release_version: str = None,
        env: str = None,
        gpu_spec: str = None,
        group_name: str = None,
        max_replica: int = None,
        memory: str = None,
        min_replica: int = None,
        queue_name: str = None,
        ray_start_params: str = None,
        replica: int = None,
        worker_type: str = None,
    ):
        # The number of CPU cores.
        self.cpu = cpu
        # The DPI engine version.
        self.display_release_version = display_release_version
        # The Ray environment variables.
        self.env = env
        # The GPU instance type.
        self.gpu_spec = gpu_spec
        # The worker group name.
        self.group_name = group_name
        # The maximum number of workers. Minimum value: 1.
        self.max_replica = max_replica
        # The memory size. Unit: GiB.
        self.memory = memory
        # The minimum number of workers. Minimum value: 1. The value must be less than or equal to maxReplica.
        self.min_replica = min_replica
        # The queue name.
        self.queue_name = queue_name
        # The Ray startup parameters.
        self.ray_start_params = ray_start_params
        # The number of workers. Minimum value: 1.
        self.replica = replica
        # The worker type.
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

        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version

        if self.env is not None:
            result['env'] = self.env

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

        if self.ray_start_params is not None:
            result['rayStartParams'] = self.ray_start_params

        if self.replica is not None:
            result['replica'] = self.replica

        if self.worker_type is not None:
            result['workerType'] = self.worker_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')

        if m.get('env') is not None:
            self.env = m.get('env')

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

        if m.get('rayStartParams') is not None:
            self.ray_start_params = m.get('rayStartParams')

        if m.get('replica') is not None:
            self.replica = m.get('replica')

        if m.get('workerType') is not None:
            self.worker_type = m.get('workerType')

        return self

class UpdateRayClusterRequestHeadSpec(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        display_release_version: str = None,
        enable_auto_scaling: bool = None,
        env: str = None,
        gft_config: main_models.UpdateRayClusterRequestHeadSpecGftConfig = None,
        gft_enabled: bool = None,
        gpu_spec: str = None,
        idle_timeout_seconds: int = None,
        memory: str = None,
        queue_name: str = None,
        ray_start_params: str = None,
    ):
        # The number of CPU cores.
        self.cpu = cpu
        # The Ray DPI engine version.
        self.display_release_version = display_release_version
        # Specifies whether to enable automatic scaling.
        self.enable_auto_scaling = enable_auto_scaling
        # The environment variables.
        self.env = env
        # The GCS Fault Tolerance configuration.
        self.gft_config = gft_config
        # Specifies whether to enable GCS Fault Tolerance.
        self.gft_enabled = gft_enabled
        # The GPU instance type.
        self.gpu_spec = gpu_spec
        # The idle timeout period of workers after automatic scaling is enabled.
        self.idle_timeout_seconds = idle_timeout_seconds
        # The memory size. Unit: GiB.
        self.memory = memory
        # The queue name.
        self.queue_name = queue_name
        # The Ray startup parameters.
        self.ray_start_params = ray_start_params

    def validate(self):
        if self.gft_config:
            self.gft_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version

        if self.enable_auto_scaling is not None:
            result['enableAutoScaling'] = self.enable_auto_scaling

        if self.env is not None:
            result['env'] = self.env

        if self.gft_config is not None:
            result['gftConfig'] = self.gft_config.to_map()

        if self.gft_enabled is not None:
            result['gftEnabled'] = self.gft_enabled

        if self.gpu_spec is not None:
            result['gpuSpec'] = self.gpu_spec

        if self.idle_timeout_seconds is not None:
            result['idleTimeoutSeconds'] = self.idle_timeout_seconds

        if self.memory is not None:
            result['memory'] = self.memory

        if self.queue_name is not None:
            result['queueName'] = self.queue_name

        if self.ray_start_params is not None:
            result['rayStartParams'] = self.ray_start_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')

        if m.get('enableAutoScaling') is not None:
            self.enable_auto_scaling = m.get('enableAutoScaling')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('gftConfig') is not None:
            temp_model = main_models.UpdateRayClusterRequestHeadSpecGftConfig()
            self.gft_config = temp_model.from_map(m.get('gftConfig'))

        if m.get('gftEnabled') is not None:
            self.gft_enabled = m.get('gftEnabled')

        if m.get('gpuSpec') is not None:
            self.gpu_spec = m.get('gpuSpec')

        if m.get('idleTimeoutSeconds') is not None:
            self.idle_timeout_seconds = m.get('idleTimeoutSeconds')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')

        if m.get('rayStartParams') is not None:
            self.ray_start_params = m.get('rayStartParams')

        return self

class UpdateRayClusterRequestHeadSpecGftConfig(DaraModel):
    def __init__(
        self,
        redis_password: str = None,
        redis_url: str = None,
        redis_username: str = None,
    ):
        # The Redis password.
        self.redis_password = redis_password
        # The Redis address.
        self.redis_url = redis_url
        # The Redis username.
        self.redis_username = redis_username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.redis_password is not None:
            result['redisPassword'] = self.redis_password

        if self.redis_url is not None:
            result['redisUrl'] = self.redis_url

        if self.redis_username is not None:
            result['redisUsername'] = self.redis_username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('redisPassword') is not None:
            self.redis_password = m.get('redisPassword')

        if m.get('redisUrl') is not None:
            self.redis_url = m.get('redisUrl')

        if m.get('redisUsername') is not None:
            self.redis_username = m.get('redisUsername')

        return self

