# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFixedPriceDemandOrderRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        contact_id: str = None,
        domain: str = None,
        source: str = None,
    ):
        self.code = code
        self.contact_id = contact_id
        self.domain = domain
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

