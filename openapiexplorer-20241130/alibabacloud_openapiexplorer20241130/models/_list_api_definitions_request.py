# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApiDefinitionsRequest(DaraModel):
    def __init__(
        self,
        api_version: str = None,
        product: str = None,
    ):
        # This parameter is required.
        self.api_version = api_version
        # This parameter is required.
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        if self.product is not None:
            result['product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('product') is not None:
            self.product = m.get('product')

        return self

