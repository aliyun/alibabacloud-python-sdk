# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateServiceRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        resource_group_id: str = None,
        service_configs: List[main_models.CreateServiceRequestServiceConfigs] = None,
        source_type: str = None,
        client_token: str = None,
    ):
        # The gateway instance ID.
        self.gateway_id = gateway_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The list of service configurations.
        self.service_configs = service_configs
        # The service source. Valid values:
        # 
        # *   MSE_NACOS: a service in an MSE Nacos instance
        # *   K8S: a service in a Kubernetes (K8s) cluster in Container Service for Kubernetes (ACK)
        # *   VIP: a fixed IP address
        # *   DNS: a Domain Name System (DNS) domain name
        # *   FC3: a service in Function Compute
        # *   SAE_K8S_SERVICE: a service in a K8s cluster in Serverless App Engine (SAE)
        # 
        # Enumerated values:
        # 
        # *   SAE_K8S_SERVICE
        # *   K8S
        # *   FC3
        # *   DNS
        # *   VIP
        # *   MSE_NACOS
        self.source_type = source_type
        self.client_token = client_token

    def validate(self):
        if self.service_configs:
            for v1 in self.service_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k1 in self.service_configs:
                result['serviceConfigs'].append(k1.to_map() if k1 else None)

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k1 in m.get('serviceConfigs'):
                temp_model = main_models.CreateServiceRequestServiceConfigs()
                self.service_configs.append(temp_model.from_map(k1))

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateServiceRequestServiceConfigs(DaraModel):
    def __init__(
        self,
        addresses: List[str] = None,
        agent_service_config: main_models.AgentServiceConfig = None,
        ai_service_config: main_models.AiServiceConfig = None,
        dns_servers: List[str] = None,
        express_type: str = None,
        group_name: str = None,
        name: str = None,
        namespace: str = None,
        qualifier: str = None,
        source_id: str = None,
        validation_options: main_models.CreateServiceRequestServiceConfigsValidationOptions = None,
    ):
        # The list of domain names or fixed addresses.
        self.addresses = addresses
        self.agent_service_config = agent_service_config
        # The AI service configurations.
        self.ai_service_config = ai_service_config
        # The list of DNS service addresses.
        self.dns_servers = dns_servers
        self.express_type = express_type
        # The service group name. This parameter is required if sourceType is set to MSE_NACOS.
        self.group_name = group_name
        # The service name.
        self.name = name
        # The service namespace. This parameter is required when sourceType is set to K8S or MSE_NACOS.
        # 
        # *   If sourceType is set to K8S, this parameter specifies the namespace where the K8s service resides.
        # *   If sourceType is set to MSE_NACOS, this parameter specifies a namespace in Nacos.
        self.namespace = namespace
        # The function version or alias.
        self.qualifier = qualifier
        self.source_id = source_id
        self.validation_options = validation_options

    def validate(self):
        if self.agent_service_config:
            self.agent_service_config.validate()
        if self.ai_service_config:
            self.ai_service_config.validate()
        if self.validation_options:
            self.validation_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addresses is not None:
            result['addresses'] = self.addresses

        if self.agent_service_config is not None:
            result['agentServiceConfig'] = self.agent_service_config.to_map()

        if self.ai_service_config is not None:
            result['aiServiceConfig'] = self.ai_service_config.to_map()

        if self.dns_servers is not None:
            result['dnsServers'] = self.dns_servers

        if self.express_type is not None:
            result['expressType'] = self.express_type

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.validation_options is not None:
            result['validationOptions'] = self.validation_options.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addresses') is not None:
            self.addresses = m.get('addresses')

        if m.get('agentServiceConfig') is not None:
            temp_model = main_models.AgentServiceConfig()
            self.agent_service_config = temp_model.from_map(m.get('agentServiceConfig'))

        if m.get('aiServiceConfig') is not None:
            temp_model = main_models.AiServiceConfig()
            self.ai_service_config = temp_model.from_map(m.get('aiServiceConfig'))

        if m.get('dnsServers') is not None:
            self.dns_servers = m.get('dnsServers')

        if m.get('expressType') is not None:
            self.express_type = m.get('expressType')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('validationOptions') is not None:
            temp_model = main_models.CreateServiceRequestServiceConfigsValidationOptions()
            self.validation_options = temp_model.from_map(m.get('validationOptions'))

        return self

class CreateServiceRequestServiceConfigsValidationOptions(DaraModel):
    def __init__(
        self,
        skip_verify_aichat_completion: bool = None,
    ):
        self.skip_verify_aichat_completion = skip_verify_aichat_completion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skip_verify_aichat_completion is not None:
            result['skipVerifyAIChatCompletion'] = self.skip_verify_aichat_completion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('skipVerifyAIChatCompletion') is not None:
            self.skip_verify_aichat_completion = m.get('skipVerifyAIChatCompletion')

        return self

