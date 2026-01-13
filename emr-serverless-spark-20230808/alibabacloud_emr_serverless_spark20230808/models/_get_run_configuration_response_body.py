# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class GetRunConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        run_configuration: main_models.GetRunConfigurationResponseBodyRunConfiguration = None,
    ):
        # 请求ID。
        self.request_id = request_id
        self.run_configuration = run_configuration

    def validate(self):
        if self.run_configuration:
            self.run_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.run_configuration is not None:
            result['runConfiguration'] = self.run_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('runConfiguration') is not None:
            temp_model = main_models.GetRunConfigurationResponseBodyRunConfiguration()
            self.run_configuration = temp_model.from_map(m.get('runConfiguration'))

        return self

class GetRunConfigurationResponseBodyRunConfiguration(DaraModel):
    def __init__(
        self,
        application_configs: List[main_models.GetRunConfigurationResponseBodyRunConfigurationApplicationConfigs] = None,
        log_config: main_models.GetRunConfigurationResponseBodyRunConfigurationLogConfig = None,
        runtime_configs: List[main_models.Tag] = None,
    ):
        # 应用配置项
        self.application_configs = application_configs
        self.log_config = log_config
        # 运行配置。
        self.runtime_configs = runtime_configs

    def validate(self):
        if self.application_configs:
            for v1 in self.application_configs:
                 if v1:
                    v1.validate()
        if self.log_config:
            self.log_config.validate()
        if self.runtime_configs:
            for v1 in self.runtime_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['applicationConfigs'] = []
        if self.application_configs is not None:
            for k1 in self.application_configs:
                result['applicationConfigs'].append(k1.to_map() if k1 else None)

        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()

        result['runtimeConfigs'] = []
        if self.runtime_configs is not None:
            for k1 in self.runtime_configs:
                result['runtimeConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_configs = []
        if m.get('applicationConfigs') is not None:
            for k1 in m.get('applicationConfigs'):
                temp_model = main_models.GetRunConfigurationResponseBodyRunConfigurationApplicationConfigs()
                self.application_configs.append(temp_model.from_map(k1))

        if m.get('logConfig') is not None:
            temp_model = main_models.GetRunConfigurationResponseBodyRunConfigurationLogConfig()
            self.log_config = temp_model.from_map(m.get('logConfig'))

        self.runtime_configs = []
        if m.get('runtimeConfigs') is not None:
            for k1 in m.get('runtimeConfigs'):
                temp_model = main_models.Tag()
                self.runtime_configs.append(temp_model.from_map(k1))

        return self

class GetRunConfigurationResponseBodyRunConfigurationLogConfig(DaraModel):
    def __init__(
        self,
        log_level: str = None,
        log_path: str = None,
    ):
        self.log_level = log_level
        self.log_path = log_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_level is not None:
            result['LogLevel'] = self.log_level

        if self.log_path is not None:
            result['LogPath'] = self.log_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')

        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')

        return self

class GetRunConfigurationResponseBodyRunConfigurationApplicationConfigs(DaraModel):
    def __init__(
        self,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        # 应用配置文件名。 应用配置文件名。 ```spark-defaults.conf```
        self.config_file_name = config_file_name
        # 配置项键。 配置项键。 ```dfs.namenode.checkpoint.period```
        self.config_item_key = config_item_key
        # 配置项值。 配置项值。 ```3600s```
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

