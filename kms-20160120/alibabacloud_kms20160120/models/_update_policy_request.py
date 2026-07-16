# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePolicyRequest(DaraModel):
    def __init__(
        self,
        access_control_rules: str = None,
        description: str = None,
        name: str = None,
        permissions: str = None,
        resources: str = None,
    ):
        # The access control rule.
        # 
        # > For more information about how to query created access control rules, see [ListNetworkRules](https://help.aliyun.com/document_detail/2539433.html).
        self.access_control_rules = access_control_rules
        # The description.
        self.description = description
        # The name of the permission policy that you want to update.
        # 
        # This parameter is required.
        self.name = name
        # The operations that are supported by the updated policy. Valid values:
        # 
        # *   RbacPermission/Template/CryptoServiceKeyUser: allows you to perform cryptographic operations.
        # *   RbacPermission/Template/CryptoServiceSecretUser: allows you to perform secret-related operations.
        # 
        # You can select both.
        self.permissions = permissions
        # The key and secret that are allowed to access after the update.
        # 
        # *   Key: Enter a key in the `key/${KeyId}` format. To allow access to all keys of a KMS instance, enter key/\\*.
        # *   Secret: Enter a secret in the `secret/${SecretName}` format. To allow access to all secrets of a KMS instance, enter secret/\\*.
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_control_rules is not None:
            result['AccessControlRules'] = self.access_control_rules

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.permissions is not None:
            result['Permissions'] = self.permissions

        if self.resources is not None:
            result['Resources'] = self.resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlRules') is not None:
            self.access_control_rules = m.get('AccessControlRules')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        return self

