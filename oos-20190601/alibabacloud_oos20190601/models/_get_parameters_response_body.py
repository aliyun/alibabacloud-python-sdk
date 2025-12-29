# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class GetParametersResponseBody(DaraModel):
    def __init__(
        self,
        invalid_parameters: List[str] = None,
        parameters: List[main_models.GetParametersResponseBodyParameters] = None,
        request_id: str = None,
    ):
        # Invalid parameters.
        self.invalid_parameters = invalid_parameters
        # The information about the common parameters.
        self.parameters = parameters
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invalid_parameters is not None:
            result['InvalidParameters'] = self.invalid_parameters

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvalidParameters') is not None:
            self.invalid_parameters = m.get('InvalidParameters')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.GetParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetParametersResponseBodyParameters(DaraModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        parameter_version: int = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
        value: str = None,
    ):
        # The constraints of the common parameter.
        self.constraints = constraints
        # The user who created the common parameter.
        self.created_by = created_by
        # The time when the common parameter was created.
        self.created_date = created_date
        # The description of the common parameter.
        self.description = description
        # The ID of the common parameter.
        self.id = id
        # The name of the common parameter.
        self.name = name
        # The version number of the common parameter.
        self.parameter_version = parameter_version
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the common parameter.
        self.share_type = share_type
        # The tags.
        self.tags = tags
        # The type of the parameter.
        self.type = type
        # The user who updated the common parameter.
        self.updated_by = updated_by
        # The time when the parameter was updated.
        self.updated_date = updated_date
        # The value of the common parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.constraints is not None:
            result['Constraints'] = self.constraints

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.created_date is not None:
            result['CreatedDate'] = self.created_date

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.type is not None:
            result['Type'] = self.type

        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by

        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')

        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

