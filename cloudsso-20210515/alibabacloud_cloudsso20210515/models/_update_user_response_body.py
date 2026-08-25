# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class UpdateUserResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user: main_models.UpdateUserResponseBodyUser = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the user.
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
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        provision_type: str = None,
        status: str = None,
        update_time: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The time when the user was created. The value is displayed in UTC.
        self.create_time = create_time
        # The description of the user.
        self.description = description
        # The display name of the user.
        self.display_name = display_name
        # The email address of the user.
        self.email = email
        # The first name of the user.
        self.first_name = first_name
        # The last name of the user.
        self.last_name = last_name
        # The type of the user. Valid values:
        # 
        # - Manual: The user is manually created.
        # 
        # - Synchronized: The user is synchronized from an external identity provider (IdP).
        self.provision_type = provision_type
        # The status of the user. Valid values:
        # 
        # - Enabled: The logon of the user is enabled.
        # 
        # - Disabled: The logon of the user is disabled.
        self.status = status
        # The time when the information about the user was modified. The value is displayed in UTC.
        self.update_time = update_time
        # The ID of the user.
        self.user_id = user_id
        # The username of the user.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

