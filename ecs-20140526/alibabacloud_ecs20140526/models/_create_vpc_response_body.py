# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpcResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        route_table_id: str = None,
        vrouter_id: str = None,
        vpc_id: str = None,
    ):
        self.request_id = request_id
        self.route_table_id = route_table_id
        self.vrouter_id = vrouter_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.vrouter_id is not None:
            result['VRouterId'] = self.vrouter_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

