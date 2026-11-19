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
        # The client token that is used to ensure the idempotence of the request. You can generate a value for this parameter on the client side and ensure that the value is unique across different requests.
        self.client_token = client_token
        # **[Deprecated]** This field is deprecated.
        self.delivery_mode = delivery_mode
        # The endpoint that receives messages for this subscription.
        self.endpoint = endpoint
        # **[Deprecated]** This field is deprecated. Use the Endpoint parameter instead.
        self.endpoints = endpoints
        # The list of event types. Valid values depend on the selected cloud service. For example, if OSS is selected, common values include ObjectCreated:PutObject and ObjectRemoved:DeleteObject. For more information, see the event notification documentation for each cloud service.
        # 
        # This parameter is required.
        self.event_types = event_types
        # The list of matching rules. A maximum of 10 rules can be specified at the outer level. The rules are connected by the OR operator.
        # 
        # This parameter is required.
        self.match_rules = match_rules
        # The name of the cloud service for event notification. Currently, only OSS is supported.
        # 
        # This parameter is required.
        self.product_name = product_name
        # The name of the event notification rule. This parameter is required.
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
        # **[Deprecated]** This field is deprecated. Use Endpoint.EndpointType instead.
        self.endpoint_type = endpoint_type
        # **[Deprecated]** This field is deprecated. Use Endpoint.EndpointValue instead.
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
        endpoint_role_name: str = None,
        endpoint_type: str = None,
        endpoint_value: str = None,
    ):
        # The ARN of the role for cross-account delivery. This parameter is required when EndpointType is set to queue and EndpointValue is set to the ARN of a cross-account queue, which means the account that owns the queue is different from the current account. Format: acs:ram::<UID of the account that owns the queue>:role/<Role name>. The role must be created by the account that owns the queue. The trust policy must allow the delivery account to assume the role, and the role must be granted permissions to send messages to the destination queue.
        self.endpoint_role_name = endpoint_role_name
        # The endpoint type. Valid values:
        # 
        # - **topic**: Topic type. Topics support delivery to multiple subscription endpoints. You can add or remove subscription endpoints later.
        # - **queue**: Queue type. Messages are delivered directly to the queue. This reduces the routing path, but you cannot add new subscription endpoints later.
        self.endpoint_type = endpoint_type
        # The actual value of the endpoint. If EndpointType is set to topic, this parameter specifies the topic name. If EndpointType is set to queue, this parameter specifies the queue name.
        self.endpoint_value = endpoint_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_role_name is not None:
            result['EndpointRoleName'] = self.endpoint_role_name

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.endpoint_value is not None:
            result['EndpointValue'] = self.endpoint_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointRoleName') is not None:
            self.endpoint_role_name = m.get('EndpointRoleName')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('EndpointValue') is not None:
            self.endpoint_value = m.get('EndpointValue')

        return self

