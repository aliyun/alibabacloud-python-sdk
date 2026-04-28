# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAdvisorChecksRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        product: str = None,
    ):
        self.language = language
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.product is not None:
            result['Product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        return self

