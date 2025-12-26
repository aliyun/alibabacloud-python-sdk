# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddressCompareIntlRequest(DaraModel):
    def __init__(
        self,
        default_country: str = None,
        product_code: str = None,
        text_1: str = None,
        text_2: str = None,
    ):
        # Country name
        # - China
        # 
        # This parameter is required.
        self.default_country = default_country
        # ADD_VERIFY
        # 
        # This parameter is required.
        self.product_code = product_code
        # Address 1
        # 
        # This parameter is required.
        self.text_1 = text_1
        # Address 2
        # 
        # This parameter is required.
        self.text_2 = text_2

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_country is not None:
            result['DefaultCountry'] = self.default_country

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.text_1 is not None:
            result['Text1'] = self.text_1

        if self.text_2 is not None:
            result['Text2'] = self.text_2

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCountry') is not None:
            self.default_country = m.get('DefaultCountry')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Text1') is not None:
            self.text_1 = m.get('Text1')

        if m.get('Text2') is not None:
            self.text_2 = m.get('Text2')

        return self

