# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateK8sServiceRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        external_traffic_policy: str = None,
        name: str = None,
        service_ports: str = None,
        type: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The policy used for external traffic management. Valid values:
        # 
        # *   Local: The network traffic can be routed to pods on the node where the Service is deployed.
        # *   Cluster: The network traffic can be routed to pods on other nodes in the cluster.
        # 
        # Default value: Local.
        self.external_traffic_policy = external_traffic_policy
        # The name of the Kubernetes Service.
        # 
        # This parameter is required.
        self.name = name
        # The port mapping of the Kubernetes Service. Set this parameter to a JSON array. The following parameters are included in the configurations:
        # 
        # *   **protocol**: the protocol used by the Service. Valid values: TCP and UDP. This parameter is mandatory.
        # *   **port**: the frontend service port. Valid values: 1 to 65535. This parameter is mandatory.
        # *   **targetPort**: the backend container port. Valid values: 1 to 65535. This parameter is mandatory.
        # 
        # Example: `[{"protocol": "TCP", "port": 80, "targetPort": 8080},{"protocol": "TCP", "port": 81, "targetPort": 8081}]`
        # 
        # This parameter is required.
        self.service_ports = service_ports
        # The type of the Kubernetes Service. Set the value to ClusterIP.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.external_traffic_policy is not None:
            result['ExternalTrafficPolicy'] = self.external_traffic_policy

        if self.name is not None:
            result['Name'] = self.name

        if self.service_ports is not None:
            result['ServicePorts'] = self.service_ports

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ExternalTrafficPolicy') is not None:
            self.external_traffic_policy = m.get('ExternalTrafficPolicy')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ServicePorts') is not None:
            self.service_ports = m.get('ServicePorts')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

