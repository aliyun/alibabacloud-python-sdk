# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AuthorizeInstanceGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_persistent_id: str = None,
        authorize_user_group_ids: List[str] = None,
        authorize_user_ids: List[str] = None,
        avatar_id: str = None,
        product_type: str = None,
        un_authorize_user_group_ids: List[str] = None,
        un_authorize_user_ids: List[str] = None,
        user_meta_shrink: str = None,
    ):
        # The delivery group ID. You can call the [ListAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) operation to obtain the value.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The persistent session ID.
        self.app_instance_persistent_id = app_instance_persistent_id
        # The list of user group IDs to be authorized.
        self.authorize_user_group_ids = authorize_user_group_ids
        # The list of usernames to be authorized for the delivery group. You can specify 1 to 100 usernames.
        self.authorize_user_ids = authorize_user_ids
        # The user avatar ID.
        # 
        # > This parameter is not available for public use.
        self.avatar_id = avatar_id
        # The product type.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The list of user group IDs to be deauthorized.
        self.un_authorize_user_group_ids = un_authorize_user_group_ids
        # The list of usernames to be deauthorized from the delivery group. You can specify 1 to 100 usernames.
        self.un_authorize_user_ids = un_authorize_user_ids
        # The user information.
        self.user_meta_shrink = user_meta_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id

        if self.authorize_user_group_ids is not None:
            result['AuthorizeUserGroupIds'] = self.authorize_user_group_ids

        if self.authorize_user_ids is not None:
            result['AuthorizeUserIds'] = self.authorize_user_ids

        if self.avatar_id is not None:
            result['AvatarId'] = self.avatar_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.un_authorize_user_group_ids is not None:
            result['UnAuthorizeUserGroupIds'] = self.un_authorize_user_group_ids

        if self.un_authorize_user_ids is not None:
            result['UnAuthorizeUserIds'] = self.un_authorize_user_ids

        if self.user_meta_shrink is not None:
            result['UserMeta'] = self.user_meta_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')

        if m.get('AuthorizeUserGroupIds') is not None:
            self.authorize_user_group_ids = m.get('AuthorizeUserGroupIds')

        if m.get('AuthorizeUserIds') is not None:
            self.authorize_user_ids = m.get('AuthorizeUserIds')

        if m.get('AvatarId') is not None:
            self.avatar_id = m.get('AvatarId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('UnAuthorizeUserGroupIds') is not None:
            self.un_authorize_user_group_ids = m.get('UnAuthorizeUserGroupIds')

        if m.get('UnAuthorizeUserIds') is not None:
            self.un_authorize_user_ids = m.get('UnAuthorizeUserIds')

        if m.get('UserMeta') is not None:
            self.user_meta_shrink = m.get('UserMeta')

        return self

