# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddPermissionPolicyToAccessConfigurationRequest(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        inline_policy_document: str = None,
        permission_policy_name: str = None,
        permission_policy_type: str = None,
    ):
        # The access configuration ID.
        self.access_configuration_id = access_configuration_id
        # The directory ID.
        self.directory_id = directory_id
        # The content of the inline policy.
        # 
        # The maximum length is 4,096 characters.
        # 
        # If PermissionPolicyType is set to Inline, this parameter is required. For more information about the syntax and structure of access policies, see [Access policy syntax and structure](https://help.aliyun.com/document_detail/93739.html).
        self.inline_policy_document = inline_policy_document
        # The name of the access policy. 
        # - If PermissionPolicyType is set to System, this parameter specifies the name of the system policy. Because RAM system policies are reused, you must obtain the system policy name from RAM.
        # - If PermissionPolicyType is set to Inline, this parameter specifies the name of the inline policy. You can customize the name. The name can be up to 32 characters in length.
        self.permission_policy_name = permission_policy_name
        # The type of the access policy. Valid values:
        # 
        # - System: system policy. Reuses the system policies of Resource Access Management (RAM).
        # - Inline: inline policy. A custom policy written based on the syntax and structure of RAM policies.
        self.permission_policy_type = permission_policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.inline_policy_document is not None:
            result['InlinePolicyDocument'] = self.inline_policy_document

        if self.permission_policy_name is not None:
            result['PermissionPolicyName'] = self.permission_policy_name

        if self.permission_policy_type is not None:
            result['PermissionPolicyType'] = self.permission_policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('InlinePolicyDocument') is not None:
            self.inline_policy_document = m.get('InlinePolicyDocument')

        if m.get('PermissionPolicyName') is not None:
            self.permission_policy_name = m.get('PermissionPolicyName')

        if m.get('PermissionPolicyType') is not None:
            self.permission_policy_type = m.get('PermissionPolicyType')

        return self

