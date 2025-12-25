# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_foasconsole20211028 import models as main_models
from darabonba.model import DaraModel

class ClusterStage(DaraModel):
    def __init__(
        self,
        current_stage: int = None,
        message: str = None,
        status: str = None,
        total_stage_with_weight: List[main_models.StageWithWeight] = None,
    ):
        self.current_stage = current_stage
        self.message = message
        self.status = status
        self.total_stage_with_weight = total_stage_with_weight

    def validate(self):
        if self.total_stage_with_weight:
            for v1 in self.total_stage_with_weight:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_stage is not None:
            result['CurrentStage'] = self.current_stage

        if self.message is not None:
            result['Message'] = self.message

        if self.status is not None:
            result['Status'] = self.status

        result['TotalStageWithWeight'] = []
        if self.total_stage_with_weight is not None:
            for k1 in self.total_stage_with_weight:
                result['TotalStageWithWeight'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentStage') is not None:
            self.current_stage = m.get('CurrentStage')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.total_stage_with_weight = []
        if m.get('TotalStageWithWeight') is not None:
            for k1 in m.get('TotalStageWithWeight'):
                temp_model = main_models.StageWithWeight()
                self.total_stage_with_weight.append(temp_model.from_map(k1))

        return self

