# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class UpdateUserResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user: main_models.UpdateUserResponseBodyUser = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the RAM user.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user is not None:
            result['User'] = self.user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('User') is not None:
            temp_model = main_models.UpdateUserResponseBodyUser()
            self.user = temp_model.from_map(m.get('User'))

        return self

class UpdateUserResponseBodyUser(DaraModel):
    def __init__(
        self,
        comments: str = None,
        create_date: str = None,
        display_name: str = None,
        email: str = None,
        last_login_date: str = None,
        mobile_phone: str = None,
        provision_type: str = None,
        update_date: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        # The description.
        self.comments = comments
        # The time when the RAM user was created.
        self.create_date = create_date
        # The display name of the RAM user.
        self.display_name = display_name
        # The email address of the RAM user.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.email = email
        # The last time when the RAM user logged on to the Alibaba Cloud Management Console.
        self.last_login_date = last_login_date
        # The mobile phone number of the RAM user.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.mobile_phone = mobile_phone
        # The source of the RAM user. Valid values:
        # 
        # *   Manual: The RAM user is manually created in the RAM console.
        # *   SCIM: The RAM user is mapped by using System for Cross-domain Identity Management (SCIM).
        # *   CloudSSO: The RAM user is mapped from a CloudSSO user.
        self.provision_type = provision_type
        # The time when the information about the RAM user was updated.
        self.update_date = update_date
        # The ID of the RAM user.
        self.user_id = user_id
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date

        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone

        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')

        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')

        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

