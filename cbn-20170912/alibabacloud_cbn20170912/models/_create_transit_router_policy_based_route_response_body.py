# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTransitRouterPolicyBasedRouteResponseBody(DaraModel):
    def __init__(
        self,
        policy_based_route_id: str = None,
        request_id: str = None,
    ):
        # The instance ID of the policy-based routing rule.
        self.policy_based_route_id = policy_based_route_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_based_route_id is not None:
            result['PolicyBasedRouteId'] = self.policy_based_route_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyBasedRouteId') is not None:
            self.policy_based_route_id = m.get('PolicyBasedRouteId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

