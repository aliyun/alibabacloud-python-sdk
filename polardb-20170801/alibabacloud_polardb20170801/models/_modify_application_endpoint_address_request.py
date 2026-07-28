# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class ModifyApplicationEndpointAddressRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        endpoint_id: str = None,
        net_type: str = None,
        new_connection_string_prefix: str = None,
        new_ports: List[main_models.ModifyApplicationEndpointAddressRequestNewPorts] = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The endpoint ID.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # The network type of the endpoint address. Valid values: 
        # 
        # * **Public**: public network.
        # * **Private**: private network.
        # 
        # This parameter is required.
        self.net_type = net_type
        # The new endpoint prefix.
        self.new_connection_string_prefix = new_connection_string_prefix
        # The list of new ports.
        self.new_ports = new_ports

    def validate(self):
        if self.new_ports:
            for v1 in self.new_ports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.new_connection_string_prefix is not None:
            result['NewConnectionStringPrefix'] = self.new_connection_string_prefix

        result['NewPorts'] = []
        if self.new_ports is not None:
            for k1 in self.new_ports:
                result['NewPorts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('NewConnectionStringPrefix') is not None:
            self.new_connection_string_prefix = m.get('NewConnectionStringPrefix')

        self.new_ports = []
        if m.get('NewPorts') is not None:
            for k1 in m.get('NewPorts'):
                temp_model = main_models.ModifyApplicationEndpointAddressRequestNewPorts()
                self.new_ports.append(temp_model.from_map(k1))

        return self

class ModifyApplicationEndpointAddressRequestNewPorts(DaraModel):
    def __init__(
        self,
        new_port: int = None,
        old_port: int = None,
        port_name: str = None,
    ):
        # The new port value.
        self.new_port = new_port
        # The old port value.
        self.old_port = old_port
        # The port name.
        self.port_name = port_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_port is not None:
            result['NewPort'] = self.new_port

        if self.old_port is not None:
            result['OldPort'] = self.old_port

        if self.port_name is not None:
            result['PortName'] = self.port_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewPort') is not None:
            self.new_port = m.get('NewPort')

        if m.get('OldPort') is not None:
            self.old_port = m.get('OldPort')

        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        return self

