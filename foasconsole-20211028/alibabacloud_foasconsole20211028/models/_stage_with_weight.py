# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StageWithWeight(DaraModel):
    def __init__(
        self,
        step_index: int = None,
        step_name: str = None,
        weight: int = None,
    ):
        self.step_index = step_index
        self.step_name = step_name
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.step_index is not None:
            result['StepIndex'] = self.step_index

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StepIndex') is not None:
            self.step_index = m.get('StepIndex')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

