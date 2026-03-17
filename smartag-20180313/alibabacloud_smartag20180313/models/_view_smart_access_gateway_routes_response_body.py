# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class ViewSmartAccessGatewayRoutesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        routes: List[main_models.ViewSmartAccessGatewayRoutesResponseBodyRoutes] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the queried routes.
        self.routes = routes

    def validate(self):
        if self.routes:
            for v1 in self.routes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Routes'] = []
        if self.routes is not None:
            for k1 in self.routes:
                result['Routes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.routes = []
        if m.get('Routes') is not None:
            for k1 in m.get('Routes'):
                temp_model = main_models.ViewSmartAccessGatewayRoutesResponseBodyRoutes()
                self.routes.append(temp_model.from_map(k1))

        return self

class ViewSmartAccessGatewayRoutesResponseBodyRoutes(DaraModel):
    def __init__(
        self,
        conflict_cidrs: List[str] = None,
        cost: str = None,
        dst: str = None,
        idx: int = None,
        nexthop: str = None,
        role: str = None,
        type: str = None,
    ):
        # The CIDR blocks that overlap with each other.
        self.conflict_cidrs = conflict_cidrs
        # The route cost.
        # 
        # The first **0** represents the administrative distance (AD).
        # 
        # The second **0** represents the router metric.
        self.cost = cost
        # The destination CIDR block.
        self.dst = dst
        # The port number. A value of -1 indicates that the next hop points to a VPN tunnel.
        # 
        # Valid values: **-1** to **4294967295**.
        self.idx = idx
        # The next hop.
        self.nexthop = nexthop
        # The port role.
        self.role = role
        # The route type. Valid values:
        # 
        # *   **static**
        # *   **bgp**
        # *   **ospf**
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conflict_cidrs is not None:
            result['ConflictCidrs'] = self.conflict_cidrs

        if self.cost is not None:
            result['Cost'] = self.cost

        if self.dst is not None:
            result['Dst'] = self.dst

        if self.idx is not None:
            result['Idx'] = self.idx

        if self.nexthop is not None:
            result['Nexthop'] = self.nexthop

        if self.role is not None:
            result['Role'] = self.role

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConflictCidrs') is not None:
            self.conflict_cidrs = m.get('ConflictCidrs')

        if m.get('Cost') is not None:
            self.cost = m.get('Cost')

        if m.get('Dst') is not None:
            self.dst = m.get('Dst')

        if m.get('Idx') is not None:
            self.idx = m.get('Idx')

        if m.get('Nexthop') is not None:
            self.nexthop = m.get('Nexthop')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

