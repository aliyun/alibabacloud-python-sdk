# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_safconsole20250521 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomerModuleMetaInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        http_status_code: int = None,
        request_id: str = None,
        result_object: main_models.DescribeCustomerModuleMetaInfoResponseBodyResultObject = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.result_object = result_object
        self.success = success

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

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

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeCustomerModuleMetaInfoResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCustomerModuleMetaInfoResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        feature_list: List[main_models.DescribeCustomerModuleMetaInfoResponseBodyResultObjectFeatureList] = None,
        feature_template: str = None,
    ):
        self.feature_list = feature_list
        self.feature_template = feature_template

    def validate(self):
        if self.feature_list:
            for v1 in self.feature_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FeatureList'] = []
        if self.feature_list is not None:
            for k1 in self.feature_list:
                result['FeatureList'].append(k1.to_map() if k1 else None)

        if self.feature_template is not None:
            result['FeatureTemplate'] = self.feature_template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_list = []
        if m.get('FeatureList') is not None:
            for k1 in m.get('FeatureList'):
                temp_model = main_models.DescribeCustomerModuleMetaInfoResponseBodyResultObjectFeatureList()
                self.feature_list.append(temp_model.from_map(k1))

        if m.get('FeatureTemplate') is not None:
            self.feature_template = m.get('FeatureTemplate')

        return self

class DescribeCustomerModuleMetaInfoResponseBodyResultObjectFeatureList(DaraModel):
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

