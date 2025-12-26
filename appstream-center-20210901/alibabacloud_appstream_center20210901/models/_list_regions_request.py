# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRegionsRequest(DaraModel):
    def __init__(
        self,
        biz_source: str = None,
        product_type: str = None,
    ):
        # >  This parameter is not publicly available.
        self.biz_source = biz_source
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_source is not None:
            result['BizSource'] = self.biz_source

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizSource') is not None:
            self.biz_source = m.get('BizSource')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

