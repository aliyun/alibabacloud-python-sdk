# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeResourceGroupRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        new_resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        user_client_ip: str = None,
    ):
        # The language in which error messages are returned by the API. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        # 
        # Default value: **zh**.
        self.lang = lang
        # The ID of the resource group to which you want to shift the domain name.
        # 
        # You can view the resource group ID in the [Resource Management Console](https://resourcemanager.console.aliyun.com/resource-groups).
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The resource ID of the domain name.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type of the domain name. This parameter is fixed to “Domain” and does not need to be specified.
        self.resource_type = resource_type
        # The IP address of the user client.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

