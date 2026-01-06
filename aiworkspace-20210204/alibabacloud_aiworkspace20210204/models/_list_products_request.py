# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductsRequest(DaraModel):
    def __init__(
        self,
        product_codes: str = None,
        service_codes: str = None,
        verbose: bool = None,
    ):
        self.product_codes = product_codes
        self.service_codes = service_codes
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_codes is not None:
            result['ProductCodes'] = self.product_codes

        if self.service_codes is not None:
            result['ServiceCodes'] = self.service_codes

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCodes') is not None:
            self.product_codes = m.get('ProductCodes')

        if m.get('ServiceCodes') is not None:
            self.service_codes = m.get('ServiceCodes')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        return self

