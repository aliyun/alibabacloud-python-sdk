# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class GetFirewallFeatureResponseBody(DaraModel):
    def __init__(
        self,
        features: List[main_models.GetFirewallFeatureResponseBodyFeatures] = None,
        request_id: str = None,
    ):
        # The list of firewall feature statuses. This list always returns the statuses of application control and web filtering.
        self.features = features
        # The request ID.
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
                temp_model = main_models.GetFirewallFeatureResponseBodyFeatures()
                self.features.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFirewallFeatureResponseBodyFeatures(DaraModel):
    def __init__(
        self,
        feature_name: str = None,
        status: str = None,
    ):
        # The feature name. Valid values:
        # - **ApplicationControl**: Application control.
        # - **WebFilter**: Web filtering.
        self.feature_name = feature_name
        # The activation status of the feature. Valid values:
        # - **Enable**: Enabled.
        # - **Disable**: Disabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

