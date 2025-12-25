# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ServiceLinkedRole(DaraModel):
    def __init__(
        self,
        arn: str = None,
        assume_role_policy_document: str = None,
        create_date: str = None,
        description: str = None,
        is_service_linked_role: bool = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
    ):
        self.arn = arn
        self.assume_role_policy_document = assume_role_policy_document
        self.create_date = create_date
        self.description = description
        self.is_service_linked_role = is_service_linked_role
        self.role_id = role_id
        self.role_name = role_name
        self.role_principal_name = role_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['arn'] = self.arn

        if self.assume_role_policy_document is not None:
            result['assumeRolePolicyDocument'] = self.assume_role_policy_document

        if self.create_date is not None:
            result['createDate'] = self.create_date

        if self.description is not None:
            result['description'] = self.description

        if self.is_service_linked_role is not None:
            result['isServiceLinkedRole'] = self.is_service_linked_role

        if self.role_id is not None:
            result['roleId'] = self.role_id

        if self.role_name is not None:
            result['roleName'] = self.role_name

        if self.role_principal_name is not None:
            result['rolePrincipalName'] = self.role_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arn') is not None:
            self.arn = m.get('arn')

        if m.get('assumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('assumeRolePolicyDocument')

        if m.get('createDate') is not None:
            self.create_date = m.get('createDate')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('isServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('isServiceLinkedRole')

        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')

        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')

        if m.get('rolePrincipalName') is not None:
            self.role_principal_name = m.get('rolePrincipalName')

        return self

