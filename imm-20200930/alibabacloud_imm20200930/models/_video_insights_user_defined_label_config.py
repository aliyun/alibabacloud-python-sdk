# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class VideoInsightsUserDefinedLabelConfig(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        labels: List[main_models.InsightsLabel] = None,
        mode: str = None,
    ):
        self.enable = enable
        self.labels = labels
        self.mode = mode

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.InsightsLabel()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

