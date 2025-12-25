# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddLogicTableRouteConfigRequest(DaraModel):
    def __init__(
        self,
        route_expr: str = None,
        route_key: str = None,
        table_id: int = None,
        tid: int = None,
    ):
        # The routing algorithm expression. For more information about how to configure a routing algorithm expression, see [Configure a routing algorithm](https://www.alibabacloud.com/help/en/data-management-service/latest/configure-a-routing-algorithm).
        # 
        # This parameter is required.
        self.route_expr = route_expr
        # The unique key of the routing algorithm. 
        # 
        # > - You can create a custom unique key for the routing algorithm. No requirements are imposed on custom unique keys.
        # > - The unique key of the routing algorithm in the same logical table must be unique.
        # 
        # This parameter is required.
        self.route_key = route_key
        # The ID of the logical table. You can call the [ListLogicTables](https://www.alibabacloud.com/help/en/data-management-service/latest/listlogictables) operation to query the ID of the logical table.
        # 
        # This parameter is required.
        self.table_id = table_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://www.alibabacloud.com/help/en/data-management-service/latest/getuseractivetenant) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_expr is not None:
            result['RouteExpr'] = self.route_expr

        if self.route_key is not None:
            result['RouteKey'] = self.route_key

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteExpr') is not None:
            self.route_expr = m.get('RouteExpr')

        if m.get('RouteKey') is not None:
            self.route_key = m.get('RouteKey')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

