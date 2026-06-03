# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckDomainResponseBody(DaraModel):
    def __init__(
        self,
        avail: str = None,
        domain_name: str = None,
        dynamic_check: bool = None,
        premium: str = None,
        price: int = None,
        reason: str = None,
        request_id: str = None,
    ):
        self.avail = avail
        self.domain_name = domain_name
        self.dynamic_check = dynamic_check
        self.premium = premium
        self.price = price
        self.reason = reason
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avail is not None:
            result['Avail'] = self.avail

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.dynamic_check is not None:
            result['DynamicCheck'] = self.dynamic_check

        if self.premium is not None:
            result['Premium'] = self.premium

        if self.price is not None:
            result['Price'] = self.price

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avail') is not None:
            self.avail = m.get('Avail')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DynamicCheck') is not None:
            self.dynamic_check = m.get('DynamicCheck')

        if m.get('Premium') is not None:
            self.premium = m.get('Premium')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

