# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFeatureTrialInfoRequest(DaraModel):
    def __init__(
        self,
        feature_type: str = None,
    ):
        # The feature type. Currently, only the free trial information of Tablestore backup can be queried.
        # 
        # This parameter is required.
        self.feature_type = feature_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        return self

