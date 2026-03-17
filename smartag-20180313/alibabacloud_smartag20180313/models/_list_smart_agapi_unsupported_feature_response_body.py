# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class ListSmartAGApiUnsupportedFeatureResponseBody(DaraModel):
    def __init__(
        self,
        features: List[main_models.ListSmartAGApiUnsupportedFeatureResponseBodyFeatures] = None,
        request_id: str = None,
    ):
        # A list of unsupported features.
        self.features = features
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.features:
            for v1 in self.features:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Features'] = []
        if self.features is not None:
            for k1 in self.features:
                result['Features'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k1 in m.get('Features'):
                temp_model = main_models.ListSmartAGApiUnsupportedFeatureResponseBodyFeatures()
                self.features.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSmartAGApiUnsupportedFeatureResponseBodyFeatures(DaraModel):
    def __init__(
        self,
        feature: str = None,
    ):
        # The unsupported feature.
        # 
        # For more information about the description of each feature, see the related API reference.
        self.feature = feature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature is not None:
            result['Feature'] = self.feature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')

        return self

