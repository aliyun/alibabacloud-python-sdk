# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRouteMapRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        route_map_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate a parameter value from your client to ensure that the value is unique among different requests. The client token only supports ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: sends a check request and does not delete the route map. The system checks whether required parameters are specified, the request format, and service limits. If the check fails, the corresponding error is returned. If the check succeeds, the error code `DryRunOperation` is returned.
        # - **false** (default): sends a normal request and directly deletes the route map after the check succeeds.
        self.dry_run = dry_run
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

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')

        return self

