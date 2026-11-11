# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRouteMapRuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        route_map_rule_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate a parameter value on your client to ensure that the value is unique across different requests. The ClientToken parameter supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run on the request. Valid values:
        # 
        # - **true**: performs a dry run and does not delete the route map rule. The system checks whether required parameters are specified, the request format is valid, and service limits are met. If the check fails, the system returns an error. If the check succeeds, the system returns the error code `DryRunOperation`.
        # - **false** (default): sends a regular request and deletes the route map rule if the dry run succeeds.
        self.dry_run = dry_run
        # The ID of the route map rule to delete.
        # 
        # This parameter is required.
        self.route_map_rule_id = route_map_rule_id

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

        if self.route_map_rule_id is not None:
            result['RouteMapRuleId'] = self.route_map_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RouteMapRuleId') is not None:
            self.route_map_rule_id = m.get('RouteMapRuleId')

        return self

