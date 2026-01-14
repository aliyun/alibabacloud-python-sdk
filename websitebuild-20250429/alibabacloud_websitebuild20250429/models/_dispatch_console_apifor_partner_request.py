# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DispatchConsoleAPIForPartnerRequest(DaraModel):
    def __init__(
        self,
        live_token: str = None,
        operation: str = None,
        params: str = None,
        product: str = None,
        site_host: str = None,
    ):
        # This parameter is required.
        self.live_token = live_token
        # This parameter is required.
        self.operation = operation
        self.params = params
        # This parameter is required.
        self.product = product
        self.site_host = site_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_token is not None:
            result['LiveToken'] = self.live_token

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.params is not None:
            result['Params'] = self.params

        if self.product is not None:
            result['Product'] = self.product

        if self.site_host is not None:
            result['SiteHost'] = self.site_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveToken') is not None:
            self.live_token = m.get('LiveToken')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('SiteHost') is not None:
            self.site_host = m.get('SiteHost')

        return self

