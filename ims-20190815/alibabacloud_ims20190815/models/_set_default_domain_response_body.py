# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDefaultDomainResponseBody(DaraModel):
    def __init__(
        self,
        default_domain_name: str = None,
        request_id: str = None,
    ):
        # The default domain name.
        self.default_domain_name = default_domain_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultDomainName') is not None:
            self.default_domain_name = m.get('DefaultDomainName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

