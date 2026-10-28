# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AuthorizeUsersForAppShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        authorize_user_ids: List[str] = None,
        product_type: str = None,
        un_authorize_user_ids: List[str] = None,
        user_meta_shrink: str = None,
    ):
        # The ID of the application. The application must be deployed in the image used by the app instance group. You can obtain the application ID from the Apps list returned by the [GetAppInstanceGroup](https://help.aliyun.com/document_detail/600836.html) operation.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the app instance group. You can call the [ListAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) operation to query the ID.
        # 
        # The application specified by AppId must be deployed in the image used by the app instance group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The list of usernames of the users to be authorized for the application. You can specify up to 100 usernames in a single call.
        # 
        # You must specify at least one of AuthorizeUserIds and UnAuthorizeUserIds, or specify both. Adding authorization is subject to the authorized user quota limit of the application.
        self.authorize_user_ids = authorize_user_ids
        # The product type. Application-level authorization applies to WUYING Cloud App app instance groups.
        # 
        # Valid values:
        # 
        # - CloudApp: WUYING Cloud App.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The list of usernames of the users whose authorization for the application is to be removed. You can specify up to 100 usernames in a single call.
        # 
        # You must specify at least one of AuthorizeUserIds and UnAuthorizeUserIds, or specify both. Removing authorization is not subject to quota limits.
        self.un_authorize_user_ids = un_authorize_user_ids
        # The account information of the authorized user, which is used to specify the account type corresponding to the username.
        # 
        # - **Required** if the workspace to which the app instance group belongs is an AD workspace: Set Type to ad, and set AdDomain to the AD domain bound to the workspace.
        # - If this parameter is not specified, the default account type is WUYING convenience account (simple).
        self.user_meta_shrink = user_meta_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.authorize_user_ids is not None:
            result['AuthorizeUserIds'] = self.authorize_user_ids

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.un_authorize_user_ids is not None:
            result['UnAuthorizeUserIds'] = self.un_authorize_user_ids

        if self.user_meta_shrink is not None:
            result['UserMeta'] = self.user_meta_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AuthorizeUserIds') is not None:
            self.authorize_user_ids = m.get('AuthorizeUserIds')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('UnAuthorizeUserIds') is not None:
            self.un_authorize_user_ids = m.get('UnAuthorizeUserIds')

        if m.get('UserMeta') is not None:
            self.user_meta_shrink = m.get('UserMeta')

        return self

