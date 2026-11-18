# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFirewallFeatureRequest(DaraModel):
    def __init__(
        self,
        feature_name: str = None,
        status: str = None,
    ):
        # The name of the feature to enable. Valid values:
        # - **ApplicationControl**: application control
        # - **WebFilter**: web filtering
        # 
        # This parameter is required.
        self.feature_name = feature_name
        # The status of the feature. Only **Enable** is supported, which enables the feature. Specifying Disable or other values returns an error. This operation is idempotent if the feature is already enabled.
        # 
        # This parameter is required.
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

