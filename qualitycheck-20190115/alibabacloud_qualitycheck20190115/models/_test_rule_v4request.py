# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TestRuleV4Request(DaraModel):
    def __init__(
        self,
        is_scheme_data: int = None,
        test_json: str = None,
    ):
        self.is_scheme_data = is_scheme_data
        # This parameter is required.
        self.test_json = test_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_scheme_data is not None:
            result['IsSchemeData'] = self.is_scheme_data

        if self.test_json is not None:
            result['TestJson'] = self.test_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSchemeData') is not None:
            self.is_scheme_data = m.get('IsSchemeData')

        if m.get('TestJson') is not None:
            self.test_json = m.get('TestJson')

        return self

