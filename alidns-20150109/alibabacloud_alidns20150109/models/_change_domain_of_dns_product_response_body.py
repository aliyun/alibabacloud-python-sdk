# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeDomainOfDnsProductResponseBody(DaraModel):
    def __init__(
        self,
        original_domain: str = None,
        request_id: str = None,
    ):
        # The domain name that is originally bound to the instance. If no value is returned for this parameter, the instance is bound to a domain name for the first time.
        self.original_domain = original_domain
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.original_domain is not None:
            result['OriginalDomain'] = self.original_domain

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginalDomain') is not None:
            self.original_domain = m.get('OriginalDomain')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

