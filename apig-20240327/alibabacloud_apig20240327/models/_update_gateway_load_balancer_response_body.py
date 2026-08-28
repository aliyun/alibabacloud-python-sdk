# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateGatewayLoadBalancerResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateGatewayLoadBalancerResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.UpdateGatewayLoadBalancerResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class UpdateGatewayLoadBalancerResponseBodyData(DaraModel):
    def __init__(
        self,
        edit_enable: bool = None,
        load_balancer_address: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_type: str = None,
        network_type: str = None,
        ports: List[int] = None,
        service_weight: int = None,
        status_description: str = None,
        virtual_service_list: List[main_models.UpdateGatewayLoadBalancerResponseBodyDataVirtualServiceList] = None,
    ):
        self.edit_enable = edit_enable
        self.load_balancer_address = load_balancer_address
        self.load_balancer_id = load_balancer_id
        self.load_balancer_name = load_balancer_name
        self.load_balancer_type = load_balancer_type
        self.network_type = network_type
        self.ports = ports
        self.service_weight = service_weight
        self.status_description = status_description
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
        if self.edit_enable is not None:
            result['editEnable'] = self.edit_enable

        if self.load_balancer_address is not None:
            result['loadBalancerAddress'] = self.load_balancer_address

        if self.load_balancer_id is not None:
            result['loadBalancerId'] = self.load_balancer_id

        if self.load_balancer_name is not None:
            result['loadBalancerName'] = self.load_balancer_name

        if self.load_balancer_type is not None:
            result['loadBalancerType'] = self.load_balancer_type

        if self.network_type is not None:
            result['networkType'] = self.network_type

        if self.ports is not None:
            result['ports'] = self.ports

        if self.service_weight is not None:
            result['serviceWeight'] = self.service_weight

        if self.status_description is not None:
            result['statusDescription'] = self.status_description

        result['virtualServiceList'] = []
        if self.virtual_service_list is not None:
            for k1 in self.virtual_service_list:
                result['virtualServiceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('editEnable') is not None:
            self.edit_enable = m.get('editEnable')

        if m.get('loadBalancerAddress') is not None:
            self.load_balancer_address = m.get('loadBalancerAddress')

        if m.get('loadBalancerId') is not None:
            self.load_balancer_id = m.get('loadBalancerId')

        if m.get('loadBalancerName') is not None:
            self.load_balancer_name = m.get('loadBalancerName')

        if m.get('loadBalancerType') is not None:
            self.load_balancer_type = m.get('loadBalancerType')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        if m.get('ports') is not None:
            self.ports = m.get('ports')

        if m.get('serviceWeight') is not None:
            self.service_weight = m.get('serviceWeight')

        if m.get('statusDescription') is not None:
            self.status_description = m.get('statusDescription')

        self.virtual_service_list = []
        if m.get('virtualServiceList') is not None:
            for k1 in m.get('virtualServiceList'):
                temp_model = main_models.UpdateGatewayLoadBalancerResponseBodyDataVirtualServiceList()
                self.virtual_service_list.append(temp_model.from_map(k1))

        return self

class UpdateGatewayLoadBalancerResponseBodyDataVirtualServiceList(DaraModel):
    def __init__(
        self,
        port: str = None,
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

