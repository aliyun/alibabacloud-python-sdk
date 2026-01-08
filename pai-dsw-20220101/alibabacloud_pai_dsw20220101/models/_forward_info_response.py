# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class ForwardInfoResponse(DaraModel):
    def __init__(
        self,
        access_type: List[str] = None,
        connect_info: main_models.ForwardInfoResponseConnectInfo = None,
        container_name: str = None,
        eip_allocation_id: str = None,
        enable: bool = None,
        external_port: str = None,
        forward_port: str = None,
        name: str = None,
        nat_gateway_id: str = None,
        sshpublic_key: str = None,
    ):
        self.access_type = access_type
        self.connect_info = connect_info
        self.container_name = container_name
        self.eip_allocation_id = eip_allocation_id
        self.enable = enable
        self.external_port = external_port
        self.forward_port = forward_port
        self.name = name
        self.nat_gateway_id = nat_gateway_id
        self.sshpublic_key = sshpublic_key

    def validate(self):
        if self.connect_info:
            self.connect_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.connect_info is not None:
            result['ConnectInfo'] = self.connect_info.to_map()

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.eip_allocation_id is not None:
            result['EipAllocationId'] = self.eip_allocation_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.external_port is not None:
            result['ExternalPort'] = self.external_port

        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port

        if self.name is not None:
            result['Name'] = self.name

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.sshpublic_key is not None:
            result['SSHPublicKey'] = self.sshpublic_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('ConnectInfo') is not None:
            temp_model = main_models.ForwardInfoResponseConnectInfo()
            self.connect_info = temp_model.from_map(m.get('ConnectInfo'))

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('EipAllocationId') is not None:
            self.eip_allocation_id = m.get('EipAllocationId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')

        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('SSHPublicKey') is not None:
            self.sshpublic_key = m.get('SSHPublicKey')

        return self

class ForwardInfoResponseConnectInfo(DaraModel):
    def __init__(
        self,
        internet: main_models.ForwardInfoResponseConnectInfoInternet = None,
        intranet: main_models.ForwardInfoResponseConnectInfoIntranet = None,
        message: str = None,
        phase: str = None,
    ):
        self.internet = internet
        self.intranet = intranet
        self.message = message
        self.phase = phase

    def validate(self):
        if self.internet:
            self.internet.validate()
        if self.intranet:
            self.intranet.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet is not None:
            result['Internet'] = self.internet.to_map()

        if self.intranet is not None:
            result['Intranet'] = self.intranet.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.phase is not None:
            result['Phase'] = self.phase

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Internet') is not None:
            temp_model = main_models.ForwardInfoResponseConnectInfoInternet()
            self.internet = temp_model.from_map(m.get('Internet'))

        if m.get('Intranet') is not None:
            temp_model = main_models.ForwardInfoResponseConnectInfoIntranet()
            self.intranet = temp_model.from_map(m.get('Intranet'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        return self

class ForwardInfoResponseConnectInfoIntranet(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        port: str = None,
    ):
        self.endpoint = endpoint
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

class ForwardInfoResponseConnectInfoInternet(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        port: str = None,
    ):
        self.endpoint = endpoint
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

