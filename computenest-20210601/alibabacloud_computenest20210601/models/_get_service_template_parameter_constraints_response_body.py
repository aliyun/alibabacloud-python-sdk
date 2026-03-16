# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class GetServiceTemplateParameterConstraintsResponseBody(DaraModel):
    def __init__(
        self,
        family_constraints: List[str] = None,
        parameter_constraints: List[main_models.GetServiceTemplateParameterConstraintsResponseBodyParameterConstraints] = None,
        request_id: str = None,
    ):
        # The package family constraints.
        self.family_constraints = family_constraints
        # The constraints on the parameters.
        self.parameter_constraints = parameter_constraints
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.parameter_constraints:
            for v1 in self.parameter_constraints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.family_constraints is not None:
            result['FamilyConstraints'] = self.family_constraints

        result['ParameterConstraints'] = []
        if self.parameter_constraints is not None:
            for k1 in self.parameter_constraints:
                result['ParameterConstraints'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FamilyConstraints') is not None:
            self.family_constraints = m.get('FamilyConstraints')

        self.parameter_constraints = []
        if m.get('ParameterConstraints') is not None:
            for k1 in m.get('ParameterConstraints'):
                temp_model = main_models.GetServiceTemplateParameterConstraintsResponseBodyParameterConstraints()
                self.parameter_constraints.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetServiceTemplateParameterConstraintsResponseBodyParameterConstraints(DaraModel):
    def __init__(
        self,
        allowed_values: List[str] = None,
        association_parameter_names: List[str] = None,
        behavior: str = None,
        behavior_reason: str = None,
        original_constraints: List[main_models.GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints] = None,
        parameter_key: str = None,
        query_errors: List[main_models.GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsQueryErrors] = None,
        type: str = None,
    ):
        # The valid values of the parameter.
        self.allowed_values = allowed_values
        # The names of the associated parameters.
        self.association_parameter_names = association_parameter_names
        # The behavior of the parameter. Valid values:
        # 
        # *   NoLimit: No limit is imposed on the value of this parameter.
        # *   NotSupport: The value of this parameter cannot be queried.
        # *   QueryError: This parameter failed to be queried.
        # 
        # >  If AllowedValues is not returned, Behavior and BehaviorReason are returned, which indicate the behavior of the parameter and the reason for the behavior.
        self.behavior = behavior
        # The reason why the behavior of the parameter is returned.
        self.behavior_reason = behavior_reason
        # The original constraint information.
        self.original_constraints = original_constraints
        # The name of the parameter.
        self.parameter_key = parameter_key
        # The error details that are returned if the request fails.
        self.query_errors = query_errors
        # The data type of the parameter.
        self.type = type

    def validate(self):
        if self.original_constraints:
            for v1 in self.original_constraints:
                 if v1:
                    v1.validate()
        if self.query_errors:
            for v1 in self.query_errors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values

        if self.association_parameter_names is not None:
            result['AssociationParameterNames'] = self.association_parameter_names

        if self.behavior is not None:
            result['Behavior'] = self.behavior

        if self.behavior_reason is not None:
            result['BehaviorReason'] = self.behavior_reason

        result['OriginalConstraints'] = []
        if self.original_constraints is not None:
            for k1 in self.original_constraints:
                result['OriginalConstraints'].append(k1.to_map() if k1 else None)

        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key

        result['QueryErrors'] = []
        if self.query_errors is not None:
            for k1 in self.query_errors:
                result['QueryErrors'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')

        if m.get('AssociationParameterNames') is not None:
            self.association_parameter_names = m.get('AssociationParameterNames')

        if m.get('Behavior') is not None:
            self.behavior = m.get('Behavior')

        if m.get('BehaviorReason') is not None:
            self.behavior_reason = m.get('BehaviorReason')

        self.original_constraints = []
        if m.get('OriginalConstraints') is not None:
            for k1 in m.get('OriginalConstraints'):
                temp_model = main_models.GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints()
                self.original_constraints.append(temp_model.from_map(k1))

        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')

        self.query_errors = []
        if m.get('QueryErrors') is not None:
            for k1 in m.get('QueryErrors'):
                temp_model = main_models.GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsQueryErrors()
                self.query_errors.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsQueryErrors(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The error message.
        self.error_message = error_message
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints(DaraModel):
    def __init__(
        self,
        allowed_values: List[str] = None,
        property_name: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The valid values of the parameter.
        self.allowed_values = allowed_values
        # The property name.
        self.property_name = property_name
        # The name of the resource that is defined in the template.
        self.resource_name = resource_name
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values

        if self.property_name is not None:
            result['PropertyName'] = self.property_name

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')

        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

