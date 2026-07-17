# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class CreateSignalRequest(DaraModel):
    def __init__(
        self,
        signal: str = None,
        target: main_models.SignalTarget = None,
    ):
        self.signal = signal
        self.target = target

    def validate(self):
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.signal is not None:
            result['Signal'] = self.signal

        if self.target is not None:
            result['Target'] = self.target.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')

        if m.get('Target') is not None:
            temp_model = main_models.SignalTarget()
            self.target = temp_model.from_map(m.get('Target'))

        return self

