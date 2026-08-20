# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class CreateSessionNetworkConfig(DaraModel):
    def __init__(
        self,
        allow_out: List[str] = None,
        allow_public_traffic: bool = None,
        deny_out: List[str] = None,
        mask_request_host: str = None,
        rules: Dict[str, List[main_models.SessionNetworkRule]] = None,
    ):
        self.allow_out = allow_out
        self.allow_public_traffic = allow_public_traffic
        self.deny_out = deny_out
        self.mask_request_host = mask_request_host
        # The request transform rules configured by exact target host. Supports transform.headers and transform.headerValueReplacements.
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

        if self.allow_public_traffic is not None:
            result['allowPublicTraffic'] = self.allow_public_traffic

        if self.deny_out is not None:
            result['denyOut'] = self.deny_out

        if self.mask_request_host is not None:
            result['maskRequestHost'] = self.mask_request_host

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

        if m.get('allowPublicTraffic') is not None:
            self.allow_public_traffic = m.get('allowPublicTraffic')

        if m.get('denyOut') is not None:
            self.deny_out = m.get('denyOut')

        if m.get('maskRequestHost') is not None:
            self.mask_request_host = m.get('maskRequestHost')

        self.rules = {}
        if m.get('rules') is not None:
            for k1, v1 in m.get('rules').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.SessionNetworkRule()
                    l1.append(temp_model.from_map(k2))
                self.rules[k1] = l1

        return self

