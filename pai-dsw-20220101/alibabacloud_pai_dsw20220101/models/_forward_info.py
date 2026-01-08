# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ForwardInfo(DaraModel):
    def __init__(
        self,
        access_type: List[str] = None,
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
        self.container_name = container_name
        self.eip_allocation_id = eip_allocation_id
        self.enable = enable
        self.external_port = external_port
        self.forward_port = forward_port
        self.name = name
        self.nat_gateway_id = nat_gateway_id
        self.sshpublic_key = sshpublic_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

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

