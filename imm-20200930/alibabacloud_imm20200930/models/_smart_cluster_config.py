# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class SmartClusterConfig(DaraModel):
    def __init__(
        self,
        figure: main_models.FigureClusterConfig = None,
    ):
        self.figure = figure

    def validate(self):
        if self.figure:
            self.figure.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.figure is not None:
            result['Figure'] = self.figure.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Figure') is not None:
            temp_model = main_models.FigureClusterConfig()
            self.figure = temp_model.from_map(m.get('Figure'))

        return self

