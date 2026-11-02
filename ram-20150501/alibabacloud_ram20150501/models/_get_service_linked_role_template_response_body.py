# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class GetServiceLinkedRoleTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        service_linked_role_template: main_models.GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplate = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The service-linked role template.
        self.service_linked_role_template = service_linked_role_template

    def validate(self):
        if self.service_linked_role_template:
            self.service_linked_role_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_linked_role_template is not None:
            result['ServiceLinkedRoleTemplate'] = self.service_linked_role_template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceLinkedRoleTemplate') is not None:
            temp_model = main_models.GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplate()
            self.service_linked_role_template = temp_model.from_map(m.get('ServiceLinkedRoleTemplate'))

        return self

class GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplate(DaraModel):
    def __init__(
        self,
        multiple_roles_allowed: bool = None,
        role_descriptions: main_models.GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplateRoleDescriptions = None,
        role_name_prefix: str = None,
        service_name: str = None,
        system_policy_name: str = None,
    ):
        # Indicates whether multiple roles are supported. Valid values:
        # 
        # - true: Multiple roles are supported.
        # - false: Multiple roles are not supported.
        self.multiple_roles_allowed = multiple_roles_allowed
        self.role_descriptions = role_descriptions
        # The prefix of the role name.
        self.role_name_prefix = role_name_prefix
        # The cloud service name.
        self.service_name = service_name
        # The name of the system policy attached to the role.
        self.system_policy_name = system_policy_name

    def validate(self):
        if self.role_descriptions:
            self.role_descriptions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.multiple_roles_allowed is not None:
            result['MultipleRolesAllowed'] = self.multiple_roles_allowed

        if self.role_descriptions is not None:
            result['RoleDescriptions'] = self.role_descriptions.to_map()

        if self.role_name_prefix is not None:
            result['RoleNamePrefix'] = self.role_name_prefix

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.system_policy_name is not None:
            result['SystemPolicyName'] = self.system_policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MultipleRolesAllowed') is not None:
            self.multiple_roles_allowed = m.get('MultipleRolesAllowed')

        if m.get('RoleDescriptions') is not None:
            temp_model = main_models.GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplateRoleDescriptions()
            self.role_descriptions = temp_model.from_map(m.get('RoleDescriptions'))

        if m.get('RoleNamePrefix') is not None:
            self.role_name_prefix = m.get('RoleNamePrefix')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('SystemPolicyName') is not None:
            self.system_policy_name = m.get('SystemPolicyName')

        return self

class GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplateRoleDescriptions(DaraModel):
    def __init__(
        self,
        role_description: List[main_models.GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplateRoleDescriptionsRoleDescription] = None,
    ):
        self.role_description = role_description

    def validate(self):
        if self.role_description:
            for v1 in self.role_description:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RoleDescription'] = []
        if self.role_description is not None:
            for k1 in self.role_description:
                result['RoleDescription'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role_description = []
        if m.get('RoleDescription') is not None:
            for k1 in m.get('RoleDescription'):
                temp_model = main_models.GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplateRoleDescriptionsRoleDescription()
                self.role_description.append(temp_model.from_map(k1))

        return self

class GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplateRoleDescriptionsRoleDescription(DaraModel):
    def __init__(
        self,
        description: str = None,
        language: str = None,
    ):
        self.description = description
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.language is not None:
            result['Language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        return self

