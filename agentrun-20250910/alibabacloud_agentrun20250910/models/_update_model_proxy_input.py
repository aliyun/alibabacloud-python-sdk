# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class UpdateModelProxyInput(DaraModel):
    def __init__(
        self,
        arms_configuration: main_models.ArmsConfiguration = None,
        credential_name: str = None,
        description: str = None,
        execution_role_arn: str = None,
        log_configuration: main_models.LogConfiguration = None,
        network_configuration: main_models.NetworkConfiguration = None,
        proxy_config: main_models.ProxyConfig = None,
    ):
        self.arms_configuration = arms_configuration
        self.credential_name = credential_name
        self.description = description
        self.execution_role_arn = execution_role_arn
        self.log_configuration = log_configuration
        self.network_configuration = network_configuration
        self.proxy_config = proxy_config

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

        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.description is not None:
            result['description'] = self.description

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.log_configuration is not None:
            result['logConfiguration'] = self.log_configuration.to_map()

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.proxy_config is not None:
            result['proxyConfig'] = self.proxy_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('armsConfiguration') is not None:
            temp_model = main_models.ArmsConfiguration()
            self.arms_configuration = temp_model.from_map(m.get('armsConfiguration'))

        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('logConfiguration') is not None:
            temp_model = main_models.LogConfiguration()
            self.log_configuration = temp_model.from_map(m.get('logConfiguration'))

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('proxyConfig') is not None:
            temp_model = main_models.ProxyConfig()
            self.proxy_config = temp_model.from_map(m.get('proxyConfig'))

        return self

