# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSecurityAgentStatusResponseBody(DaraModel):
    def __init__(
        self,
        client_status: str = None,
        request_id: str = None,
    ):
        # The status of the Security Center agent. Valid values:
        # 
        # - pause: The Security Center agent suspends protection for your server.
        # 
        # - online: The Security Center agent is protecting your server.
        # 
        # - offline: The Security Center agent does not protect your server.
        self.client_status = client_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_status is not None:
            result['ClientStatus'] = self.client_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientStatus') is not None:
            self.client_status = m.get('ClientStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

