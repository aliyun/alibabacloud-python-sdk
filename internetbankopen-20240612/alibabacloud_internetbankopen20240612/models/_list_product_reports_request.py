# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductReportsRequest(DaraModel):
    def __init__(
        self,
        latest_only: bool = None,
        product_code: str = None,
    ):
        self.latest_only = latest_only
        # This parameter is required.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latest_only is not None:
            result['LatestOnly'] = self.latest_only

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LatestOnly') is not None:
            self.latest_only = m.get('LatestOnly')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

