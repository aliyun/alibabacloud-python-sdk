# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTransitRouterPolicyTableResponseBody(DaraModel):
    def __init__(
        self,
        policy_table_id: str = None,
        request_id: str = None,
    ):
        # The ID of the policy route table.
        self.policy_table_id = policy_table_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_table_id is not None:
            result['PolicyTableId'] = self.policy_table_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyTableId') is not None:
            self.policy_table_id = m.get('PolicyTableId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

