# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDomainExtensionResponseBody(DaraModel):
    def __init__(
        self,
        domain_extension_id: str = None,
        listener_port: int = None,
        request_id: str = None,
    ):
        # The ID of the additional domain name.
        self.domain_extension_id = domain_extension_id
        # The frontend port that is used by the SLB instance.
        self.listener_port = listener_port
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_extension_id is not None:
            result['DomainExtensionId'] = self.domain_extension_id

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainExtensionId') is not None:
            self.domain_extension_id = m.get('DomainExtensionId')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

