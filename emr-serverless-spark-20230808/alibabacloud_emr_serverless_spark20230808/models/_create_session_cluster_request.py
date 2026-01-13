# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class CreateSessionClusterRequest(DaraModel):
    def __init__(
        self,
        application_configs: List[main_models.CreateSessionClusterRequestApplicationConfigs] = None,
        auto_start_configuration: main_models.CreateSessionClusterRequestAutoStartConfiguration = None,
        auto_stop_configuration: main_models.CreateSessionClusterRequestAutoStopConfiguration = None,
        client_token: str = None,
        display_release_version: str = None,
        env_id: str = None,
        fusion: bool = None,
        kind: str = None,
        name: str = None,
        public_endpoint_enabled: bool = None,
        queue_name: str = None,
        release_version: str = None,
        region_id: str = None,
    ):
        # The Spark configurations.
        self.application_configs = application_configs
        # Specifies whether to enable automatic startup.
        # 
        # *   true
        # *   false
        self.auto_start_configuration = auto_start_configuration
        # The automatic termination configuration.
        self.auto_stop_configuration = auto_stop_configuration
        self.client_token = client_token
        # The version of the Spark engine.
        self.display_release_version = display_release_version
        # The ID of the Python environment. This parameter takes effect only for notebook sessions.
        self.env_id = env_id
        # Specifies whether to enable Fusion engine for acceleration.
        self.fusion = fusion
        # The session type.
        # 
        # *   SQL
        # *   NOTEBOOK
        self.kind = kind
        # The name of the job.
        self.name = name
        self.public_endpoint_enabled = public_endpoint_enabled
        # The queue name.
        self.queue_name = queue_name
        # The version number of Spark.
        self.release_version = release_version
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.application_configs:
            for v1 in self.application_configs:
                 if v1:
                    v1.validate()
        if self.auto_start_configuration:
            self.auto_start_configuration.validate()
        if self.auto_stop_configuration:
            self.auto_stop_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['applicationConfigs'] = []
        if self.application_configs is not None:
            for k1 in self.application_configs:
                result['applicationConfigs'].append(k1.to_map() if k1 else None)

        if self.auto_start_configuration is not None:
            result['autoStartConfiguration'] = self.auto_start_configuration.to_map()

        if self.auto_stop_configuration is not None:
            result['autoStopConfiguration'] = self.auto_stop_configuration.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version

        if self.env_id is not None:
            result['envId'] = self.env_id

        if self.fusion is not None:
            result['fusion'] = self.fusion

        if self.kind is not None:
            result['kind'] = self.kind

        if self.name is not None:
            result['name'] = self.name

        if self.public_endpoint_enabled is not None:
            result['publicEndpointEnabled'] = self.public_endpoint_enabled

        if self.queue_name is not None:
            result['queueName'] = self.queue_name

        if self.release_version is not None:
            result['releaseVersion'] = self.release_version

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_configs = []
        if m.get('applicationConfigs') is not None:
            for k1 in m.get('applicationConfigs'):
                temp_model = main_models.CreateSessionClusterRequestApplicationConfigs()
                self.application_configs.append(temp_model.from_map(k1))

        if m.get('autoStartConfiguration') is not None:
            temp_model = main_models.CreateSessionClusterRequestAutoStartConfiguration()
            self.auto_start_configuration = temp_model.from_map(m.get('autoStartConfiguration'))

        if m.get('autoStopConfiguration') is not None:
            temp_model = main_models.CreateSessionClusterRequestAutoStopConfiguration()
            self.auto_stop_configuration = temp_model.from_map(m.get('autoStopConfiguration'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')

        if m.get('envId') is not None:
            self.env_id = m.get('envId')

        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('publicEndpointEnabled') is not None:
            self.public_endpoint_enabled = m.get('publicEndpointEnabled')

        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')

        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class CreateSessionClusterRequestAutoStopConfiguration(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        idle_timeout_minutes: int = None,
    ):
        # Specifies whether to enable automatic termination.
        # 
        # *   true
        # *   false
        self.enable = enable
        # The idle timeout period. The session is automatically terminated when the idle timeout period is exceeded.
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

class CreateSessionClusterRequestAutoStartConfiguration(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Specifies whether to enable automatic startup.
        # 
        # *   true
        # *   false
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

class CreateSessionClusterRequestApplicationConfigs(DaraModel):
    def __init__(
        self,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        # The name of the configuration file.
        self.config_file_name = config_file_name
        # The key of SparkConf.
        self.config_item_key = config_item_key
        # The value of SparkConf.
        self.config_item_value = config_item_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_file_name is not None:
            result['configFileName'] = self.config_file_name

        if self.config_item_key is not None:
            result['configItemKey'] = self.config_item_key

        if self.config_item_value is not None:
            result['configItemValue'] = self.config_item_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configFileName') is not None:
            self.config_file_name = m.get('configFileName')

        if m.get('configItemKey') is not None:
            self.config_item_key = m.get('configItemKey')

        if m.get('configItemValue') is not None:
            self.config_item_value = m.get('configItemValue')

        return self

