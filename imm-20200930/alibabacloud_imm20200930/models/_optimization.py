# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Optimization(DaraModel):
    def __init__(
        self,
        learning_rate: float = None,
        optimizer: str = None,
    ):
        # The initial learning rate.
        self.learning_rate = learning_rate
        # The optimization method.
        self.optimizer = optimizer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.learning_rate is not None:
            result['LearningRate'] = self.learning_rate

        if self.optimizer is not None:
            result['Optimizer'] = self.optimizer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LearningRate') is not None:
            self.learning_rate = m.get('LearningRate')

        if m.get('Optimizer') is not None:
            self.optimizer = m.get('Optimizer')

        return self

