# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLProgressConfig(DaraModel):
    def __init__(
        self,
        num_minibatches: int = None,
        ppo_mini_batch_size: int = None,
        rollout_n: int = None,
        total_steps: int = None,
        train_batch_size: int = None,
    ):
        # The number of mini-batches per step.
        self.num_minibatches = num_minibatches
        # The PPO mini-batch size.
        self.ppo_mini_batch_size = ppo_mini_batch_size
        # The number of rollouts per prompt.
        self.rollout_n = rollout_n
        # The total number of training steps.
        self.total_steps = total_steps
        # The training batch size.
        self.train_batch_size = train_batch_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.num_minibatches is not None:
            result['NumMinibatches'] = self.num_minibatches

        if self.ppo_mini_batch_size is not None:
            result['PpoMiniBatchSize'] = self.ppo_mini_batch_size

        if self.rollout_n is not None:
            result['RolloutN'] = self.rollout_n

        if self.total_steps is not None:
            result['TotalSteps'] = self.total_steps

        if self.train_batch_size is not None:
            result['TrainBatchSize'] = self.train_batch_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NumMinibatches') is not None:
            self.num_minibatches = m.get('NumMinibatches')

        if m.get('PpoMiniBatchSize') is not None:
            self.ppo_mini_batch_size = m.get('PpoMiniBatchSize')

        if m.get('RolloutN') is not None:
            self.rollout_n = m.get('RolloutN')

        if m.get('TotalSteps') is not None:
            self.total_steps = m.get('TotalSteps')

        if m.get('TrainBatchSize') is not None:
            self.train_batch_size = m.get('TrainBatchSize')

        return self

