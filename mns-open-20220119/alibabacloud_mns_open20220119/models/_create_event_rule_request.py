# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class CreateEventRuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        delivery_mode: str = None,
        endpoint: main_models.CreateEventRuleRequestEndpoint = None,
        endpoints: List[main_models.CreateEventRuleRequestEndpoints] = None,
        event_types: List[str] = None,
        match_rules: List[List[main_models.EventMatchRule]] = None,
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
        self.endpoint = endpoint
        # This parameter is deprecated. Use Endpoint instead.
        self.endpoints = endpoints
        # A list of event types.
        # 
        # This parameter is required.
        self.event_types = event_types
        # A list of matching rules. The logical relationship between the rules is OR.
        # 
        # This parameter is required.
        self.match_rules = match_rules
        # The name of the Alibaba Cloud product for which you want to receive event notifications.
        # 
        # This parameter is required.
        self.product_name = product_name
        # The name of the event rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        if self.endpoint:
            self.endpoint.validate()
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()
        if self.match_rules:
            for v1 in self.match_rules:
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.delivery_mode is not None:
            result['DeliveryMode'] = self.delivery_mode

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint.to_map()

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.event_types is not None:
            result['EventTypes'] = self.event_types

        result['MatchRules'] = []
        if self.match_rules is not None:
            for k1 in self.match_rules:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['MatchRules'].append(l1)

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
            temp_model = main_models.CreateEventRuleRequestEndpoint()
            self.endpoint = temp_model.from_map(m.get('Endpoint'))

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.CreateEventRuleRequestEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')

        self.match_rules = []
        if m.get('MatchRules') is not None:
            for k1 in m.get('MatchRules'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.EventMatchRule()
                    l1.append(temp_model.from_map(k2))
                self.match_rules.append(l1)

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class CreateEventRuleRequestEndpoints(DaraModel):
    def __init__(
        self,
        endpoint_type: str = None,
        endpoint_value: str = None,
    ):
        # Deprecated. Use Endpoint.EndpointType instead.
        self.endpoint_type = endpoint_type
        # Deprecated. Use Endpoint.EndpointValue instead.
        self.endpoint_value = endpoint_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.endpoint_value is not None:
            result['EndpointValue'] = self.endpoint_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('EndpointValue') is not None:
            self.endpoint_value = m.get('EndpointValue')

        return self



class CreateEventRuleRequestEndpoint(DaraModel):
    def __init__(
        self,
        endpoint_type: str = None,
        endpoint_value: str = None,
    ):
        # The endpoint type. Valid values:
        # 
        # - **topic**: The endpoint is a topic. A topic can deliver messages to multiple subscribers. You can add or remove subscribers later.
        # 
        # - **queue**: The endpoint is a queue. Messages are delivered directly to the queue. This simplifies the delivery path, but you cannot add new subscribers later.
        self.endpoint_type = endpoint_type
        # The value of the endpoint.
        self.endpoint_value = endpoint_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.endpoint_value is not None:
            result['EndpointValue'] = self.endpoint_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('EndpointValue') is not None:
            self.endpoint_value = m.get('EndpointValue')

        return self

