# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GenerateTemplatePolicyResponseBody(DaraModel):
    def __init__(
        self,
        policy: main_models.GenerateTemplatePolicyResponseBodyPolicy = None,
        policy_functions: List[main_models.GenerateTemplatePolicyResponseBodyPolicyFunctions] = None,
        request_id: str = None,
    ):
        # The information about the policy.
        self.policy = policy
        self.policy_functions = policy_functions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()
        if self.policy_functions:
            for v1 in self.policy_functions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        result['PolicyFunctions'] = []
        if self.policy_functions is not None:
            for k1 in self.policy_functions:
                result['PolicyFunctions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = main_models.GenerateTemplatePolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        self.policy_functions = []
        if m.get('PolicyFunctions') is not None:
            for k1 in m.get('PolicyFunctions'):
                temp_model = main_models.GenerateTemplatePolicyResponseBodyPolicyFunctions()
                self.policy_functions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GenerateTemplatePolicyResponseBodyPolicyFunctions(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_policy_functions: List[main_models.GenerateTemplatePolicyResponseBodyPolicyFunctionsActionPolicyFunctions] = None,
        requirement_level: str = None,
    ):
        self.action = action
        self.action_policy_functions = action_policy_functions
        self.requirement_level = requirement_level

    def validate(self):
        if self.action_policy_functions:
            for v1 in self.action_policy_functions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        result['ActionPolicyFunctions'] = []
        if self.action_policy_functions is not None:
            for k1 in self.action_policy_functions:
                result['ActionPolicyFunctions'].append(k1.to_map() if k1 else None)

        if self.requirement_level is not None:
            result['RequirementLevel'] = self.requirement_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        self.action_policy_functions = []
        if m.get('ActionPolicyFunctions') is not None:
            for k1 in m.get('ActionPolicyFunctions'):
                temp_model = main_models.GenerateTemplatePolicyResponseBodyPolicyFunctionsActionPolicyFunctions()
                self.action_policy_functions.append(temp_model.from_map(k1))

        if m.get('RequirementLevel') is not None:
            self.requirement_level = m.get('RequirementLevel')

        return self

class GenerateTemplatePolicyResponseBodyPolicyFunctionsActionPolicyFunctions(DaraModel):
    def __init__(
        self,
        functions: List[main_models.GenerateTemplatePolicyResponseBodyPolicyFunctionsActionPolicyFunctionsFunctions] = None,
        logical_resource_id: str = None,
        resource_type: str = None,
    ):
        self.functions = functions
        self.logical_resource_id = logical_resource_id
        self.resource_type = resource_type

    def validate(self):
        if self.functions:
            for v1 in self.functions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Functions'] = []
        if self.functions is not None:
            for k1 in self.functions:
                result['Functions'].append(k1.to_map() if k1 else None)

        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.functions = []
        if m.get('Functions') is not None:
            for k1 in m.get('Functions'):
                temp_model = main_models.GenerateTemplatePolicyResponseBodyPolicyFunctionsActionPolicyFunctionsFunctions()
                self.functions.append(temp_model.from_map(k1))

        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class GenerateTemplatePolicyResponseBodyPolicyFunctionsActionPolicyFunctionsFunctions(DaraModel):
    def __init__(
        self,
        function: str = None,
        operation_type: str = None,
        related_properties: List[str] = None,
        requirement_level: str = None,
    ):
        self.function = function
        self.operation_type = operation_type
        self.related_properties = related_properties
        self.requirement_level = requirement_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['Function'] = self.function

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.related_properties is not None:
            result['RelatedProperties'] = self.related_properties

        if self.requirement_level is not None:
            result['RequirementLevel'] = self.requirement_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            self.function = m.get('Function')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('RelatedProperties') is not None:
            self.related_properties = m.get('RelatedProperties')

        if m.get('RequirementLevel') is not None:
            self.requirement_level = m.get('RequirementLevel')

        return self

class GenerateTemplatePolicyResponseBodyPolicy(DaraModel):
    def __init__(
        self,
        statement: List[main_models.GenerateTemplatePolicyResponseBodyPolicyStatement] = None,
        version: str = None,
    ):
        # The statements that are contained in the policy.
        self.statement = statement
        # The version number.
        self.version = version

    def validate(self):
        if self.statement:
            for v1 in self.statement:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Statement'] = []
        if self.statement is not None:
            for k1 in self.statement:
                result['Statement'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.statement = []
        if m.get('Statement') is not None:
            for k1 in m.get('Statement'):
                temp_model = main_models.GenerateTemplatePolicyResponseBodyPolicyStatement()
                self.statement.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GenerateTemplatePolicyResponseBodyPolicyStatement(DaraModel):
    def __init__(
        self,
        action: List[str] = None,
        condition: Dict[str, Any] = None,
        effect: str = None,
        resource: str = None,
    ):
        # The operations that are performed on the specified resource.
        self.action = action
        # The condition that is required for the policy to take effect.
        self.condition = condition
        # The effect of the statement. Valid values:
        # 
        # *   Allow
        # *   Deny
        self.effect = effect
        # The objects that the statement covers. An asterisk (\\*) indicates all resources.
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.condition is not None:
            result['Condition'] = self.condition

        if self.effect is not None:
            result['Effect'] = self.effect

        if self.resource is not None:
            result['Resource'] = self.resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('Effect') is not None:
            self.effect = m.get('Effect')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        return self

