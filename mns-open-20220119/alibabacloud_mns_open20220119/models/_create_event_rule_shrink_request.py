# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEventRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        delivery_mode: str = None,
        endpoint_shrink: str = None,
        endpoints_shrink: str = None,
        event_types_shrink: str = None,
        match_rules_shrink: str = None,
        product_name: str = None,
        rule_name: str = None,
    ):
        # A client token to ensure the idempotence of the request.
        # 
        # Generate a unique value for this parameter from your client for each request.
        self.client_token = client_token
        # This parameter is deprecated.
        self.delivery_mode = delivery_mode
        # The endpoint that receives messages for this subscription.
        self.endpoint_shrink = endpoint_shrink
        # This parameter is deprecated. Use Endpoint instead.
        self.endpoints_shrink = endpoints_shrink
        # A list of event types.
        # 
        # This parameter is required.
        self.event_types_shrink = event_types_shrink
        # A list of matching rules. The logical relationship between the rules is OR.
        # 
        # This parameter is required.
        self.match_rules_shrink = match_rules_shrink
        # The name of the Alibaba Cloud product for which you want to receive event notifications.
        # 
        # This parameter is required.
        self.product_name = product_name
        # The name of the event rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.delivery_mode is not None:
            result['DeliveryMode'] = self.delivery_mode

        if self.endpoint_shrink is not None:
            result['Endpoint'] = self.endpoint_shrink

        if self.endpoints_shrink is not None:
            result['Endpoints'] = self.endpoints_shrink

        if self.event_types_shrink is not None:
            result['EventTypes'] = self.event_types_shrink

        if self.match_rules_shrink is not None:
            result['MatchRules'] = self.match_rules_shrink

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeliveryMode') is not None:
            self.delivery_mode = m.get('DeliveryMode')

        if m.get('Endpoint') is not None:
            self.endpoint_shrink = m.get('Endpoint')

        if m.get('Endpoints') is not None:
            self.endpoints_shrink = m.get('Endpoints')

        if m.get('EventTypes') is not None:
            self.event_types_shrink = m.get('EventTypes')

        if m.get('MatchRules') is not None:
            self.match_rules_shrink = m.get('MatchRules')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

