# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckDomainResponseBody(DaraModel):
    def __init__(
        self,
        domain_status: int = None,
        request_id: str = None,
    ):
        # Domain status. Indicates whether the verification was successful, with values as follows:
        # 
        # - **0**: Available, verified successfully
        # - **1**: Unavailable, verification failed
        self.domain_status = domain_status
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

