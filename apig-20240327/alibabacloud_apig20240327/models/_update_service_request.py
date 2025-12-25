# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateServiceRequest(DaraModel):
    def __init__(
        self,
        addresses: List[str] = None,
        agent_service_config: main_models.AgentServiceConfig = None,
        ai_service_config: main_models.AiServiceConfig = None,
        dns_servers: List[str] = None,
        health_check_config: main_models.UpdateServiceRequestHealthCheckConfig = None,
        healthy_panic_threshold: float = None,
        outlier_detection_config: main_models.UpdateServiceRequestOutlierDetectionConfig = None,
        ports: List[main_models.UpdateServiceRequestPorts] = None,
        protocol: str = None,
    ):
        # The list of domain names or fixed addresses.
        self.addresses = addresses
        # The agent service configurations.
        self.agent_service_config = agent_service_config
        # The AI service configurations.
        self.ai_service_config = ai_service_config
        # A DNS service address.
        self.dns_servers = dns_servers
        # The health check configurations.
        self.health_check_config = health_check_config
        # The health check threshold.
        self.healthy_panic_threshold = healthy_panic_threshold
        # The passive health check configurations.
        self.outlier_detection_config = outlier_detection_config
        # The port information.
        self.ports = ports
        # The service protocol.
        self.protocol = protocol

    def validate(self):
        if self.agent_service_config:
            self.agent_service_config.validate()
        if self.ai_service_config:
            self.ai_service_config.validate()
        if self.health_check_config:
            self.health_check_config.validate()
        if self.outlier_detection_config:
            self.outlier_detection_config.validate()
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

        if self.dns_servers is not None:
            result['dnsServers'] = self.dns_servers

        if self.health_check_config is not None:
            result['healthCheckConfig'] = self.health_check_config.to_map()

        if self.healthy_panic_threshold is not None:
            result['healthyPanicThreshold'] = self.healthy_panic_threshold

        if self.outlier_detection_config is not None:
            result['outlierDetectionConfig'] = self.outlier_detection_config.to_map()

        result['ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['ports'].append(k1.to_map() if k1 else None)

        if self.protocol is not None:
            result['protocol'] = self.protocol

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

        if m.get('healthCheckConfig') is not None:
            temp_model = main_models.UpdateServiceRequestHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m.get('healthCheckConfig'))

        if m.get('healthyPanicThreshold') is not None:
            self.healthy_panic_threshold = m.get('healthyPanicThreshold')

        if m.get('outlierDetectionConfig') is not None:
            temp_model = main_models.UpdateServiceRequestOutlierDetectionConfig()
            self.outlier_detection_config = temp_model.from_map(m.get('outlierDetectionConfig'))

        self.ports = []
        if m.get('ports') is not None:
            for k1 in m.get('ports'):
                temp_model = main_models.UpdateServiceRequestPorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

class UpdateServiceRequestPorts(DaraModel):
    def __init__(
        self,
        name: str = None,
        port: int = None,
        protocol: str = None,
    ):
        # The port name.
        self.name = name
        # The port.
        self.port = port
        # The protocol.
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

class UpdateServiceRequestOutlierDetectionConfig(DaraModel):
    def __init__(
        self,
        base_ejection_time: int = None,
        enable: bool = None,
        failure_percentage_minimum_hosts: int = None,
        failure_percentage_threshold: int = None,
        interval: int = None,
    ):
        # The initial isolation duration after a node is isolated (e.g., 30 seconds). The isolation time is calculated as: k \\* base_ejection_time (with k initially set to 1). Each subsequent isolation increases the isolation time (k is incremented by 1), while consecutive healthy checks gradually decrease the isolation time (k is decremented by 1).
        self.base_ejection_time = base_ejection_time
        # enable
        self.enable = enable
        # The panic threshold.
        # 
        # When the proportion of healthy nodes in the service is greater than the panic threshold, health checks take effect normally, and requests are only sent to healthy nodes, not to ejected nodes. When the proportion of healthy nodes in the service is less than or equal to the panic threshold, health checks are effectively disabled, and requests are sent to all nodes, including those that have been ejected nodes.
        self.failure_percentage_minimum_hosts = failure_percentage_minimum_hosts
        # When the request failure rate of a node reaches this threshold, the system triggers the isolation mechanism of the node.
        self.failure_percentage_threshold = failure_percentage_threshold
        # The detection interval.
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

class UpdateServiceRequestHealthCheckConfig(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        expected_statuses: List[str] = None,
        healthy_threshold: int = None,
        http_host: str = None,
        http_path: str = None,
        interval: int = None,
        protocol: str = None,
        timeout: int = None,
        unhealthy_threshold: int = None,
    ):
        # Specifies whether to enable health checks.
        self.enable = enable
        # The normal status codes to be returned. This parameter is required if the health check protocol is HTTP.
        self.expected_statuses = expected_statuses
        # The healthy threshold.
        self.healthy_threshold = healthy_threshold
        # The domain name that you want to use for health checks. Optional. This parameter is available if the health check protocol is HTTP.
        self.http_host = http_host
        # The request path of health checks. This parameter is required if the health check protocol is HTTP.
        self.http_path = http_path
        # The health check interval. Unit: seconds
        self.interval = interval
        # The protocol over which the system performs health checks.
        # 
        # Valid values:
        # 
        # *   TCP
        # *   HTTP
        self.protocol = protocol
        # The timeout period for a health check response. Unit: seconds
        self.timeout = timeout
        # The unhealthy threshold.
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.expected_statuses is not None:
            result['expectedStatuses'] = self.expected_statuses

        if self.healthy_threshold is not None:
            result['healthyThreshold'] = self.healthy_threshold

        if self.http_host is not None:
            result['httpHost'] = self.http_host

        if self.http_path is not None:
            result['httpPath'] = self.http_path

        if self.interval is not None:
            result['interval'] = self.interval

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.unhealthy_threshold is not None:
            result['unhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('expectedStatuses') is not None:
            self.expected_statuses = m.get('expectedStatuses')

        if m.get('healthyThreshold') is not None:
            self.healthy_threshold = m.get('healthyThreshold')

        if m.get('httpHost') is not None:
            self.http_host = m.get('httpHost')

        if m.get('httpPath') is not None:
            self.http_path = m.get('httpPath')

        if m.get('interval') is not None:
            self.interval = m.get('interval')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('unhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('unhealthyThreshold')

        return self

