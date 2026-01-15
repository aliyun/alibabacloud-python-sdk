# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFeatureOptionRequest(DaraModel):
    def __init__(
        self,
        feature_template: str = None,
    ):
        # This parameter is required.
        self.feature_template = feature_template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_template is not None:
            result['FeatureTemplate'] = self.feature_template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureTemplate') is not None:
            self.feature_template = m.get('FeatureTemplate')

        return self

