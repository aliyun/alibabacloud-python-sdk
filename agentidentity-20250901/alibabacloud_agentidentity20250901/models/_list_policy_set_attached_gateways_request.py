# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPolicySetAttachedGatewaysRequest(DaraModel):
    def __init__(
        self,
        gateway_type: str = None,
        max_results: int = None,
        next_token: str = None,
        policy_set_name: str = None,
    ):
        self.gateway_type = gateway_type
        self.max_results = max_results
        self.next_token = next_token
        self.policy_set_name = policy_set_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.policy_set_name is not None:
            result['PolicySetName'] = self.policy_set_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PolicySetName') is not None:
            self.policy_set_name = m.get('PolicySetName')

        return self

