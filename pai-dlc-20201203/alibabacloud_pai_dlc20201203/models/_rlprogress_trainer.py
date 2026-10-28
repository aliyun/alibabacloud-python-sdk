# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class RLProgressTrainer(DaraModel):
    def __init__(
        self,
        micro: main_models.RLProgressMicro = None,
        mini_idx: int = None,
        num_minibatches: int = None,
        sync: main_models.RLProgressSync = None,
    ):
        # The micro-batch progress.
        self.micro = micro
        # The current mini-batch ordinal number.
        self.mini_idx = mini_idx
        # The total number of mini-batches.
        self.num_minibatches = num_minibatches
        # The parameter synchronization status.
        self.sync = sync

    def validate(self):
        if self.micro:
            self.micro.validate()
        if self.sync:
            self.sync.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.micro is not None:
            result['Micro'] = self.micro.to_map()

        if self.mini_idx is not None:
            result['MiniIdx'] = self.mini_idx

        if self.num_minibatches is not None:
            result['NumMinibatches'] = self.num_minibatches

        if self.sync is not None:
            result['Sync'] = self.sync.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Micro') is not None:
            temp_model = main_models.RLProgressMicro()
            self.micro = temp_model.from_map(m.get('Micro'))

        if m.get('MiniIdx') is not None:
            self.mini_idx = m.get('MiniIdx')

        if m.get('NumMinibatches') is not None:
            self.num_minibatches = m.get('NumMinibatches')

        if m.get('Sync') is not None:
            temp_model = main_models.RLProgressSync()
            self.sync = temp_model.from_map(m.get('Sync'))

        return self

