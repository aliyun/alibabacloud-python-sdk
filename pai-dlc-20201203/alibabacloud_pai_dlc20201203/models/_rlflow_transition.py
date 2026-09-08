# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class RLFlowTransition(DaraModel):
    def __init__(
        self,
        avg: float = None,
        count: int = None,
        key: str = None,
        label: str = None,
        max: float = None,
        p_50: float = None,
        p_90: float = None,
        p_99: float = None,
        slowest: List[main_models.RLFlowSlowestItem] = None,
    ):
        # The average duration in seconds.
        self.avg = avg
        # The number of trajectories included in the statistics.
        self.count = count
        # The phase identifier. Valid values: dispatch_wait, start_wait, env_prepare, generation, agent_finish, reward, buffer_wait, logprob, ref_logprob, advantage, update, and e2e.
        self.key = key
        # The Chinese name of the phase.
        self.label = label
        # The maximum duration in seconds.
        self.max = max
        # The P50 duration in seconds.
        self.p_50 = p_50
        # The P90 duration in seconds.
        self.p_90 = p_90
        # The P99 duration in seconds.
        self.p_99 = p_99
        # The slowest 5 trajectories.
        self.slowest = slowest

    def validate(self):
        if self.slowest:
            for v1 in self.slowest:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg is not None:
            result['Avg'] = self.avg

        if self.count is not None:
            result['Count'] = self.count

        if self.key is not None:
            result['Key'] = self.key

        if self.label is not None:
            result['Label'] = self.label

        if self.max is not None:
            result['Max'] = self.max

        if self.p_50 is not None:
            result['P50'] = self.p_50

        if self.p_90 is not None:
            result['P90'] = self.p_90

        if self.p_99 is not None:
            result['P99'] = self.p_99

        result['Slowest'] = []
        if self.slowest is not None:
            for k1 in self.slowest:
                result['Slowest'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avg') is not None:
            self.avg = m.get('Avg')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('P50') is not None:
            self.p_50 = m.get('P50')

        if m.get('P90') is not None:
            self.p_90 = m.get('P90')

        if m.get('P99') is not None:
            self.p_99 = m.get('P99')

        self.slowest = []
        if m.get('Slowest') is not None:
            for k1 in m.get('Slowest'):
                temp_model = main_models.RLFlowSlowestItem()
                self.slowest.append(temp_model.from_map(k1))

        return self

