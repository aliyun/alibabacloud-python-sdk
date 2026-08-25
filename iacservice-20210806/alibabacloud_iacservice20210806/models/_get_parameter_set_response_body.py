# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetParameterSetResponseBody(DaraModel):
    def __init__(
        self,
        parameter_set: main_models.GetParameterSetResponseBodyParameterSet = None,
        request_id: str = None,
    ):
        # The parameter set details.
        self.parameter_set = parameter_set
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.parameter_set:
            self.parameter_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_set is not None:
            result['parameterSet'] = self.parameter_set.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameterSet') is not None:
            temp_model = main_models.GetParameterSetResponseBodyParameterSet()
            self.parameter_set = temp_model.from_map(m.get('parameterSet'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetParameterSetResponseBodyParameterSet(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        parameter_set_id: str = None,
        parameters: List[main_models.GetParameterSetResponseBodyParameterSetParameters] = None,
        relation_list: List[main_models.GetParameterSetResponseBodyParameterSetRelationList] = None,
    ):
        # The creation time in UTC, in the ISO 8601 format of YYYY-MM-DDTHH:mm:ssZ.
        self.create_time = create_time
        # The description of the parameter set.
        self.description = description
        # The name of the parameter set.
        self.name = name
        # The parameter set ID.
        self.parameter_set_id = parameter_set_id
        # The parameters in the parameter set.
        self.parameters = parameters
        # The association relationships.
        self.relation_list = relation_list

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.relation_list:
            for v1 in self.relation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.parameter_set_id is not None:
            result['parameterSetId'] = self.parameter_set_id

        result['parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['parameters'].append(k1.to_map() if k1 else None)

        result['relationList'] = []
        if self.relation_list is not None:
            for k1 in self.relation_list:
                result['relationList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parameterSetId') is not None:
            self.parameter_set_id = m.get('parameterSetId')

        self.parameters = []
        if m.get('parameters') is not None:
            for k1 in m.get('parameters'):
                temp_model = main_models.GetParameterSetResponseBodyParameterSetParameters()
                self.parameters.append(temp_model.from_map(k1))

        self.relation_list = []
        if m.get('relationList') is not None:
            for k1 in m.get('relationList'):
                temp_model = main_models.GetParameterSetResponseBodyParameterSetRelationList()
                self.relation_list.append(temp_model.from_map(k1))

        return self

class GetParameterSetResponseBodyParameterSetRelationList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The creation time in UTC, in the ISO 8601 format of YYYY-MM-DDTHH:mm:ssZ.
        self.create_time = create_time
        # The resource ID. When the resource type is ModuleVersion, the ID is composed of <moduleId>-<moduleversion>, such as mod-34535345df123fr-v3.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # - Module: template.
        # - ModuleVersion: template version.
        # - Task: task.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class GetParameterSetResponseBodyParameterSetParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        secret: bool = None,
        status: str = None,
        type: str = None,
        value: Any = None,
    ):
        # The name of the parameter.
        self.name = name
        # Specifies whether the parameter is secret. Secret parameters are hidden in API responses and console displays, and are stored with encryption.
        self.secret = secret
        # The parameter set status. Valid values:
        # 
        # - HAS_VALUE (default): A specific value is defined.
        # - EXPLICIT_NULL: Explicitly set to null.
        self.status = status
        # The type of the parameter (string/number/bool/map(string)/list(string)).
        self.type = type
        # The value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.secret is not None:
            result['secret'] = self.secret

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('secret') is not None:
            self.secret = m.get('secret')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

