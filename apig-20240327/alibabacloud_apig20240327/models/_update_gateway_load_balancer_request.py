# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateGatewayLoadBalancerRequest(DaraModel):
    def __init__(
        self,
        load_balancer_dto: main_models.UpdateGatewayLoadBalancerRequestLoadBalancerDTO = None,
        option: str = None,
        ports: List[main_models.UpdateGatewayLoadBalancerRequestPorts] = None,
    ):
        self.load_balancer_dto = load_balancer_dto
        self.option = option
        self.ports = ports

    def validate(self):
        if self.load_balancer_dto:
            self.load_balancer_dto.validate()
        if self.ports:
            for v1 in self.ports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_dto is not None:
            result['loadBalancerDTO'] = self.load_balancer_dto.to_map()

        if self.option is not None:
            result['option'] = self.option

        result['ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['ports'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loadBalancerDTO') is not None:
            temp_model = main_models.UpdateGatewayLoadBalancerRequestLoadBalancerDTO()
            self.load_balancer_dto = temp_model.from_map(m.get('loadBalancerDTO'))

        if m.get('option') is not None:
            self.option = m.get('option')

        self.ports = []
        if m.get('ports') is not None:
            for k1 in m.get('ports'):
                temp_model = main_models.UpdateGatewayLoadBalancerRequestPorts()
                self.ports.append(temp_model.from_map(k1))

        return self

class UpdateGatewayLoadBalancerRequestPorts(DaraModel):
    def __init__(
        self,
        gateway_load_balancer_ports: List[main_models.UpdateGatewayLoadBalancerRequestPortsGatewayLoadBalancerPorts] = None,
        type: str = None,
    ):
        self.gateway_load_balancer_ports = gateway_load_balancer_ports
        self.type = type

    def validate(self):
        if self.gateway_load_balancer_ports:
            for v1 in self.gateway_load_balancer_ports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['gatewayLoadBalancerPorts'] = []
        if self.gateway_load_balancer_ports is not None:
            for k1 in self.gateway_load_balancer_ports:
                result['gatewayLoadBalancerPorts'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway_load_balancer_ports = []
        if m.get('gatewayLoadBalancerPorts') is not None:
            for k1 in m.get('gatewayLoadBalancerPorts'):
                temp_model = main_models.UpdateGatewayLoadBalancerRequestPortsGatewayLoadBalancerPorts()
                self.gateway_load_balancer_ports.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateGatewayLoadBalancerRequestPortsGatewayLoadBalancerPorts(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

class UpdateGatewayLoadBalancerRequestLoadBalancerDTO(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        load_balancer_type: str = None,
        network_type: str = None,
        service_weight: int = None,
        virtual_service_list: List[main_models.UpdateGatewayLoadBalancerRequestLoadBalancerDTOVirtualServiceList] = None,
    ):
        self.load_balancer_id = load_balancer_id
        self.load_balancer_type = load_balancer_type
        self.network_type = network_type
        self.service_weight = service_weight
        self.virtual_service_list = virtual_service_list

    def validate(self):
        if self.virtual_service_list:
            for v1 in self.virtual_service_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_id is not None:
            result['loadBalancerId'] = self.load_balancer_id

        if self.load_balancer_type is not None:
            result['loadBalancerType'] = self.load_balancer_type

        if self.network_type is not None:
            result['networkType'] = self.network_type

        if self.service_weight is not None:
            result['serviceWeight'] = self.service_weight

        result['virtualServiceList'] = []
        if self.virtual_service_list is not None:
            for k1 in self.virtual_service_list:
                result['virtualServiceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loadBalancerId') is not None:
            self.load_balancer_id = m.get('loadBalancerId')

        if m.get('loadBalancerType') is not None:
            self.load_balancer_type = m.get('loadBalancerType')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        if m.get('serviceWeight') is not None:
            self.service_weight = m.get('serviceWeight')

        self.virtual_service_list = []
        if m.get('virtualServiceList') is not None:
            for k1 in m.get('virtualServiceList'):
                temp_model = main_models.UpdateGatewayLoadBalancerRequestLoadBalancerDTOVirtualServiceList()
                self.virtual_service_list.append(temp_model.from_map(k1))

        return self

class UpdateGatewayLoadBalancerRequestLoadBalancerDTOVirtualServiceList(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        virtual_service_group_id: str = None,
        virtual_service_group_name: str = None,
    ):
        self.port = port
        self.protocol = protocol
        self.virtual_service_group_id = virtual_service_group_id
        self.virtual_service_group_name = virtual_service_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.virtual_service_group_id is not None:
            result['virtualServiceGroupId'] = self.virtual_service_group_id

        if self.virtual_service_group_name is not None:
            result['virtualServiceGroupName'] = self.virtual_service_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('virtualServiceGroupId') is not None:
            self.virtual_service_group_id = m.get('virtualServiceGroupId')

        if m.get('virtualServiceGroupName') is not None:
            self.virtual_service_group_name = m.get('virtualServiceGroupName')

        return self

