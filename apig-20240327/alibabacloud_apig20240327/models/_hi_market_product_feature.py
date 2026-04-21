# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HiMarketProductFeature(DaraModel):
    def __init__(
        self,
        model_feature: main_models.HiMarketModelFeature = None,
    ):
        self.model_feature = model_feature

    def validate(self):
        if self.model_feature:
            self.model_feature.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_feature is not None:
            result['modelFeature'] = self.model_feature.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelFeature') is not None:
            temp_model = main_models.HiMarketModelFeature()
            self.model_feature = temp_model.from_map(m.get('modelFeature'))

        return self

