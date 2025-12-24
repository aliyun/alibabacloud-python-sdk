# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class ListGatewayIntranetLinkedVpcPeerResponseBody(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        peer_vpc_list: List[main_models.ListGatewayIntranetLinkedVpcPeerResponseBodyPeerVpcList] = None,
        request_id: str = None,
    ):
        # The ID of the private gateway.
        self.gateway_id = gateway_id
        # The VPC peers.
        self.peer_vpc_list = peer_vpc_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.peer_vpc_list:
            for v1 in self.peer_vpc_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        result['PeerVpcList'] = []
        if self.peer_vpc_list is not None:
            for k1 in self.peer_vpc_list:
                result['PeerVpcList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        self.peer_vpc_list = []
        if m.get('PeerVpcList') is not None:
            for k1 in m.get('PeerVpcList'):
                temp_model = main_models.ListGatewayIntranetLinkedVpcPeerResponseBodyPeerVpcList()
                self.peer_vpc_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListGatewayIntranetLinkedVpcPeerResponseBodyPeerVpcList(DaraModel):
    def __init__(
        self,
        peer_vpcs: List[main_models.ListGatewayIntranetLinkedVpcPeerResponseBodyPeerVpcListPeerVpcs] = None,
        vpc_id: str = None,
    ):
        # The IDs of the VPC peers.
        self.peer_vpcs = peer_vpcs
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.peer_vpcs:
            for v1 in self.peer_vpcs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PeerVpcs'] = []
        if self.peer_vpcs is not None:
            for k1 in self.peer_vpcs:
                result['PeerVpcs'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.peer_vpcs = []
        if m.get('PeerVpcs') is not None:
            for k1 in m.get('PeerVpcs'):
                temp_model = main_models.ListGatewayIntranetLinkedVpcPeerResponseBodyPeerVpcListPeerVpcs()
                self.peer_vpcs.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListGatewayIntranetLinkedVpcPeerResponseBodyPeerVpcListPeerVpcs(DaraModel):
    def __init__(
        self,
        region: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        # The region where the VPC peer resides.
        self.region = region
        self.status = status
        # The ID of the VPC peer.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region is not None:
            result['Region'] = self.region

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

