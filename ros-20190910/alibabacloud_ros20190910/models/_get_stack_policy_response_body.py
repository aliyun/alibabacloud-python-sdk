# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetStackPolicyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stack_policy_body: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length.
        self.stack_policy_body = stack_policy_body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')

        return self

