# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_safconsole20250521 import models as main_models
from darabonba.model import DaraModel

class DescribeModelFeatureResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        http_status_code: int = None,
        request_id: str = None,
        result_object: List[main_models.DescribeModelFeatureResponseBodyResultObject] = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.result_object = result_object
        self.success = success

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['ResultObject'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('ResultObject') is not None:
            for k1 in m.get('ResultObject'):
                temp_model = main_models.DescribeModelFeatureResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeModelFeatureResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        feature_name: str = None,
        feature_type: str = None,
        name: str = None,
    ):
        self.default_value = default_value
        self.feature_name = feature_name
        self.feature_type = feature_type
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

