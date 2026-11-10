# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel



class InvokeDataProductRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        product_code: str = None,
        service_parameters: str = None,
    ):
        self.client_token = client_token
        self.product_code = product_code
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.product_code is not None:
            result['productCode'] = self.product_code

        if self.service_parameters is not None:
            result['serviceParameters'] = self.service_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')

        if m.get('serviceParameters') is not None:
            self.service_parameters = m.get('serviceParameters')

        return self

