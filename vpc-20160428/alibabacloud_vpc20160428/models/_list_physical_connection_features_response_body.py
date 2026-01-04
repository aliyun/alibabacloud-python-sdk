# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListPhysicalConnectionFeaturesResponseBody(DaraModel):
    def __init__(
        self,
        physical_connection_features: List[main_models.ListPhysicalConnectionFeaturesResponseBodyPhysicalConnectionFeatures] = None,
        request_id: str = None,
    ):
        # The list of Express Connect circuit features.
        self.physical_connection_features = physical_connection_features
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.physical_connection_features:
            for v1 in self.physical_connection_features:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PhysicalConnectionFeatures'] = []
        if self.physical_connection_features is not None:
            for k1 in self.physical_connection_features:
                result['PhysicalConnectionFeatures'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.physical_connection_features = []
        if m.get('PhysicalConnectionFeatures') is not None:
            for k1 in m.get('PhysicalConnectionFeatures'):
                temp_model = main_models.ListPhysicalConnectionFeaturesResponseBodyPhysicalConnectionFeatures()
                self.physical_connection_features.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPhysicalConnectionFeaturesResponseBodyPhysicalConnectionFeatures(DaraModel):
    def __init__(
        self,
        feature_key: str = None,
        feature_value: str = None,
    ):
        # The feature key of the Express Connect circuit. Valid values:
        # 
        # *   **SubifRateLimit**: subinterface throttling
        # *   **BFD Capability**: Bidirectional Forwarding Detection (BFD)
        # *   **DualStack**: Dual stack
        # *   **CEN**: When a virtual border router (VBR) is attached to a Cloud Enterprise Network (CEN) instance and BGP routes are advertised on the user side, attributes such as **as-path** and **community** are carried.
        # *   **CENv6**: When a VBR is attached to an IPv6 CEN instance and BGP routes are advertised on the user side, attributes such as **as-path** and **community** are carried.
        # *   **QOS**: The device supports configuring QOS policies on physical ports.
        # *   **MSHA**: The device supports fast switching groups between two VBRs.
        # *   **MULTI_MS_HA**: The device supports a maximum of eight VBRs that can be added to the same ECR.
        self.feature_key = feature_key
        # The feature value of the Express Connect circuit. Valid values:
        # 
        # *   **OK**: Supported
        # *   **NOK**: Not supported
        self.feature_value = feature_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_key is not None:
            result['FeatureKey'] = self.feature_key

        if self.feature_value is not None:
            result['FeatureValue'] = self.feature_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureKey') is not None:
            self.feature_key = m.get('FeatureKey')

        if m.get('FeatureValue') is not None:
            self.feature_value = m.get('FeatureValue')

        return self

