# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRouteMapRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        name: str = None,
        priority: int = None,
        route_map_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request may be different.
        self.client_token = client_token
        # The description of the route map.
        # 
        # The description can be empty or 1 to 256 characters in length. It cannot start with http:// or https://.
        self.description = description
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: prechecks the request without updating the route map. The system checks whether required parameters are specified, the request format is valid, and the service limits are met. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the DryRunOperation error code is returned.
        # - **false** (default): sends the request. If the request passes the precheck, the route map is updated.
        self.dry_run = dry_run
        # The name of the route map.
        # 
        # The name can be empty or 1 to 128 characters in length. It cannot start with http:// or https://.
        self.name = name
        # Policy priority of the route map. Valid values: **1** to **100**. A smaller value indicates a higher priority.
        # 
        # > Policy priority of each route map within an Alibaba Cloud account must be unique. When a route map is applied, the system starts to match routes against the rules of the route map that has the highest priority (the smallest priority value) and then proceeds to route maps with lower priorities based on the rule priorities. Therefore, when you specify policy priority of a route map, make sure that policy priority meets your expected matching order.
        self.priority = priority
        # The ID of the route map.
        # 
        # This parameter is required.
        self.route_map_id = route_map_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')

        return self

