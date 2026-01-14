# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateCustomRoutingEndpointTrafficPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
        request_id: str = None,
    ):
        # The IDs of the traffic destinations.
        self.policy_ids = policy_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

