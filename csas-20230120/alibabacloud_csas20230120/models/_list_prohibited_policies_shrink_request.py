# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListProhibitedPoliciesShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        enabled: bool = None,
        match_mode: str = None,
        name: str = None,
        object_type: str = None,
        page_size: int = None,
        policy_ids: List[str] = None,
        policy_type: str = None,
        software_id_shrink: str = None,
        software_name: str = None,
        tag_id: str = None,
        tag_name: str = None,
        user_group_id: str = None,
    ):
        # The page number of the current page in a paged query. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Specifies whether the policy is enabled. Valid values:
        # - **true**: Enabled. The policy is delivered to endpoints and takes effect.
        # - **false**: Disabled. The policy configuration is retained but not delivered to endpoints.
        self.enabled = enabled
        # The effective scope. Valid values:
        # - **UserGroupAll**: Applies to all users under the current Alibaba Cloud account. No user group needs to be specified.
        # - **UserGroupNormal**: Applies only to users in the user groups specified by UserGroupIds.
        self.match_mode = match_mode
        # Policy Name of the software prohibition policy. Fuzzy match is supported. Policy Name can be up to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), and hyphens (-). Spaces are not supported.
        self.name = name
        # The object type of the controlled target. Valid values:
        # - **App**: Controls by prohibited software. The controlled objects are specified by SoftwareIds.
        # - **Tag**: Controls by prohibited software tag. The controlled objects are specified by TagIds. All prohibited software under the tag is controlled.
        self.object_type = object_type
        # The number of entries per page in a paged query. Valid values: 1 to 500.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The collection of software prohibition policy IDs. Duplicate values are not allowed.
        self.policy_ids = policy_ids
        # The action to take. Valid values:
        # - **Ban**: Blocks the software from running and displays a pop-up notification on the endpoint to alert the user.
        # - **BanSilent**: Blocks the software from running without notifying the user. The blocking is silent.
        # - **Warn**: Only displays a pop-up notification on the endpoint to alert the user without blocking the software from running.
        self.policy_type = policy_type
        # The unique identifier of the prohibited software.
        self.software_id_shrink = software_id_shrink
        # The name of the prohibited software. Fuzzy match is supported. The name can be up to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), and hyphens (-). Spaces are not supported.
        self.software_name = software_name
        # The prohibited software tag ID, used to filter policies that reference this tag. You can obtain the value from the following operations:
        # - [ListProhibitedTags](~~ListProhibitedTags~~): Lists prohibited software tags.
        # - [CreateProhibitedTag](~~CreateProhibitedTag~~): Creates a custom prohibited software tag.
        self.tag_id = tag_id
        # The name of the prohibited software tag. Fuzzy match is supported. The name can be up to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), and hyphens (-). Spaces are not supported.
        self.tag_name = tag_name
        # The user group ID, used to filter policies whose effective scope includes this user group. You can obtain the value from the following operations:
        # - [ListUserGroups](~~ListUserGroups~~): Lists user groups.
        # - [CreateUserGroup](~~CreateUserGroup~~): Creates a user group.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.name is not None:
            result['Name'] = self.name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.software_id_shrink is not None:
            result['SoftwareId'] = self.software_id_shrink

        if self.software_name is not None:
            result['SoftwareName'] = self.software_name

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('SoftwareId') is not None:
            self.software_id_shrink = m.get('SoftwareId')

        if m.get('SoftwareName') is not None:
            self.software_name = m.get('SoftwareName')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

