# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySampleConsistencyJobDifferenceRequest(DaraModel):
    def __init__(
        self,
        feature_name: str = None,
        feature_type: str = None,
        instance_id: str = None,
    ):
        self.feature_name = feature_name
        self.feature_type = feature_type
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

