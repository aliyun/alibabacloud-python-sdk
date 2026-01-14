# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInvalidDomainCountResponseBody(DaraModel):
    def __init__(
        self,
        invalid_domain_count: str = None,
        request_id: str = None,
    ):
        # The number of invalid domain names.
        self.invalid_domain_count = invalid_domain_count
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invalid_domain_count is not None:
            result['InvalidDomainCount'] = self.invalid_domain_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvalidDomainCount') is not None:
            self.invalid_domain_count = m.get('InvalidDomainCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

