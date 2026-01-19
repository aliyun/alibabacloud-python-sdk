# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeEventVariableTemplateListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: List[main_models.DescribeEventVariableTemplateListResponseBodyResultObject] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
        self.result_object = result_object

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeEventVariableTemplateListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class DescribeEventVariableTemplateListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        template_code: str = None,
        template_name: str = None,
        variables: List[main_models.DescribeEventVariableTemplateListResponseBodyResultObjectVariables] = None,
    ):
        # Template code.
        self.template_code = template_code
        # Template name.
        self.template_name = template_name
        # Variable list.
        self.variables = variables

    def validate(self):
        if self.variables:
            for v1 in self.variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_code is not None:
            result['templateCode'] = self.template_code

        if self.template_name is not None:
            result['templateName'] = self.template_name

        result['variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        self.variables = []
        if m.get('variables') is not None:
            for k1 in m.get('variables'):
                temp_model = main_models.DescribeEventVariableTemplateListResponseBodyResultObjectVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class DescribeEventVariableTemplateListResponseBodyResultObjectVariables(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        field_type: str = None,
        id: int = None,
        name: str = None,
        title: str = None,
        type: str = None,
    ):
        # Variable code
        self.code = code
        # Description information.
        self.description = description
        # Variable input type
        self.field_type = field_type
        # Primary key ID
        self.id = id
        # Variable name
        self.name = name
        # Title.
        self.title = title
        # Variable type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.description is not None:
            result['description'] = self.description

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

