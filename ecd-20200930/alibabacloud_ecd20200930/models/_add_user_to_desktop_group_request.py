# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddUserToDesktopGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        desktop_group_id: str = None,
        desktop_group_ids: List[str] = None,
        end_user_ids: List[str] = None,
        region_id: str = None,
        simple_user_group_id: str = None,
        user_group_name: str = None,
        user_ou_path: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence of a request](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the cloud computer share.
        self.desktop_group_id = desktop_group_id
        # The IDs of the cloud computer shares.
        self.desktop_group_ids = desktop_group_ids
        # The IDs of the users to whom you want to grant permissions.
        self.end_user_ids = end_user_ids
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.simple_user_group_id = simple_user_group_id
        self.user_group_name = user_group_name
        self.user_ou_path = user_ou_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_group_ids is not None:
            result['DesktopGroupIds'] = self.desktop_group_ids

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.simple_user_group_id is not None:
            result['SimpleUserGroupId'] = self.simple_user_group_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        if self.user_ou_path is not None:
            result['UserOuPath'] = self.user_ou_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopGroupIds') is not None:
            self.desktop_group_ids = m.get('DesktopGroupIds')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SimpleUserGroupId') is not None:
            self.simple_user_group_id = m.get('SimpleUserGroupId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        if m.get('UserOuPath') is not None:
            self.user_ou_path = m.get('UserOuPath')

        return self

