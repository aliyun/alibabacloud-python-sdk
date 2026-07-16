# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDistributionProductsLinkRequest(DaraModel):
    def __init__(
        self,
        codes: List[str] = None,
    ):
        # This parameter is required.
        self.codes = codes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.codes is not None:
            result['Codes'] = self.codes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes = m.get('Codes')

        return self

