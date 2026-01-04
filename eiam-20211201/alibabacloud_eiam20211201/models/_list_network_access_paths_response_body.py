# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListNetworkAccessPathsResponseBody(DaraModel):
    def __init__(
        self,
        network_access_paths: List[main_models.ListNetworkAccessPathsResponseBodyNetworkAccessPaths] = None,
        request_id: str = None,
    ):
        # Network access paths
        self.network_access_paths = network_access_paths
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.network_access_paths:
            for v1 in self.network_access_paths:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkAccessPaths'] = []
        if self.network_access_paths is not None:
            for k1 in self.network_access_paths:
                result['NetworkAccessPaths'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_access_paths = []
        if m.get('NetworkAccessPaths') is not None:
            for k1 in m.get('NetworkAccessPaths'):
                temp_model = main_models.ListNetworkAccessPathsResponseBodyNetworkAccessPaths()
                self.network_access_paths.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListNetworkAccessPathsResponseBodyNetworkAccessPaths(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        instance_id: str = None,
        network_access_endpoint_id: str = None,
        network_access_path_id: str = None,
        network_interface_id: str = None,
        private_ip_address: str = None,
        status: str = None,
        update_time: int = None,
        v_switch_id: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # Network access endpoint ID.
        self.network_access_endpoint_id = network_access_endpoint_id
        # Network access path ID
        self.network_access_path_id = network_access_path_id
        # Network interface ID
        self.network_interface_id = network_interface_id
        # The private IP address.
        self.private_ip_address = private_ip_address
        # Network access path status
        self.status = status
        # The update time.
        self.update_time = update_time
        # The ID of a vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id

        if self.network_access_path_id is not None:
            result['NetworkAccessPathId'] = self.network_access_path_id

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('NetworkAccessPathId') is not None:
            self.network_access_path_id = m.get('NetworkAccessPathId')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

