# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRouteMapRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        match_conditions_shrink: str = None,
        name: str = None,
        priority: int = None,
        route_map_rule_id: str = None,
        set_actions_shrink: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # The detailed description of the rule. The description can be empty or 1 to 256 characters in length, and cannot start with http:// or https://.
        self.description = description
        # Specifies whether to precheck only this request. Valid values:
        # 
        # - **true**: prechecks the request without updating the route map rule. The system checks whether required parameters are set, the request format, and service limits. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # - **false** (default): sends the request. If the request passes the precheck, the route map rule is updated.
        self.dry_run = dry_run
        # The match conditions of the route map rule. The system performs the actions defined in **SetActions** only when a route meets all the match conditions defined in this parameter.
        self.match_conditions_shrink = match_conditions_shrink
        # The name of the rule for easy identification. The name can be empty or 1 to 128 characters in length, and cannot start with http:// or https://.
        self.name = name
        # The priority of the rule. A smaller value indicates a higher priority.
        self.priority = priority
        # The ID of the route map rule to be updated.
        self.route_map_rule_id = route_map_rule_id
        # The actions to be performed for the route map rule. After a route meets all the match conditions defined in **MatchConditions**, the system processes the route based on the actions defined in this parameter.
        self.set_actions_shrink = set_actions_shrink

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

        if self.match_conditions_shrink is not None:
            result['MatchConditions'] = self.match_conditions_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.route_map_rule_id is not None:
            result['RouteMapRuleId'] = self.route_map_rule_id

        if self.set_actions_shrink is not None:
            result['SetActions'] = self.set_actions_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('MatchConditions') is not None:
            self.match_conditions_shrink = m.get('MatchConditions')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RouteMapRuleId') is not None:
            self.route_map_rule_id = m.get('RouteMapRuleId')

        if m.get('SetActions') is not None:
            self.set_actions_shrink = m.get('SetActions')

        return self

