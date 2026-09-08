# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLFlowTotals(DaraModel):
    def __init__(
        self,
        inflight: int = None,
        rewarded: int = None,
        sampled: int = None,
        trained: int = None,
        trajs: int = None,
        uids: int = None,
    ):
        # The number of in-flight trajectories (no desired state).
        self.inflight = inflight
        # The number of trajectories that have completed reward scoring (hit reward_score_computed).
        self.rewarded = rewarded
        # The number of trajectories sampled into a batch by the trainer (hit sampled_from_replay_buffer).
        self.sampled = sampled
        # The number of trajectories that have completed training (hit actor_parameters_updated).
        self.trained = trained
        # The total number of trajectories in the window.
        self.trajs = trajs
        # The number of sample UIDs that appear in the window.
        self.uids = uids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inflight is not None:
            result['Inflight'] = self.inflight

        if self.rewarded is not None:
            result['Rewarded'] = self.rewarded

        if self.sampled is not None:
            result['Sampled'] = self.sampled

        if self.trained is not None:
            result['Trained'] = self.trained

        if self.trajs is not None:
            result['Trajs'] = self.trajs

        if self.uids is not None:
            result['Uids'] = self.uids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Inflight') is not None:
            self.inflight = m.get('Inflight')

        if m.get('Rewarded') is not None:
            self.rewarded = m.get('Rewarded')

        if m.get('Sampled') is not None:
            self.sampled = m.get('Sampled')

        if m.get('Trained') is not None:
            self.trained = m.get('Trained')

        if m.get('Trajs') is not None:
            self.trajs = m.get('Trajs')

        if m.get('Uids') is not None:
            self.uids = m.get('Uids')

        return self

