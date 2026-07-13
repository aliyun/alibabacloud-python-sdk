# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class QueryFeaturesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryFeaturesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryFeaturesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryFeaturesResponseBodyData(DaraModel):
    def __init__(
        self,
        features: List[main_models.QueryFeaturesResponseBodyDataFeatures] = None,
        instance_id: str = None,
        resource_name: str = None,
        target_scope: str = None,
    ):
        self.features = features
        self.instance_id = instance_id
        self.resource_name = resource_name
        self.target_scope = target_scope

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.target_scope is not None:
            result['TargetScope'] = self.target_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k1 in m.get('Features'):
                temp_model = main_models.QueryFeaturesResponseBodyDataFeatures()
                self.features.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('TargetScope') is not None:
            self.target_scope = m.get('TargetScope')

        return self

class QueryFeaturesResponseBodyDataFeatures(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        feature_code: str = None,
        supported: bool = None,
        unsupported_reason: str = None,
        unsupported_reason_code: str = None,
    ):
        self.description = description
        self.display_name = display_name
        self.feature_code = feature_code
        self.supported = supported
        self.unsupported_reason = unsupported_reason
        self.unsupported_reason_code = unsupported_reason_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.feature_code is not None:
            result['FeatureCode'] = self.feature_code

        if self.supported is not None:
            result['Supported'] = self.supported

        if self.unsupported_reason is not None:
            result['UnsupportedReason'] = self.unsupported_reason

        if self.unsupported_reason_code is not None:
            result['UnsupportedReasonCode'] = self.unsupported_reason_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('FeatureCode') is not None:
            self.feature_code = m.get('FeatureCode')

        if m.get('Supported') is not None:
            self.supported = m.get('Supported')

        if m.get('UnsupportedReason') is not None:
            self.unsupported_reason = m.get('UnsupportedReason')

        if m.get('UnsupportedReasonCode') is not None:
            self.unsupported_reason_code = m.get('UnsupportedReasonCode')

        return self

