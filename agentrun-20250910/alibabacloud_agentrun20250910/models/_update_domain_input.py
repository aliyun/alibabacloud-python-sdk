# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDomainInput(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        protocol: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

