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
        # The client token that is used to ensure the idempotence of the request. You can generate a value for this parameter on the client side and ensure that the value is unique across different requests.
        self.client_token = client_token
        # **[Deprecated]** This field is deprecated.
        self.delivery_mode = delivery_mode
        # The endpoint that receives messages for this subscription.
        self.endpoint_shrink = endpoint_shrink
        # **[Deprecated]** This field is deprecated. Use the Endpoint parameter instead.
        self.endpoints_shrink = endpoints_shrink
        # The list of event types. Valid values depend on the selected cloud service. For example, if OSS is selected, common values include ObjectCreated:PutObject and ObjectRemoved:DeleteObject. For more information, see the event notification documentation for each cloud service.
        # 
        # This parameter is required.
        self.event_types_shrink = event_types_shrink
        # The list of matching rules. A maximum of 10 rules can be specified at the outer level. The rules are connected by the OR operator.
        # 
        # This parameter is required.
        self.match_rules_shrink = match_rules_shrink
        # The name of the cloud service for event notification. Currently, only OSS is supported.
        # 
        # This parameter is required.
        self.product_name = product_name
        # The name of the event notification rule. This parameter is required.
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

