# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConfigRulesForTargetRequest(DaraModel):
    def __init__(
        self,
        max_result: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        policy_type: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        tag_key: str = None,
        target_id: str = None,
        target_type: str = None,
        user_type: str = None,
    ):
        # The number of entries to return on each page.
        # 
        # Default value: 50. Maximum value: 1000.
        self.max_result = max_result
        # The token that is used to start the next query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The use scenario of the tag policy. This parameter specifies a filter condition for the query. Valid values:
        # 
        # - tags: enables tags with specified tag values to be added to resources.
        # 
        # - rg_inherit: enables resources in a resource group to automatically inherit tags from the resource group.
        self.policy_type = policy_type
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The tag key. This parameter specifies a filter condition for the query.
        self.tag_key = tag_key
        # The ID of the object. This parameter specifies a filter condition for the query.
        self.target_id = target_id
        # The type of the object. This parameter specifies a filter condition for the query. Valid values:
        # 
        # - USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # 
        # - ROOT: the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # - FOLDER: a folder other than the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # - ACCOUNT: a member in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # > The value of this parameter is not case-sensitive.
        self.target_type = target_type
        # The mode of the Tag Policy feature. This parameter specifies a filter condition for the query. Valid values:
        # 
        # - USER: single-account mode
        # 
        # - RD: multi-account mode
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        # 
        # > The value of this parameter is not case-sensitive.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_result is not None:
            result['MaxResult'] = self.max_result

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

