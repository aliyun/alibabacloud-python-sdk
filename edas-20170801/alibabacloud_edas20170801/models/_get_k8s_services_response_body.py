# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetK8sServicesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        services: List[main_models.GetK8sServicesResponseBodyServices] = None,
    ):
        # The HTTP status code.
        self.code = code
        # Additional information.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The list of Kubernetes Services.
        self.services = services

    def validate(self):
        if self.services:
            for v1 in self.services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['Services'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.services = []
        if m.get('Services') is not None:
            for k1 in m.get('Services'):
                temp_model = main_models.GetK8sServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k1))

        return self

class GetK8sServicesResponseBodyServices(DaraModel):
    def __init__(
        self,
        cluster_ip: str = None,
        name: str = None,
        service_ports: List[main_models.GetK8sServicesResponseBodyServicesServicePorts] = None,
        type: str = None,
    ):
        # The IP address of the Kubernetes Service.
        self.cluster_ip = cluster_ip
        # The service name.
        self.name = name
        # The list of port mappings.
        self.service_ports = service_ports
        # The service type.
        self.type = type

    def validate(self):
        if self.service_ports:
            for v1 in self.service_ports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_ip is not None:
            result['ClusterIP'] = self.cluster_ip

        if self.name is not None:
            result['Name'] = self.name

        result['ServicePorts'] = []
        if self.service_ports is not None:
            for k1 in self.service_ports:
                result['ServicePorts'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIP') is not None:
            self.cluster_ip = m.get('ClusterIP')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.service_ports = []
        if m.get('ServicePorts') is not None:
            for k1 in m.get('ServicePorts'):
                temp_model = main_models.GetK8sServicesResponseBodyServicesServicePorts()
                self.service_ports.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetK8sServicesResponseBodyServicesServicePorts(DaraModel):
    def __init__(
        self,
        node_port: int = None,
        port: int = None,
        protocol: str = None,
        target_port: str = None,
    ):
        # The node port.
        self.node_port = node_port
        # The frontend service port.
        self.port = port
        # The service protocol.
        self.protocol = protocol
        # The backend container port.
        self.target_port = target_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_port is not None:
            result['NodePort'] = self.node_port

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodePort') is not None:
            self.node_port = m.get('NodePort')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        return self

