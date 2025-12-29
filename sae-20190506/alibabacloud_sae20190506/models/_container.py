# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class Container(DaraModel):
    def __init__(
        self,
        args: str = None,
        command: str = None,
        environment_variables: Dict[str, str] = None,
        image: str = None,
        image_registry_config: main_models.ImageRegistryConfig = None,
        metrics_collect_config: main_models.MetricsCollectConfig = None,
        port: int = None,
        request_concurrency: int = None,
        request_timeout: int = None,
        resources: main_models.ContainerResources = None,
        slscollect_configs: main_models.SLSCollectConfigs = None,
        startup_probe: main_models.StartupProbe = None,
        web_nasconfig: main_models.WebNASConfig = None,
        web_ossconfig: main_models.WebOSSConfig = None,
    ):
        self.args = args
        self.command = command
        self.environment_variables = environment_variables
        # This parameter is required.
        self.image = image
        self.image_registry_config = image_registry_config
        self.metrics_collect_config = metrics_collect_config
        self.port = port
        self.request_concurrency = request_concurrency
        self.request_timeout = request_timeout
        # This parameter is required.
        self.resources = resources
        self.slscollect_configs = slscollect_configs
        self.startup_probe = startup_probe
        self.web_nasconfig = web_nasconfig
        self.web_ossconfig = web_ossconfig

    def validate(self):
        if self.image_registry_config:
            self.image_registry_config.validate()
        if self.metrics_collect_config:
            self.metrics_collect_config.validate()
        if self.resources:
            self.resources.validate()
        if self.slscollect_configs:
            self.slscollect_configs.validate()
        if self.startup_probe:
            self.startup_probe.validate()
        if self.web_nasconfig:
            self.web_nasconfig.validate()
        if self.web_ossconfig:
            self.web_ossconfig.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.command is not None:
            result['Command'] = self.command

        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables

        if self.image is not None:
            result['Image'] = self.image

        if self.image_registry_config is not None:
            result['ImageRegistryConfig'] = self.image_registry_config.to_map()

        if self.metrics_collect_config is not None:
            result['MetricsCollectConfig'] = self.metrics_collect_config.to_map()

        if self.port is not None:
            result['Port'] = self.port

        if self.request_concurrency is not None:
            result['RequestConcurrency'] = self.request_concurrency

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.slscollect_configs is not None:
            result['SLSCollectConfigs'] = self.slscollect_configs.to_map()

        if self.startup_probe is not None:
            result['StartupProbe'] = self.startup_probe.to_map()

        if self.web_nasconfig is not None:
            result['WebNASConfig'] = self.web_nasconfig.to_map()

        if self.web_ossconfig is not None:
            result['WebOSSConfig'] = self.web_ossconfig.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImageRegistryConfig') is not None:
            temp_model = main_models.ImageRegistryConfig()
            self.image_registry_config = temp_model.from_map(m.get('ImageRegistryConfig'))

        if m.get('MetricsCollectConfig') is not None:
            temp_model = main_models.MetricsCollectConfig()
            self.metrics_collect_config = temp_model.from_map(m.get('MetricsCollectConfig'))

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RequestConcurrency') is not None:
            self.request_concurrency = m.get('RequestConcurrency')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('Resources') is not None:
            temp_model = main_models.ContainerResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('SLSCollectConfigs') is not None:
            temp_model = main_models.SLSCollectConfigs()
            self.slscollect_configs = temp_model.from_map(m.get('SLSCollectConfigs'))

        if m.get('StartupProbe') is not None:
            temp_model = main_models.StartupProbe()
            self.startup_probe = temp_model.from_map(m.get('StartupProbe'))

        if m.get('WebNASConfig') is not None:
            temp_model = main_models.WebNASConfig()
            self.web_nasconfig = temp_model.from_map(m.get('WebNASConfig'))

        if m.get('WebOSSConfig') is not None:
            temp_model = main_models.WebOSSConfig()
            self.web_ossconfig = temp_model.from_map(m.get('WebOSSConfig'))

        return self

