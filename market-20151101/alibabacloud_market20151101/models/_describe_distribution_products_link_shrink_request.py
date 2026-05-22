# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDistributionProductsLinkShrinkRequest(DaraModel):
    def __init__(
        self,
        codes_shrink: str = None,
    ):
        # This parameter is required.
        self.codes_shrink = codes_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.codes_shrink is not None:
            result['Codes'] = self.codes_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes_shrink = m.get('Codes')

        return self

