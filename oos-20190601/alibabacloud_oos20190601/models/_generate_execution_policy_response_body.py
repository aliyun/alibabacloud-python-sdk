# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateExecutionPolicyResponseBody(DaraModel):
    def __init__(
        self,
        missing_policy: str = None,
        policy: str = None,
        request_id: str = None,
    ):
        # The policies that are missing.
        self.missing_policy = missing_policy
        # The RAM policy.
        self.policy = policy
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.missing_policy is not None:
            result['MissingPolicy'] = self.missing_policy

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MissingPolicy') is not None:
            self.missing_policy = m.get('MissingPolicy')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

