# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeEventVariableTemplateBindResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeEventVariableTemplateBindResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeEventVariableTemplateBindResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeEventVariableTemplateBindResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        charge_variables: List[main_models.DescribeEventVariableTemplateBindResponseBodyResultObjectChargeVariables] = None,
        free_variables: List[main_models.DescribeEventVariableTemplateBindResponseBodyResultObjectFreeVariables] = None,
        template_code: str = None,
        total_count: str = None,
    ):
        # List of chargeable variables
        self.charge_variables = charge_variables
        # List of free variables
        self.free_variables = free_variables
        # Template code
        self.template_code = template_code
        # Total count
        self.total_count = total_count

    def validate(self):
        if self.charge_variables:
            for v1 in self.charge_variables:
                 if v1:
                    v1.validate()
        if self.free_variables:
            for v1 in self.free_variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['chargeVariables'] = []
        if self.charge_variables is not None:
            for k1 in self.charge_variables:
                result['chargeVariables'].append(k1.to_map() if k1 else None)

        result['freeVariables'] = []
        if self.free_variables is not None:
            for k1 in self.free_variables:
                result['freeVariables'].append(k1.to_map() if k1 else None)

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.charge_variables = []
        if m.get('chargeVariables') is not None:
            for k1 in m.get('chargeVariables'):
                temp_model = main_models.DescribeEventVariableTemplateBindResponseBodyResultObjectChargeVariables()
                self.charge_variables.append(temp_model.from_map(k1))

        self.free_variables = []
        if m.get('freeVariables') is not None:
            for k1 in m.get('freeVariables'):
                temp_model = main_models.DescribeEventVariableTemplateBindResponseBodyResultObjectFreeVariables()
                self.free_variables.append(temp_model.from_map(k1))

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class DescribeEventVariableTemplateBindResponseBodyResultObjectFreeVariables(DaraModel):
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
        # Variable description.
        self.description = description
        # Field type.
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

class DescribeEventVariableTemplateBindResponseBodyResultObjectChargeVariables(DaraModel):
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
        # Description of the variable.
        self.description = description
        # Field type.
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

