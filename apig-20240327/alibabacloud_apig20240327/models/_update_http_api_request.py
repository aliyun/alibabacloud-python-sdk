# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateHttpApiRequest(DaraModel):
    def __init__(
        self,
        agent_protocols: List[str] = None,
        ai_protocols: List[str] = None,
        auth_config: main_models.AuthConfig = None,
        base_path: str = None,
        deploy_configs: List[main_models.HttpApiDeployConfig] = None,
        description: str = None,
        enable_auth: bool = None,
        first_byte_timeout: int = None,
        ingress_config: main_models.UpdateHttpApiRequestIngressConfig = None,
        only_change_config: bool = None,
        protocols: List[str] = None,
        remove_base_path_on_forward: bool = None,
        version_config: main_models.HttpApiVersionConfig = None,
    ):
        self.agent_protocols = agent_protocols
        # The AI protocols.
        self.ai_protocols = ai_protocols
        # The authentication configuration.
        self.auth_config = auth_config
        # The API base path, which must start with a forward slash (/).
        # 
        # This parameter is required.
        self.base_path = base_path
        # The deployment configurations.
        self.deploy_configs = deploy_configs
        # The API description.
        self.description = description
        # Specifies whether to enable authentication.
        self.enable_auth = enable_auth
        self.first_byte_timeout = first_byte_timeout
        # The HTTP Ingress API configurations.
        self.ingress_config = ingress_config
        self.only_change_config = only_change_config
        # The protocols that are used to access the API.
        self.protocols = protocols
        self.remove_base_path_on_forward = remove_base_path_on_forward
        # The versioning configurations.
        self.version_config = version_config

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.deploy_configs:
            for v1 in self.deploy_configs:
                 if v1:
                    v1.validate()
        if self.ingress_config:
            self.ingress_config.validate()
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_protocols is not None:
            result['agentProtocols'] = self.agent_protocols

        if self.ai_protocols is not None:
            result['aiProtocols'] = self.ai_protocols

        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()

        if self.base_path is not None:
            result['basePath'] = self.base_path

        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k1 in self.deploy_configs:
                result['deployConfigs'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.enable_auth is not None:
            result['enableAuth'] = self.enable_auth

        if self.first_byte_timeout is not None:
            result['firstByteTimeout'] = self.first_byte_timeout

        if self.ingress_config is not None:
            result['ingressConfig'] = self.ingress_config.to_map()

        if self.only_change_config is not None:
            result['onlyChangeConfig'] = self.only_change_config

        if self.protocols is not None:
            result['protocols'] = self.protocols

        if self.remove_base_path_on_forward is not None:
            result['removeBasePathOnForward'] = self.remove_base_path_on_forward

        if self.version_config is not None:
            result['versionConfig'] = self.version_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentProtocols') is not None:
            self.agent_protocols = m.get('agentProtocols')

        if m.get('aiProtocols') is not None:
            self.ai_protocols = m.get('aiProtocols')

        if m.get('authConfig') is not None:
            temp_model = main_models.AuthConfig()
            self.auth_config = temp_model.from_map(m.get('authConfig'))

        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')

        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k1 in m.get('deployConfigs'):
                temp_model = main_models.HttpApiDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enableAuth') is not None:
            self.enable_auth = m.get('enableAuth')

        if m.get('firstByteTimeout') is not None:
            self.first_byte_timeout = m.get('firstByteTimeout')

        if m.get('ingressConfig') is not None:
            temp_model = main_models.UpdateHttpApiRequestIngressConfig()
            self.ingress_config = temp_model.from_map(m.get('ingressConfig'))

        if m.get('onlyChangeConfig') is not None:
            self.only_change_config = m.get('onlyChangeConfig')

        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')

        if m.get('removeBasePathOnForward') is not None:
            self.remove_base_path_on_forward = m.get('removeBasePathOnForward')

        if m.get('versionConfig') is not None:
            temp_model = main_models.HttpApiVersionConfig()
            self.version_config = temp_model.from_map(m.get('versionConfig'))

        return self

class UpdateHttpApiRequestIngressConfig(DaraModel):
    def __init__(
        self,
        environment_id: str = None,
        ingress_class: str = None,
        override_ingress_ip: bool = None,
        source_id: str = None,
        watch_namespace: str = None,
    ):
        # The environment ID.
        self.environment_id = environment_id
        # The Ingress class for listening.
        self.ingress_class = ingress_class
        # Specifies whether to update the address in Ingress Status.
        self.override_ingress_ip = override_ingress_ip
        # The source ID.
        self.source_id = source_id
        # The namespace for listening.
        self.watch_namespace = watch_namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.ingress_class is not None:
            result['ingressClass'] = self.ingress_class

        if self.override_ingress_ip is not None:
            result['overrideIngressIp'] = self.override_ingress_ip

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.watch_namespace is not None:
            result['watchNamespace'] = self.watch_namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('ingressClass') is not None:
            self.ingress_class = m.get('ingressClass')

        if m.get('overrideIngressIp') is not None:
            self.override_ingress_ip = m.get('overrideIngressIp')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('watchNamespace') is not None:
            self.watch_namespace = m.get('watchNamespace')

        return self

