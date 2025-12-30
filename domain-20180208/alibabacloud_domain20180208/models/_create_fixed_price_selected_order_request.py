# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFixedPriceSelectedOrderRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        contact_id: str = None,
        domain_name: str = None,
        expected_price: float = None,
        source: str = None,
    ):
        self.code = code
        # This parameter is required.
        self.contact_id = contact_id
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.expected_price = expected_price
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

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.expected_price is not None:
            result['ExpectedPrice'] = self.expected_price

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ExpectedPrice') is not None:
            self.expected_price = m.get('ExpectedPrice')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

