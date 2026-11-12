# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGatewayIntranetLinkedVpcPeerRequest(DaraModel):
    def __init__(
        self,
        vpc_id: str = None,
    ):
        # The ID of the associated VPC. For more information about how to query the VPC ID, see [ListGatewayIntranetLinkedVpc](https://help.aliyun.com/document_detail/2621223.html).
        # - If you specify a VPC ID, only the VPC peers associated with the specified VPC ID are queried.
        # - If you do not specify a VPC ID, all VPC peers are queried.
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

