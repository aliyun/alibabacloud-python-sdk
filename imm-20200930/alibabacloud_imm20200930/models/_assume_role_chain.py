# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class AssumeRoleChain(DaraModel):
    def __init__(
        self,
        chain: List[main_models.AssumeRoleChainNode] = None,
        policy: str = None,
    ):
        # The authorization chains.
        self.chain = chain
        # The policy.
        self.policy = policy

    def validate(self):
        if self.chain:
            for v1 in self.chain:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Chain'] = []
        if self.chain is not None:
            for k1 in self.chain:
                result['Chain'].append(k1.to_map() if k1 else None)

        if self.policy is not None:
            result['Policy'] = self.policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chain = []
        if m.get('Chain') is not None:
            for k1 in m.get('Chain'):
                temp_model = main_models.AssumeRoleChainNode()
                self.chain.append(temp_model.from_map(k1))

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        return self

