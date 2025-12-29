# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class CreateSecretParameterResponseBody(DaraModel):
    def __init__(
        self,
        parameter: main_models.CreateSecretParameterResponseBodyParameter = None,
        request_id: str = None,
    ):
        # The information about the encryption parameter.
        self.parameter = parameter
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = main_models.CreateSecretParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m.get('Parameter'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateSecretParameterResponseBodyParameter(DaraModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        dkmsinstance_id: str = None,
        description: str = None,
        id: str = None,
        key_id: str = None,
        name: str = None,
        parameter_version: int = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The constraints of the encryption parameter.
        self.constraints = constraints
        # The user who created the encryption parameter.
        self.created_by = created_by
        # The time when the encryption parameter was created.
        self.created_date = created_date
        # The instance ID of the KMS instance.
        self.dkmsinstance_id = dkmsinstance_id
        # The description of the encryption parameter.
        self.description = description
        # The ID of the encryption parameter.
        self.id = id
        # The key ID of KMS that is used to encrypt the parameter.
        self.key_id = key_id
        # The name of the encryption parameter.
        self.name = name
        # The version number of the encryption parameter.
        self.parameter_version = parameter_version
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the encryption parameter.
        self.share_type = share_type
        # The tags.
        self.tags = tags
        # The type of the parameter.
        self.type = type
        # The user who updated the encryption parameter.
        self.updated_by = updated_by
        # The time when the encryption parameter was updated.
        self.updated_date = updated_date

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

        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.key_id is not None:
            result['KeyId'] = self.key_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')

        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

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

        return self

