# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModulePriceMapValue(DaraModel):
    def __init__(
        self,
        price: int = None,
        service_no: str = None,
    ):
        # The price, in cents.
        self.price = price
        # The service number, such as a flight number or train number.
        self.service_no = service_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price is not None:
            result['price'] = self.price

        if self.service_no is not None:
            result['service_no'] = self.service_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('service_no') is not None:
            self.service_no = m.get('service_no')

        return self

