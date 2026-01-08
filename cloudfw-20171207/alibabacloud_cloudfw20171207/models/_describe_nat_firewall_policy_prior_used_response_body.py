# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNatFirewallPolicyPriorUsedResponseBody(DaraModel):
    def __init__(
        self,
        end: int = None,
        request_id: str = None,
        start: int = None,
    ):
        # The lowest priority for the access control policy.
        self.end = end
        # The request ID.
        self.request_id = request_id
        # The highest priority for the access control policy.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

