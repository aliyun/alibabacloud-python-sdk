# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelFeatureAvailableFeaturesRequest(DaraModel):
    def __init__(
        self,
        feature_name: str = None,
    ):
        self.feature_name = feature_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        return self

