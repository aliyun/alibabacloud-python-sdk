# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAlgorithmVersionShrinkRequest(DaraModel):
    def __init__(
        self,
        algorithm_spec_shrink: str = None,
    ):
        self.algorithm_spec_shrink = algorithm_spec_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_spec_shrink is not None:
            result['AlgorithmSpec'] = self.algorithm_spec_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmSpec') is not None:
            self.algorithm_spec_shrink = m.get('AlgorithmSpec')

        return self

