# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListSecretParameterVersionsResponseBody(DaraModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        parameter_versions: List[main_models.ListSecretParameterVersionsResponseBodyParameterVersions] = None,
        request_id: str = None,
        total_count: int = None,
        type: str = None,
    ):
        # The user who created the encryption parameter.
        self.created_by = created_by
        # The time when the encryption parameter was created.
        self.created_date = created_date
        # The description of the encryption parameter.
        self.description = description
        # The ID of the encryption parameter.
        self.id = id
        # The number of entries returned per page.
        self.max_results = max_results
        # The name of the encryption parameter.
        self.name = name
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The information about the version of the encryption parameter.
        self.parameter_versions = parameter_versions
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The type of the encryption parameter.
        self.type = type

    def validate(self):
        if self.parameter_versions:
            for v1 in self.parameter_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.created_date is not None:
            result['CreatedDate'] = self.created_date

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['ParameterVersions'] = []
        if self.parameter_versions is not None:
            for k1 in self.parameter_versions:
                result['ParameterVersions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.parameter_versions = []
        if m.get('ParameterVersions') is not None:
            for k1 in m.get('ParameterVersions'):
                temp_model = main_models.ListSecretParameterVersionsResponseBodyParameterVersions()
                self.parameter_versions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListSecretParameterVersionsResponseBodyParameterVersions(DaraModel):
    def __init__(
        self,
        parameter_version: int = None,
        updated_by: str = None,
        updated_date: str = None,
        value: str = None,
    ):
        # The version number of the encryption parameter.
        self.parameter_version = parameter_version
        # The user who updated the encryption parameter.
        self.updated_by = updated_by
        # The time when the encryption parameter was updated.
        self.updated_date = updated_date
        # The value of the encryption parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version

        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by

        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')

        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')

        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

