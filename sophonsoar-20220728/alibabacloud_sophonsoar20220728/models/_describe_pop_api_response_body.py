# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribePopApiResponseBody(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        open_api_meta_list: List[main_models.DescribePopApiResponseBodyOpenApiMetaList] = None,
        pop_code: str = None,
        request_id: str = None,
        version: str = None,
    ):
        # The name of the API.
        self.api_name = api_name
        # The information about the API.
        self.open_api_meta_list = open_api_meta_list
        # The POP code of the Alibaba Cloud service.
        self.pop_code = pop_code
        # The request ID.
        self.request_id = request_id
        # The version of the API.
        self.version = version

    def validate(self):
        if self.open_api_meta_list:
            for v1 in self.open_api_meta_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        result['OpenApiMetaList'] = []
        if self.open_api_meta_list is not None:
            for k1 in self.open_api_meta_list:
                result['OpenApiMetaList'].append(k1.to_map() if k1 else None)

        if self.pop_code is not None:
            result['PopCode'] = self.pop_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        self.open_api_meta_list = []
        if m.get('OpenApiMetaList') is not None:
            for k1 in m.get('OpenApiMetaList'):
                temp_model = main_models.DescribePopApiResponseBodyOpenApiMetaList()
                self.open_api_meta_list.append(temp_model.from_map(k1))

        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribePopApiResponseBodyOpenApiMetaList(DaraModel):
    def __init__(
        self,
        description: str = None,
        example_value: str = None,
        name: str = None,
        required: bool = None,
        style: str = None,
        type: str = None,
    ):
        # The parameter description.
        self.description = description
        # The example value.
        self.example_value = example_value
        # The parameter name.
        self.name = name
        # Indicates whether the parameter is required.
        # 
        # *   true
        # *   false
        self.required = required
        self.style = style
        # The data type of the parameter field. Valid values:
        # 
        # *   **string**
        # *   **boolean**
        # *   **integer**
        # *   **long**
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.example_value is not None:
            result['ExampleValue'] = self.example_value

        if self.name is not None:
            result['Name'] = self.name

        if self.required is not None:
            result['Required'] = self.required

        if self.style is not None:
            result['Style'] = self.style

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExampleValue') is not None:
            self.example_value = m.get('ExampleValue')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('Style') is not None:
            self.style = m.get('Style')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

