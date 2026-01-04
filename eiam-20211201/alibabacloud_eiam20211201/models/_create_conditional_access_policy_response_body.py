# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConditionalAccessPolicyResponseBody(DaraModel):
    def __init__(
        self,
        conditional_access_policy_id: str = None,
        request_id: str = None,
    ):
        # Conditional Access Policy ID
        self.conditional_access_policy_id = conditional_access_policy_id
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conditional_access_policy_id is not None:
            result['ConditionalAccessPolicyId'] = self.conditional_access_policy_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionalAccessPolicyId') is not None:
            self.conditional_access_policy_id = m.get('ConditionalAccessPolicyId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

