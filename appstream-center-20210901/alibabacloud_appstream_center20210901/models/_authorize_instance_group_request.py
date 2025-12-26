# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class AuthorizeInstanceGroupRequest(DaraModel):
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
        user_meta: main_models.AuthorizeInstanceGroupRequestUserMeta = None,
    ):
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # 持久会话ID。
        self.app_instance_persistent_id = app_instance_persistent_id
        self.authorize_user_group_ids = authorize_user_group_ids
        # The IDs of the users that you want to add to the authorization list of the delivery group. You can specify 1 to 100 user IDs.
        self.authorize_user_ids = authorize_user_ids
        self.avatar_id = avatar_id
        # This parameter is required.
        self.product_type = product_type
        self.un_authorize_user_group_ids = un_authorize_user_group_ids
        # The IDs of the users that you want to remove from the authorization list of the delivery group. You can specify 1 to 100 user IDs.
        self.un_authorize_user_ids = un_authorize_user_ids
        # The user information.
        self.user_meta = user_meta

    def validate(self):
        if self.user_meta:
            self.user_meta.validate()

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

        if self.user_meta is not None:
            result['UserMeta'] = self.user_meta.to_map()

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
            temp_model = main_models.AuthorizeInstanceGroupRequestUserMeta()
            self.user_meta = temp_model.from_map(m.get('UserMeta'))

        return self



class AuthorizeInstanceGroupRequestUserMeta(DaraModel):
    def __init__(
        self,
        ad_domain: str = None,
        type: str = None,
    ):
        # The AD domain name.
        self.ad_domain = ad_domain
        # The user type.
        # 
        # Valid values:
        # 
        # *   ad: Active Directory (AD) account
        # *   simple: convenience account
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

