# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataMaskingAccountCountRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        product_ids: str = None,
    ):
        self.lang = lang
        self.product_ids = product_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.product_ids is not None:
            result['ProductIds'] = self.product_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProductIds') is not None:
            self.product_ids = m.get('ProductIds')

        return self

