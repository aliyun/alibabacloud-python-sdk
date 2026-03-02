# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class PdpListLogResult(DaraModel):
    def __init__(
        self,
        logs: List[main_models.PdpLog] = None,
    ):
        self.logs = logs

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['logs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logs = []
        if m.get('logs') is not None:
            for k1 in m.get('logs'):
                temp_model = main_models.PdpLog()
                self.logs.append(temp_model.from_map(k1))

        return self

