# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class AuthorizeUsersForAppRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        authorize_user_ids: List[str] = None,
        product_type: str = None,
        un_authorize_user_ids: List[str] = None,
        user_meta: main_models.AuthorizeUsersForAppRequestUserMeta = None,
    ):
        # The application ID. The application must be deployed in the image used by the delivery group. You can obtain the ID from the Apps list returned by the [GetAppInstanceGroup](https://help.aliyun.com/document_detail/600836.html) operation.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The delivery group ID. You can call the [ListAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) operation to obtain the ID.
        # 
        # The application specified by AppId must be deployed in the image used by this delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The list of usernames to add authorization for the application. A maximum of 100 usernames can be specified in a single request.
        # 
        # At least one of AuthorizeUserIds and UnAuthorizeUserIds must be specified. You can also specify both. Adding authorization is subject to the authorized user quota for the application.
        self.authorize_user_ids = authorize_user_ids
        # The product type. Application-level authorization applies to WUYING Cloud Application delivery groups.
        # 
        # Valid values:
        # 
        # - CloudApp: WUYING Cloud Application.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The list of usernames to be unauthorized for the application. A maximum of 100 usernames can be specified in a single request.
        # 
        # At least one of AuthorizeUserIds and UnAuthorizeUserIds must be specified. You can also specify both. Removing authorizations is not subject to quota limits.
        self.un_authorize_user_ids = un_authorize_user_ids
        # The account information of the authorized user, which specifies the account type corresponding to the username.
        # 
        # - If the workspace to which the delivery group belongs is an AD workspace, **this parameter is required**: set Type to ad and set AdDomain to the AD domain bound to the workspace.
        # - If this parameter is not specified, the WUYING convenience account (simple) is used by default.
        self.user_meta = user_meta

    def validate(self):
        if self.user_meta:
            self.user_meta.validate()

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

        if self.user_meta is not None:
            result['UserMeta'] = self.user_meta.to_map()

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
            temp_model = main_models.AuthorizeUsersForAppRequestUserMeta()
            self.user_meta = temp_model.from_map(m.get('UserMeta'))

        return self

class AuthorizeUsersForAppRequestUserMeta(DaraModel):
    def __init__(
        self,
        ad_domain: str = None,
        type: str = None,
    ):
        # The AD domain name. Specify this parameter when Type is set to ad. The value must match the AD domain bound to the workspace of the delivery group.
        self.ad_domain = ad_domain
        # The account type. Default value: simple.
        # 
        # Valid values:
        # 
        # - ad: AD account.
        # - simple: WUYING convenience account.
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

