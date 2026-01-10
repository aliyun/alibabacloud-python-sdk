# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateModelProxyInput(DaraModel):
    def __init__(
        self,
        arms_configuration: main_models.ArmsConfiguration = None,
        cpu: float = None,
        credential_name: str = None,
        description: str = None,
        execution_role_arn: str = None,
        litellm_version: str = None,
        log_configuration: main_models.LogConfiguration = None,
        memory: int = None,
        model_proxy_name: str = None,
        model_type: str = None,
        network_configuration: main_models.NetworkConfiguration = None,
        proxy_config: main_models.ProxyConfig = None,
        proxy_mode: str = None,
        service_region_id: str = None,
    ):
        self.arms_configuration = arms_configuration
        # This parameter is required.
        self.cpu = cpu
        self.credential_name = credential_name
        self.description = description
        self.execution_role_arn = execution_role_arn
        self.litellm_version = litellm_version
        self.log_configuration = log_configuration
        # This parameter is required.
        self.memory = memory
        # This parameter is required.
        self.model_proxy_name = model_proxy_name
        self.model_type = model_type
        self.network_configuration = network_configuration
        # This parameter is required.
        self.proxy_config = proxy_config
        # This parameter is required.
        self.proxy_mode = proxy_mode
        self.service_region_id = service_region_id

    def validate(self):
        if self.arms_configuration:
            self.arms_configuration.validate()
        if self.log_configuration:
            self.log_configuration.validate()
        if self.network_configuration:
            self.network_configuration.validate()
        if self.proxy_config:
            self.proxy_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arms_configuration is not None:
            result['armsConfiguration'] = self.arms_configuration.to_map()

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.description is not None:
            result['description'] = self.description

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.litellm_version is not None:
            result['litellmVersion'] = self.litellm_version

        if self.log_configuration is not None:
            result['logConfiguration'] = self.log_configuration.to_map()

        if self.memory is not None:
            result['memory'] = self.memory

        if self.model_proxy_name is not None:
            result['modelProxyName'] = self.model_proxy_name

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.proxy_config is not None:
            result['proxyConfig'] = self.proxy_config.to_map()

        if self.proxy_mode is not None:
            result['proxyMode'] = self.proxy_mode

        if self.service_region_id is not None:
            result['serviceRegionId'] = self.service_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('armsConfiguration') is not None:
            temp_model = main_models.ArmsConfiguration()
            self.arms_configuration = temp_model.from_map(m.get('armsConfiguration'))

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('litellmVersion') is not None:
            self.litellm_version = m.get('litellmVersion')

        if m.get('logConfiguration') is not None:
            temp_model = main_models.LogConfiguration()
            self.log_configuration = temp_model.from_map(m.get('logConfiguration'))

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('modelProxyName') is not None:
            self.model_proxy_name = m.get('modelProxyName')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('proxyConfig') is not None:
            temp_model = main_models.ProxyConfig()
            self.proxy_config = temp_model.from_map(m.get('proxyConfig'))

        if m.get('proxyMode') is not None:
            self.proxy_mode = m.get('proxyMode')

        if m.get('serviceRegionId') is not None:
            self.service_region_id = m.get('serviceRegionId')

        return self

