# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class ModelProxy(DaraModel):
    def __init__(
        self,
        cpu: float = None,
        created_at: str = None,
        credential_name: str = None,
        description: str = None,
        endpoint: str = None,
        execution_role_arn: str = None,
        function_name: str = None,
        last_updated_at: str = None,
        litellm_version: str = None,
        log_configuration: main_models.LogConfiguration = None,
        memory: int = None,
        model_proxy_id: str = None,
        model_proxy_name: str = None,
        model_type: str = None,
        network_configuration: main_models.NetworkConfiguration = None,
        proxy_config: main_models.ProxyConfig = None,
        proxy_mode: str = None,
        service_region_id: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        self.cpu = cpu
        self.created_at = created_at
        self.credential_name = credential_name
        self.description = description
        self.endpoint = endpoint
        self.execution_role_arn = execution_role_arn
        self.function_name = function_name
        self.last_updated_at = last_updated_at
        self.litellm_version = litellm_version
        self.log_configuration = log_configuration
        self.memory = memory
        self.model_proxy_id = model_proxy_id
        self.model_proxy_name = model_proxy_name
        self.model_type = model_type
        self.network_configuration = network_configuration
        self.proxy_config = proxy_config
        self.proxy_mode = proxy_mode
        self.service_region_id = service_region_id
        self.status = status
        self.status_reason = status_reason

    def validate(self):
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
        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.description is not None:
            result['description'] = self.description

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.litellm_version is not None:
            result['litellmVersion'] = self.litellm_version

        if self.log_configuration is not None:
            result['logConfiguration'] = self.log_configuration.to_map()

        if self.memory is not None:
            result['memory'] = self.memory

        if self.model_proxy_id is not None:
            result['modelProxyId'] = self.model_proxy_id

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

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        if m.get('litellmVersion') is not None:
            self.litellm_version = m.get('litellmVersion')

        if m.get('logConfiguration') is not None:
            temp_model = main_models.LogConfiguration()
            self.log_configuration = temp_model.from_map(m.get('logConfiguration'))

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('modelProxyId') is not None:
            self.model_proxy_id = m.get('modelProxyId')

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

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        return self

