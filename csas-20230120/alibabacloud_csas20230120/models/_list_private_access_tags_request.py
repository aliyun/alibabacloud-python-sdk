# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListPrivateAccessTagsRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        policy_id: str = None,
        simple_mode: bool = None,
        tag_ids: List[str] = None,
    ):
        # The ID of the internal access application. You can obtain the application ID by calling the following operations:
        # 
        # *   [ListPrivateAccessApplications](~~ListPrivateAccessApplications~~): queries all internal access applications.
        # *   [CreatePrivateAccessApplication](~~CreatePrivateAccessApplication~~): creates an internal access application.
        self.application_id = application_id
        # The page number. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The name of the internal access tag. The name must be 1 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The number of entries per page. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the internal access policy. You can obtain the policy ID by calling the following operations:
        # 
        # *   [ListPrivateAccessPolices](~~ListPrivateAccessPolices~~): queries all internal access policies.
        # *   [CreatePrivateAccessPolicy](~~CreatePrivateAccessPolicy~~): creates an internal access policy.
        self.policy_id = policy_id
        # Specifies whether to enable the simple query mode. A value of true specifies that policy IDs are not queried.
        self.simple_mode = simple_mode
        # The IDs of internal access tags. You can specify up to 100 tag IDs.
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.simple_mode is not None:
            result['SimpleMode'] = self.simple_mode

        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('SimpleMode') is not None:
            self.simple_mode = m.get('SimpleMode')

        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')

        return self

