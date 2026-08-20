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
        dns_servers: List[str] = None,
        express_type: str = None,
        gateway_id: str = None,
        group_name: str = None,
        health_check: main_models.ServiceHealthCheck = None,
        health_status: str = None,
        healthy_panic_threshold: float = None,
        label_details: List[main_models.LabelDetail] = None,
        model_provider_id: str = None,
        name: str = None,
        namespace: str = None,
        outlier_detection: main_models.ServiceOutlierDetection = None,
        outlier_endpoints: List[str] = None,
        ports: List[main_models.ServicePorts] = None,
        protocol: str = None,
        qualifier: str = None,
        resource_group_id: str = None,
        runtime_detail_error_code: str = None,
        runtime_detail_status: str = None,
        service_id: str = None,
        source_type: str = None,
        unhealthy_endpoints: List[str] = None,
        update_timestamp: int = None,
        versions: List[main_models.ServiceVersions] = None,
    ):
        # The address information, including IP addresses or domain name lists.
        self.addresses = addresses
        # The agent service configuration.
        self.agent_service_config = agent_service_config
        # The AI service configuration.
        self.ai_service_config = ai_service_config
        # The time when the service was created.
        self.create_timestamp = create_timestamp
        # The list of DNS servers.
        self.dns_servers = dns_servers
        # The execution mode of CloudFlow.
        self.express_type = express_type
        # The instance ID of the gateway.
        self.gateway_id = gateway_id
        # The name of the service group.
        self.group_name = group_name
        # The health check configuration.
        self.health_check = health_check
        # The health check status. Valid values: Healthy and Unhealthy.
        self.health_status = health_status
        # The healthy panic threshold.
        self.healthy_panic_threshold = healthy_panic_threshold
        # The label information of the service.
        self.label_details = label_details
        # The resource ID of the model provider.
        self.model_provider_id = model_provider_id
        # The name of the service.
        self.name = name
        # The namespace.
        self.namespace = namespace
        # The configuration for removing abnormal instances.
        self.outlier_detection = outlier_detection
        # The circuit-broken endpoints.
        self.outlier_endpoints = outlier_endpoints
        # The list of port information.
        self.ports = ports
        # The service protocol.
        self.protocol = protocol
        # The qualifier of the function.
        self.qualifier = qualifier
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The masked error code of the runtime details.
        self.runtime_detail_error_code = runtime_detail_error_code
        # The runtime detail status.
        self.runtime_detail_status = runtime_detail_status
        # The unique ID of the service.
        self.service_id = service_id
        # The source type of the service.
        self.source_type = source_type
        # The unhealthy endpoints.
        self.unhealthy_endpoints = unhealthy_endpoints
        # The time when the service was created.
        self.update_timestamp = update_timestamp
        # The list of service versions.
        self.versions = versions

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
        if self.outlier_detection:
            self.outlier_detection.validate()
        if self.ports:
            for v1 in self.ports:
                 if v1:
                    v1.validate()
        if self.versions:
            for v1 in self.versions:
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

        if self.dns_servers is not None:
            result['dnsServers'] = self.dns_servers

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

        if self.healthy_panic_threshold is not None:
            result['healthyPanicThreshold'] = self.healthy_panic_threshold

        result['labelDetails'] = []
        if self.label_details is not None:
            for k1 in self.label_details:
                result['labelDetails'].append(k1.to_map() if k1 else None)

        if self.model_provider_id is not None:
            result['modelProviderId'] = self.model_provider_id

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.outlier_detection is not None:
            result['outlierDetection'] = self.outlier_detection.to_map()

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

        if self.runtime_detail_error_code is not None:
            result['runtimeDetailErrorCode'] = self.runtime_detail_error_code

        if self.runtime_detail_status is not None:
            result['runtimeDetailStatus'] = self.runtime_detail_status

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.unhealthy_endpoints is not None:
            result['unhealthyEndpoints'] = self.unhealthy_endpoints

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        result['versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['versions'].append(k1.to_map() if k1 else None)

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

        if m.get('dnsServers') is not None:
            self.dns_servers = m.get('dnsServers')

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

        if m.get('healthyPanicThreshold') is not None:
            self.healthy_panic_threshold = m.get('healthyPanicThreshold')

        self.label_details = []
        if m.get('labelDetails') is not None:
            for k1 in m.get('labelDetails'):
                temp_model = main_models.LabelDetail()
                self.label_details.append(temp_model.from_map(k1))

        if m.get('modelProviderId') is not None:
            self.model_provider_id = m.get('modelProviderId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('outlierDetection') is not None:
            temp_model = main_models.ServiceOutlierDetection()
            self.outlier_detection = temp_model.from_map(m.get('outlierDetection'))

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

        if m.get('runtimeDetailErrorCode') is not None:
            self.runtime_detail_error_code = m.get('runtimeDetailErrorCode')

        if m.get('runtimeDetailStatus') is not None:
            self.runtime_detail_status = m.get('runtimeDetailStatus')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('unhealthyEndpoints') is not None:
            self.unhealthy_endpoints = m.get('unhealthyEndpoints')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        self.versions = []
        if m.get('versions') is not None:
            for k1 in m.get('versions'):
                temp_model = main_models.ServiceVersions()
                self.versions.append(temp_model.from_map(k1))

        return self

class ServiceVersions(DaraModel):
    def __init__(
        self,
        labels: List[main_models.ServiceVersionsLabels] = None,
        name: str = None,
    ):
        # The list of version labels.
        self.labels = labels
        # The version name.
        self.name = name

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('labels') is not None:
            for k1 in m.get('labels'):
                temp_model = main_models.ServiceVersionsLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ServiceVersionsLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The label key.
        self.key = key
        # The label value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ServicePorts(DaraModel):
    def __init__(
        self,
        name: str = None,
        port: int = None,
        protocol: str = None,
    ):
        # The name of the port.
        self.name = name
        # The port number.
        self.port = port
        # The protocol. Valid values: TCP and UDP.
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

class ServiceOutlierDetection(DaraModel):
    def __init__(
        self,
        base_ejection_time: int = None,
        enable: bool = None,
        failure_percentage_minimum_hosts: int = None,
        failure_percentage_threshold: int = None,
        interval: int = None,
    ):
        # The base ejection duration in seconds. Valid values: 1 to 3600.
        self.base_ejection_time = base_ejection_time
        # Specifies whether to enable outlier detection.
        self.enable = enable
        # The minimum number of hosts. The value must be greater than or equal to 0.
        self.failure_percentage_minimum_hosts = failure_percentage_minimum_hosts
        # The failure rate threshold in percentage. Valid values: 1 to 100.
        self.failure_percentage_threshold = failure_percentage_threshold
        # The detection interval in seconds. Valid values: 1 to 3600.
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_ejection_time is not None:
            result['baseEjectionTime'] = self.base_ejection_time

        if self.enable is not None:
            result['enable'] = self.enable

        if self.failure_percentage_minimum_hosts is not None:
            result['failurePercentageMinimumHosts'] = self.failure_percentage_minimum_hosts

        if self.failure_percentage_threshold is not None:
            result['failurePercentageThreshold'] = self.failure_percentage_threshold

        if self.interval is not None:
            result['interval'] = self.interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baseEjectionTime') is not None:
            self.base_ejection_time = m.get('baseEjectionTime')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('failurePercentageMinimumHosts') is not None:
            self.failure_percentage_minimum_hosts = m.get('failurePercentageMinimumHosts')

        if m.get('failurePercentageThreshold') is not None:
            self.failure_percentage_threshold = m.get('failurePercentageThreshold')

        if m.get('interval') is not None:
            self.interval = m.get('interval')

        return self

