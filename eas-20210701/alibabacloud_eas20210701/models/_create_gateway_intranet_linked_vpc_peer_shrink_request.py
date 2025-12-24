# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGatewayIntranetLinkedVpcPeerShrinkRequest(DaraModel):
    def __init__(
        self,
        peer_vpcs_shrink: str = None,
        vpc_id: str = None,
    ):
        # The list of VPC peers.
        self.peer_vpcs_shrink = peer_vpcs_shrink
        # The VPC ID. To obtain the VPC ID, see [ListGatewayIntranetLinkedVpc](https://help.aliyun.com/document_detail/2621223.html).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.peer_vpcs_shrink is not None:
            result['PeerVpcs'] = self.peer_vpcs_shrink

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeerVpcs') is not None:
            self.peer_vpcs_shrink = m.get('PeerVpcs')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

