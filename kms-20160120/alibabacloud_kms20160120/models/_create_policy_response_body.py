# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolicyResponseBody(DaraModel):
    def __init__(
        self,
        access_control_rules: str = None,
        arn: str = None,
        description: str = None,
        kms_instance: str = None,
        name: str = None,
        permissions: str = None,
        request_id: str = None,
        resources: str = None,
    ):
        # The name of the access control rule.
        self.access_control_rules = access_control_rules
        # The ARN of the permission policy.
        self.arn = arn
        # The description.
        self.description = description
        # The scope of the permission policy.
        self.kms_instance = kms_instance
        # The name of the permission policy.
        self.name = name
        # The operations that can be performed.
        self.permissions = permissions
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The key and secret that are allowed to access.
        # 
        # *   `key/*` indicates that all keys of the KMS instance can be accessed.
        # *   `secret/*` indicates all secrets of the KMS instance can be accessed.
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

        if self.arn is not None:
            result['Arn'] = self.arn

        if self.description is not None:
            result['Description'] = self.description

        if self.kms_instance is not None:
            result['KmsInstance'] = self.kms_instance

        if self.name is not None:
            result['Name'] = self.name

        if self.permissions is not None:
            result['Permissions'] = self.permissions

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resources is not None:
            result['Resources'] = self.resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlRules') is not None:
            self.access_control_rules = m.get('AccessControlRules')

        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KmsInstance') is not None:
            self.kms_instance = m.get('KmsInstance')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        return self

