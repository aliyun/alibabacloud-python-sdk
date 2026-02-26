# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Schedule(DaraModel):
    def __init__(
        self,
        gamma: float = None,
        lrscheduler: str = None,
        step_size: int = None,
    ):
        # The learning rate decay. This parameter takes effect only when LRScheduler is set to StepLR.
        self.gamma = gamma
        # The learning rate scheduler.
        self.lrscheduler = lrscheduler
        # The number of epochs the learning rate is changed after. This parameter takes effect only when LRScheduler is set to StepLR.
        self.step_size = step_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gamma is not None:
            result['Gamma'] = self.gamma

        if self.lrscheduler is not None:
            result['LRScheduler'] = self.lrscheduler

        if self.step_size is not None:
            result['StepSize'] = self.step_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gamma') is not None:
            self.gamma = m.get('Gamma')

        if m.get('LRScheduler') is not None:
            self.lrscheduler = m.get('LRScheduler')

        if m.get('StepSize') is not None:
            self.step_size = m.get('StepSize')

        return self

