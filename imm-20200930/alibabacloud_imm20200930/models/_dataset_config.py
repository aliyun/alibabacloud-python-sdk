# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class DatasetConfig(DaraModel):
    def __init__(
        self,
        insights: main_models.InsightsConfig = None,
    ):
        self.insights = insights

    def validate(self):
        if self.insights:
            self.insights.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.insights is not None:
            result['Insights'] = self.insights.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Insights') is not None:
            temp_model = main_models.InsightsConfig()
            self.insights = temp_model.from_map(m.get('Insights'))

        return self

