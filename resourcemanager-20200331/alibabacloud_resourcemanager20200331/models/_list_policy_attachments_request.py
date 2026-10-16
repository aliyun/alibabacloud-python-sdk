# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPolicyAttachmentsRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_name: str = None,
        policy_type: str = None,
        principal_name: str = None,
        principal_type: str = None,
        resource_group_id: str = None,
    ):
        # The language type. The description of the system access policy is returned in the specified language.
        # 
        # - en: English.
        # - zh-CN: Chinese.
        # - ja: Japanese.
        self.language = language
        # The page number.
        # 
        # Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # Policy Name of the access policy.
        # 
        # Policy Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        self.policy_name = policy_name
        # The type of the access policy. If this parameter is left empty, all types of access policies are listed.
        # 
        # - Custom: custom policy.
        # - System: system policy.
        self.policy_type = policy_type
        # The name of the principal.
        self.principal_name = principal_name
        # The authorization object type. If this parameter is left empty, all types of authorization objects are listed.
        # 
        # - IMSUser: Resource Access Management (RAM) user.
        # - IMSGroup: RAM user group.
        # - ServiceRole: RAM role.
        self.principal_type = principal_type
        # The ID of the resource group or the Alibaba Cloud account ID to which the resource group belongs. If this parameter is left empty, all authorization records under the current account are listed.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

