# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnWafDefaultRulesRequest(DaraModel):
    def __init__(
        self,
        query_args: str = None,
    ):
        # The query conditions. The value is a string in the JSON format. Format: `QueryArgs={"DefenseScene":"anti_scan"}`
        self.query_args = query_args

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_args is not None:
            result['QueryArgs'] = self.query_args

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryArgs') is not None:
            self.query_args = m.get('QueryArgs')

        return self

