# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListPrivateAccessPolicesRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        policy_action: str = None,
        policy_ids: List[str] = None,
        status: str = None,
        tag_id: str = None,
        tag_name: str = None,
        user_group_id: str = None,
    ):
        # The ID of the private access application. The application ID cannot be used together with the private access tag ID for filtering. Sources of the value:
        #  - [ListPrivateAccessApplications](~~ListPrivateAccessApplications~~): Queries private access applications by batch.
        #  - [CreatePrivateAccessApplication](~~CreatePrivateAccessApplication~~): Creates a private access application.
        self.application_id = application_id
        # The name of the private access application.
        self.application_name = application_name
        # The page number of the current page that is returned during paginated queries. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The name of the private access policy. The name must be 1 to 128 characters in length and supports Chinese characters and uppercase and lowercase English letters. It can contain digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The number of entries per page that is set during paginated queries. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The action of the private access policy. Valid values:
        # - **Block**: Block.
        # - **Allow**: Allow.
        self.policy_action = policy_action
        # The collection of private access policy IDs. You can specify up to 100 private access policy IDs.
        self.policy_ids = policy_ids
        # The status of the private access policy. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.status = status
        # The ID of the private access tag. The tag ID cannot be used together with the application ID for filtering. Sources of the value:
        #  - [ListPrivateAccessTags](~~ListPrivateAccessTags~~): Queries private access tags by batch.
        #  - [CreatePrivateAccessTag](~~CreatePrivateAccessTag~~): Creates a private access tag.
        self.tag_id = tag_id
        # The name of the tag.
        self.tag_name = tag_name
        # The ID of the user group. Sources of the value:
        # - [ListUserGroups](~~ListUserGroups~~): Queries user groups by batch.
        # - [CreateUserGroup](~~CreateUserGroup~~): Creates a user group.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

