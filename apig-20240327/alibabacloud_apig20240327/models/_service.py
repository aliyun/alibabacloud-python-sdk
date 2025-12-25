# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class Service(DaraModel):
    def __init__(
        self,
        addresses: List[str] = None,
        agent_service_config: main_models.AgentServiceConfig = None,
        ai_service_config: main_models.AiServiceConfig = None,
        create_timestamp: int = None,
        express_type: str = None,
        gateway_id: str = None,
        group_name: str = None,
        health_check: main_models.ServiceHealthCheck = None,
        health_status: str = None,
        label_details: List[main_models.LabelDetail] = None,
        name: str = None,
        namespace: str = None,
        outlier_endpoints: List[str] = None,
        ports: List[main_models.ServicePorts] = None,
        protocol: str = None,
        qualifier: str = None,
        resource_group_id: str = None,
        service_id: str = None,
        source_type: str = None,
        unhealthy_endpoints: List[str] = None,
        update_timestamp: int = None,
    ):
        self.addresses = addresses
        self.agent_service_config = agent_service_config
        self.ai_service_config = ai_service_config
        self.create_timestamp = create_timestamp
        self.express_type = express_type
        self.gateway_id = gateway_id
        self.group_name = group_name
        self.health_check = health_check
        self.health_status = health_status
        self.label_details = label_details
        self.name = name
        self.namespace = namespace
        self.outlier_endpoints = outlier_endpoints
        self.ports = ports
        self.protocol = protocol
        self.qualifier = qualifier
        self.resource_group_id = resource_group_id
        self.service_id = service_id
        self.source_type = source_type
        self.unhealthy_endpoints = unhealthy_endpoints
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.agent_service_config:
            self.agent_service_config.validate()
        if self.ai_service_config:
            self.ai_service_config.validate()
        if self.health_check:
            self.health_check.validate()
        if self.label_details:
            for v1 in self.label_details:
                 if v1:
                    v1.validate()
        if self.ports:
            for v1 in self.ports:
                 if v1:
                    v1.validate()

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

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.express_type is not None:
            result['expressType'] = self.express_type

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.health_check is not None:
            result['healthCheck'] = self.health_check.to_map()

        if self.health_status is not None:
            result['healthStatus'] = self.health_status

        result['labelDetails'] = []
        if self.label_details is not None:
            for k1 in self.label_details:
                result['labelDetails'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.outlier_endpoints is not None:
            result['outlierEndpoints'] = self.outlier_endpoints

        result['ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['ports'].append(k1.to_map() if k1 else None)

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.unhealthy_endpoints is not None:
            result['unhealthyEndpoints'] = self.unhealthy_endpoints

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

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

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('expressType') is not None:
            self.express_type = m.get('expressType')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('healthCheck') is not None:
            temp_model = main_models.ServiceHealthCheck()
            self.health_check = temp_model.from_map(m.get('healthCheck'))

        if m.get('healthStatus') is not None:
            self.health_status = m.get('healthStatus')

        self.label_details = []
        if m.get('labelDetails') is not None:
            for k1 in m.get('labelDetails'):
                temp_model = main_models.LabelDetail()
                self.label_details.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('outlierEndpoints') is not None:
            self.outlier_endpoints = m.get('outlierEndpoints')

        self.ports = []
        if m.get('ports') is not None:
            for k1 in m.get('ports'):
                temp_model = main_models.ServicePorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('unhealthyEndpoints') is not None:
            self.unhealthy_endpoints = m.get('unhealthyEndpoints')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

class ServicePorts(DaraModel):
    def __init__(
        self,
        name: str = None,
        port: int = None,
        protocol: str = None,
    ):
        self.name = name
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

