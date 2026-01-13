# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class CreateLivyComputeRequest(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        auto_start_configuration: main_models.CreateLivyComputeRequestAutoStartConfiguration = None,
        auto_stop_configuration: main_models.CreateLivyComputeRequestAutoStopConfiguration = None,
        cpu_limit: str = None,
        display_release_version: str = None,
        enable_public: bool = None,
        environment_id: str = None,
        fusion: bool = None,
        livy_server_conf: str = None,
        livy_version: str = None,
        memory_limit: str = None,
        name: str = None,
        network_name: str = None,
        queue_name: str = None,
        release_version: str = None,
        region_id: str = None,
    ):
        self.auth_type = auth_type
        self.auto_start_configuration = auto_start_configuration
        self.auto_stop_configuration = auto_stop_configuration
        self.cpu_limit = cpu_limit
        self.display_release_version = display_release_version
        self.enable_public = enable_public
        self.environment_id = environment_id
        self.fusion = fusion
        self.livy_server_conf = livy_server_conf
        self.livy_version = livy_version
        self.memory_limit = memory_limit
        self.name = name
        self.network_name = network_name
        self.queue_name = queue_name
        self.release_version = release_version
        self.region_id = region_id

    def validate(self):
        if self.auto_start_configuration:
            self.auto_start_configuration.validate()
        if self.auto_stop_configuration:
            self.auto_stop_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['authType'] = self.auth_type

        if self.auto_start_configuration is not None:
            result['autoStartConfiguration'] = self.auto_start_configuration.to_map()

        if self.auto_stop_configuration is not None:
            result['autoStopConfiguration'] = self.auto_stop_configuration.to_map()

        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit

        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version

        if self.enable_public is not None:
            result['enablePublic'] = self.enable_public

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.fusion is not None:
            result['fusion'] = self.fusion

        if self.livy_server_conf is not None:
            result['livyServerConf'] = self.livy_server_conf

        if self.livy_version is not None:
            result['livyVersion'] = self.livy_version

        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit

        if self.name is not None:
            result['name'] = self.name

        if self.network_name is not None:
            result['networkName'] = self.network_name

        if self.queue_name is not None:
            result['queueName'] = self.queue_name

        if self.release_version is not None:
            result['releaseVersion'] = self.release_version

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('autoStartConfiguration') is not None:
            temp_model = main_models.CreateLivyComputeRequestAutoStartConfiguration()
            self.auto_start_configuration = temp_model.from_map(m.get('autoStartConfiguration'))

        if m.get('autoStopConfiguration') is not None:
            temp_model = main_models.CreateLivyComputeRequestAutoStopConfiguration()
            self.auto_stop_configuration = temp_model.from_map(m.get('autoStopConfiguration'))

        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')

        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')

        if m.get('enablePublic') is not None:
            self.enable_public = m.get('enablePublic')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')

        if m.get('livyServerConf') is not None:
            self.livy_server_conf = m.get('livyServerConf')

        if m.get('livyVersion') is not None:
            self.livy_version = m.get('livyVersion')

        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkName') is not None:
            self.network_name = m.get('networkName')

        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')

        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class CreateLivyComputeRequestAutoStopConfiguration(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        idle_timeout_minutes: int = None,
    ):
        self.enable = enable
        self.idle_timeout_minutes = idle_timeout_minutes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.idle_timeout_minutes is not None:
            result['idleTimeoutMinutes'] = self.idle_timeout_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('idleTimeoutMinutes') is not None:
            self.idle_timeout_minutes = m.get('idleTimeoutMinutes')

        return self

class CreateLivyComputeRequestAutoStartConfiguration(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        return self

