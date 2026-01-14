# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDomainStateResponseBody(DaraModel):
    def __init__(
        self,
        domain: str = None,
        request_id: str = None,
        state: str = None,
    ):
        # The accelerated domain name.
        self.domain = domain
        # The request ID.
        self.request_id = request_id
        # The ICP filing status of the accelerated domain name. Valid values:
        # 
        # *   **illegal:** The domain name is illegal.
        # *   **inactive:** The domain name has not completed ICP filing.
        # *   **active:** The domain name has a valid ICP number.
        # *   **unknown:** The ICP filing status is unknown.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

