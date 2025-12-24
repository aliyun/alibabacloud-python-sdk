# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DeleteGatewayIntranetLinkedVpcPeerRequest(DaraModel):
    def __init__(
        self,
        peer_vpcs: List[main_models.DeleteGatewayIntranetLinkedVpcPeerRequestPeerVpcs] = None,
        vpc_id: str = None,
    ):
        # The VPC peer.
        self.peer_vpcs = peer_vpcs
        # The ID of the associated VPC. To obtain the VPC ID, see [ListGatewayIntranetLinkedVpc](https://help.aliyun.com/document_detail/2621223.html).
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
                temp_model = main_models.DeleteGatewayIntranetLinkedVpcPeerRequestPeerVpcs()
                self.peer_vpcs.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DeleteGatewayIntranetLinkedVpcPeerRequestPeerVpcs(DaraModel):
    def __init__(
        self,
        region: str = None,
        vpc_id: str = None,
    ):
        # The region where the VPC peer resides.
        self.region = region
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

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

