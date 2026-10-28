# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class RLProgressStages(DaraModel):
    def __init__(
        self,
        current_index: int = None,
        mode: str = None,
        stages: List[main_models.RLProgressStage] = None,
        step_done: bool = None,
    ):
        # The index of the current stage.
        self.current_index = current_index
        # The disagg, colocate, or empty string.
        self.mode = mode
        # The list of stages in pipeline order.
        self.stages = stages
        # Indicates whether the stage pipeline for this step is completed.
        self.step_done = step_done

    def validate(self):
        if self.stages:
            for v1 in self.stages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_index is not None:
            result['CurrentIndex'] = self.current_index

        if self.mode is not None:
            result['Mode'] = self.mode

        result['Stages'] = []
        if self.stages is not None:
            for k1 in self.stages:
                result['Stages'].append(k1.to_map() if k1 else None)

        if self.step_done is not None:
            result['StepDone'] = self.step_done

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentIndex') is not None:
            self.current_index = m.get('CurrentIndex')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        self.stages = []
        if m.get('Stages') is not None:
            for k1 in m.get('Stages'):
                temp_model = main_models.RLProgressStage()
                self.stages.append(temp_model.from_map(k1))

        if m.get('StepDone') is not None:
            self.step_done = m.get('StepDone')

        return self

