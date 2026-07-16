# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGatewayIntranetLinkedVpcPeerRequest(DaraModel):
    def __init__(
        self,
        vpc_id: str = None,
    ):
        # The ID of the attached virtual private cloud (VPC). For more information, see [ListGatewayIntranetLinkedVpc](https://help.aliyun.com/document_detail/2621223.html).
        # 
        # - Specify a VPC ID to query only the VPC peers for that VPC.
        # 
        # - If you do not specify a VPC ID, all VPC peers are returned.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

