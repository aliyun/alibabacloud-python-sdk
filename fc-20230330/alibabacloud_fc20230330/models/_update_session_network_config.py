# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class UpdateSessionNetworkConfig(DaraModel):
    def __init__(
        self,
        allow_out: List[str] = None,
        deny_out: List[str] = None,
        rules: Dict[str, List[main_models.SessionNetworkRule]] = None,
    ):
        self.allow_out = allow_out
        self.deny_out = deny_out
        # The request transform rules configured by exact target host. If omitted, existing rules are retained. An empty object clears all rules, and a non-empty object replaces all rules entirely. Null is not supported. The transform.headers and transform.headerValueReplacements fields are supported.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_out is not None:
            result['allowOut'] = self.allow_out

        if self.deny_out is not None:
            result['denyOut'] = self.deny_out

        result['rules'] = {}
        if self.rules is not None:
            for k1, v1 in self.rules.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['rules'][k1] = l1

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowOut') is not None:
            self.allow_out = m.get('allowOut')

        if m.get('denyOut') is not None:
            self.deny_out = m.get('denyOut')

        self.rules = {}
        if m.get('rules') is not None:
            for k1, v1 in m.get('rules').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.SessionNetworkRule()
                    l1.append(temp_model.from_map(k2))
                self.rules[k1] = l1

        return self

